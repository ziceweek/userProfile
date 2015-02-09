# coding:utf-8
__author__ = 'zice'
import scrapy
from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import Category, DoubanGroup
import json

class DBSpider2(Spider):
    name = "explore2"
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://www.douban.com/explore/",
    ]
    domain = 'http://www.douban.com/'

    def parse(self, response):

        sel = Selector(response)
        items = []
        for a in sel.xpath('//a[@class="cate-a"]'):
            item = Category()
            item['url'] = a.xpath('@href').extract()[0].encode('utf-8')
            item['subtag'] = a.xpath('text()').extract()[0].encode('utf-8')
            # print(a.xpath('text()').extract()[0].encode('utf-8')+':'+a.xpath('@href').extract()[0].encode('utf-8'))
            items.append(item)
        for item in items:
            yield scrapy.Request(url='http://www.douban.com/'+item['url'], callback=self.parse_item)

    def parse_item(self, response):
        selector = Selector(response)
        groups = []
        for g in selector.xpath('//div[@class="explore-item"]'):
            group = DoubanGroup()
            group['url'] = g.xpath('//a[@href]').extract()[0].encode('utf-8')
            group['name'] = g.xpath('//a[@title]').extract()[0].encode('utf-8')
            print(group['name']+":"+group['url'])
            groups.append(group)
        return groups


class DBSpider(CrawlSpider):
    name = "explore"
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://www.douban.com/explore/",
    ]
    domain = 'http://www.douban.com/'

    rules = [
        Rule(SgmlLinkExtractor(allow=['/explore/']), 'parse_explore'),
        Rule(SgmlLinkExtractor(allow=['/explore/?tag=.*']), 'parse_group'),
        Rule(SgmlLinkExtractor(allow=['/j/explore/site/tag/.*']), 'process_pages')
    ]

    def parse_explore(self, response):

        sel = Selector(response)
        items = []
        for a in sel.xpath('//a[@class="cate-a"]'):
            item = Category()
            item['url'] = a.xpath('@href').extract()[0].encode('utf-8')
            item['tagID'] = a.xpath('@data-tag').extract()[0].encode('utf-8')
            item['subtag'] = a.xpath('text()').extract()[0].encode('utf-8')
            # print(a.xpath('text()').extract()[0].encode('utf-8')+':'+a.xpath('@href').extract()[0].encode('utf-8'))
            items.append(item)
        for item in items:
            yield scrapy.Request(url='http://www.douban.com/'+item['url'], meta={'item': item}, callback=self.parse_group)

    def parse_item(self, response):
        item = response.meta['item']
        selector = Selector(response)
        selector_sites = selector.xpath('//div[@id="explore-sites"]')
        groups = []
        for g in selector_sites.xpath('.//div[@class="title"]'):
            group = DoubanGroup()
            group['category'] = item['subtag']
            group['url'] = g.xpath('.//@href').extract()[0].encode('utf-8')
            group['name'] = g.xpath('.//a/text()').extract()[0].encode('utf-8')
            print(group['category']+'-----'+group['name'])
            groups.append(group)
        return groups

    def parse_group(self, response):
        item = response.meta['item']
        selector = Selector(response)
        selector_sites = selector.xpath('//div[@id="explore-sites"]')
        groups = []
        for g in selector_sites.xpath('.//div[@class="title"]'):
            group = DoubanGroup()
            group['category'] = item['subtag']
            group['category_ID'] = item['tagID'].encode('utf-8')
            group['url'] = g.xpath('.//@href').extract()[0].encode('utf-8')
            group['name'] = g.xpath('.//a/text()').extract()[0].encode('utf-8')
            print(group['category']+'-----'+group['name'])
            groups.append(group)

        selector2 = Selector(response)
        selector_sites_ids = []
        print ('------------找id：')
        # for a in selector2.xpath('//div[@class="content"]'):
        #     print a.xpath('.//a[@class="lnk-follow a_show_login"]/@data-site-id').extract()[0].encode('utf-8')
        for a in selector2.xpath('.//a[@class="lnk-follow a_show_login"]/@data-site-id').extract():
            print a
            selector_sites_ids.append(a)
        seq = ','
        last_ids = seq.join(selector_sites_ids)
        return scrapy.Request(url='http://www.douban.com/j/explore/site/tag/'+item['tagID']+'/?last_id='+last_ids, meta={'page': 0, 'last_ids': last_ids, 'item':item, 'groups':groups}, callback=self.process_pages)



        # print('目标链接为：-----》》http://www.douban.com/j/explore/site/tag/'+item['tagID'].encode('utf-8')+'/?last_id='+last_ids.encode('utf-8'))
        # return groups


    def process_pages(self, response):
        groups = response.meta['groups']
        item = response.meta['item']
        print response.body
        json_content = json.loads(response.body)
        print json_content["html"]
        # selector = Selector(json_content["html"])
        for g in Selector(text=json_content["html"]).xpath('.//div[@class="title"]'):
            group = DoubanGroup()
            group['category'] = item['subtag']
            group['category_ID'] = item['tagID'].encode('utf-8')
            group['url'] = g.xpath('.//@href').extract()[0].encode('utf-8')
            group['name'] = g.xpath('.//a/text()').extract()[0].encode('utf-8')
            print(group['category']+'-----'+group['name'])
            groups.append(group)
        page = response.meta['page']
        print('第'+str(page)+'页')
        if page < 4:
            selector_sites_id = Selector(text=json_content["html"]).xpath('.//a[@class="lnk-follow"]')
            seq = ','
            new_last_ids = seq.join(selector_sites_id)
            page += 1
            print('第'+str(page)+'页')
            return scrapy.Request(url='http://www.douban.com/j/explore/site/tag/'+item['tagID']+'/?last_id='+response.meta['last_ids']+','+new_last_ids, meta={'page': page, 'item': item, 'last_ids':response.meta['last_ids']+','+new_last_ids, 'groups': groups}, callback=self.process_pages)
        else:
            return groups

