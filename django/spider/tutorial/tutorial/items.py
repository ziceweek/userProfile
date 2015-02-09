# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Category(scrapy.Item):
    url = scrapy.Field()
    subtag = scrapy.Field()
    tagID = scrapy.Field()
    pass


class DoubanGroup(scrapy.Item):
    category = scrapy.Field()
    category_ID = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    groupID = scrapy.Field()
    pass


class Site(scrapy.Item):
    url = scrapy.Field()
    content = scrapy.Field()
    pass