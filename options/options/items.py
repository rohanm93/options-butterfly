# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OptionsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    stockName = scrapy.Field()
    currentPrice = scrapy.Field()
    strikePrice = scrapy.Field()
    askPrice = scrapy.Field()
    askQty = scrapy.Field()
    oi = scrapy.Field()
    # 'c' = call, 'p' = put
    cp = scrapy.Field()