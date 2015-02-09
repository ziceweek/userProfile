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
from tutorial.items import Site
import json
import re

class modSpider(CrawlSpider):
    name = "everySite"
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://site.douban.com/117080/",
        "http://site.douban.com/133306/",
        "http://site.douban.com/weibozhiyan798/"
    ]
    domain = 'http://www.douban.com/'

    rules = [
        Rule(SgmlLinkExtractor(allow=['site.douban.com/[^/]*/']), 'nav'),
        Rule(SgmlLinkExtractor(allow=['site.douban.com/[^/]*/room/[0-9]*/']), 'parse_mod'),
    ]

    def __int__(self, *args, **kwargs):
        super(modSpider, self).__init__(*args, **kwargs)
        self.start_urls = self.sites_to_cawler()
        for n in self.start_urls:
            print n

    # 导航栏上每一项都加入待爬的url
    def nav(self, response):

        sel = Selector(response)
        urls = []
        items = sel.xpath('//div[@class="nav-items"]')
        for a in items.xpath('.//a/@href'):
            url = a.extract().encode('utf-8')
            urls.append(url)
        for site_url in urls:
            yield scrapy.Request(url=site_url, meta={'url': site_url}, callback=self.parse_mod)

    def parse_mod(self, response):
        selector = Selector(response)
        mods = selector.xpath('//div[@class="main"]').xpath('.//div[@class="mod"]')
        site = Site()
        site['url'] = response.meta['url']
        print('--------------------mod\'s id is ')
        for m in mods:
            mod_ids = m.xpath('@id').re('(.*)-')
            if len(mod_ids) == 0:
                continue
            mod_id = mod_ids[0]
            if mod_id == 'board':
                print mod_id+' == board'
                board = m.extract()
                board_content = re.sub('<.*>', '', board)
                print board_content
                tmp_board = site['content']
                tmp_board += board_content
                site['content'] = tmp_board
            elif mod_id == 'notes':
                print mod_id+' == notes'
                notes_list = m.xpath('.//div[@class="summary"]/text()').extract()
                tmp_notes = site['content']
                for n in notes_list:
                    tmp_notes += n
                site['content'] = tmp_notes
            elif mod_id == 'miniblog':
                print mod_id+' == miniblog'
                # miniblog_list = []
                miniblogs = m.xpath('//div[@class="description"]/text()').extract()
                tmp_miniblog = site['content']
                for m in miniblogs:
                    # print m
                    # miniblog_list.append(m)
                    tmp_miniblog += m
                site['content'] = tmp_miniblog
            elif mod_id == 'forum':
                print mod_id+' == forum'
                forum_list = []
                rows = m.xpath('//tr')
                tmp_forum = site['content']
                for r in rows:
                    title = r.xpath('.//td')[0].xpath('.//a/text()').extract()
                    if len(title) != 0:
                        # print title[0]
                        # forum_list.append(title[0])
                        tmp_forum += title[0]
                site['content'] = tmp_forum
            else:
                print mod_id+'is not my like'
        return site

    def sites_to_cawler(self):
        json_file = file("../explore_yes.json")
        sites_info = json_file.read()
        s = json.loads(sites_info)
        json_file.close()
        urls_list = []
        for a in s:
            urls_list.append(a["url"])
        return urls_list

