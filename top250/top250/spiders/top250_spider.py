# -*- coding:utf-8 -*-

import scrapy
from scrapy import Request
from scrapy.log import logger
from scrapy.selector import Selector
from .. import items
from .. import settings
import random, string


class top250(scrapy.Spider):

    name = 'top250'

    allowed_domains = ['movie.douban.com']

    url_template = 'https://movie.douban.com/top250?start={page}&filter='

    start_urls = [
        url_template.format(page = x) for x in range(0,250,25)
        ]

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
            yield Request(url=p, headers=self.default_headers, callback=self.parse)

    def parse(self, response):
        if not response.body:
            logger.error(msg='there is no response body ,please go and check it ')
            return

        all_item_urls = Selector(response).xpath('//div[@class  = "hd"]/a')

        for i in all_item_urls:
            item = items.Top250ItemUrl()
            item['url'] = i.xpath('./@href').extract()[0]

            yield item
