# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request
from scrapy.log import logger
import random
from .. import items
import codecs

class jd(scrapy.Spider):

    name = 'jd'

    allowed_domains = ['item.jd.com']

    url_template = 'https://sclub.jd.com/comment/productPageComments.action?productId=4006502' \
                   '&score=0&sortType=3&page={page}&pageSize=10&isShadowSku=0&callback=fetchJSON_comment98vv178'


    start_urls = [
        url_template.format(page=x) for x in random.sample(range(100), 100)
                  ]

    user_agents =['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.'
                 '0.2227.1 Safari/537.36',
                 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36' ,
                 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.'
                 '2062.124 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0'
                 '.2049.0 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

                 ]


    default_headers = {
        'User-Agent': random.choice(user_agents),
        # 'cookie' : 

    }


    def start_requests(self):
        for p in self.start_urls:
            yield Request(url=p, headers=self.default_headers, callback=self.parse)

    def parse(self, response):
        if not response.body:
            logger.error(msg='there is no response body ,please go and check it ')
            return
        html = str(response.body)
        # item = items.jdItem()
        # item['html'] = html
        # yield item


        with open("page.txt", "a") as f:
            f.write(html)
            f.close()
