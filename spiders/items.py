# -*- coding: utf-8 -*-

import scrapy


class XianyuItem(scrapy.Item):

      title = scrapy.Field()
      price = scrapy.Field()
      description = scrapy.Field()
      pic = scrapy.Field()
      area = scrapy.Field()
      info = scrapy.Field()

class jdItem(scrapy.Item):

      html = scrapy.Field()

