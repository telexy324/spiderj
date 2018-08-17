# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_no = scrapy.Field()
    tags = scrapy.Field()
    actress_no = scrapy.Field()
    #url = scrapy.Field()