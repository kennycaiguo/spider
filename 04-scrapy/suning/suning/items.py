# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SuningItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    big_classify = scrapy.Field()
    small_classify = scrapy.Field()
    shop = scrapy.Field()
    detail_href = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    press = scrapy.Field()
    publish_date = scrapy.Field()
