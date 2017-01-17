# -*- coding: utf-8 -*-

import scrapy


class Top250ItemUrl(scrapy.Item):
    url = scrapy.Field()



class Top250Item(scrapy.Item):

    rank = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    rating = scrapy.Field()
    rating_people = scrapy.Field()
    intro = scrapy.Field()
    style = scrapy.Field()
    area = scrapy.Field()





