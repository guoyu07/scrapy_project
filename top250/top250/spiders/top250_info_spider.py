# -*- coding:utf-8 -*-

import scrapy
from scrapy import Request
from scrapy.log import logger
from scrapy.selector import Selector
from .. import items
from .. import settings
import random, string,pymongo


class top250(scrapy.Spider):

    name = 'top250_info'

    allowed_domains = ['movie.douban.com']

    client = pymongo.MongoClient('localhost', 27017, connect=False)

    douban = client['douban']

    top250 = douban['top250']

    start_urls = top250.find().limit(250)

    user_agents = [
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.'
        '0.2227.1 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.'
        '2062.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0'
        '.2049.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'
    ]

    default_headers = {
        'User-Agent': random.choice(user_agents),
        # 'cookie': "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11)) + ';'
    }

    def start_requests(self):
        for p in self.start_urls:
            yield Request(url=p['url'], headers=self.default_headers, callback=self.parse)

    def parse(self, response):
        if not response.body:
            logger.error(msg='there is no response body ,please go and check it ')
            return

        i = Selector(response)
        item = items.Top250Item()
        item['rank'] = i.xpath('//span[@class = "top250-no"]/text()').extract()[0]
        item['title'] = i.xpath('//span[@property="v:itemreviewed"]/text()').extract()[0]
        item['year'] = i.xpath('//span[@class = "year"]/text()').extract()[0]
        item['area'] = i.xpath('//div[@id = "info"]/br[4]/following-sibling::text()').extract()[1]
        item['rating'] = i.xpath('//strong[@class="ll rating_num"]/text()').extract()[0]
        item['rating_people'] = i.xpath('//span[@property="v:votes"]/text()').extract()[0]
        item['intro'] = i.xpath('//span[@property="v:summary"]/text()').extract()
        item['style'] = i.xpath('//span[@property="v:genre"]/text()').extract()

        yield item
