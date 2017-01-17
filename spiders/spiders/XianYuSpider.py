# -*- coding: UTF-8 -*-



import scrapy
from scrapy import Request
from scrapy.log import logger
from scrapy.selector import Selector
from .. import items
from .. import settings
import random


class xianyu(scrapy.Spider):

    name = 'xianyu'

    allowed_domains = ['s.2.taobao.com']

    url_template = 'https://s.2.taobao.com/list/list.htm?spm=2007.100033' \
                   '7.0.0.hKA1I0&catid=50100423&st_trust=1&page={page}&ist=0'


    start_urls = [
        url_template.format(page=x) for x in range(1,settings.MAX_PAGE_COUNT+1)
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

        all_items =  Selector(response).xpath('//ul[@class = "item-lists"]/li')

        for i in range(len(all_items)):
            item = items.XianyuItem()
            item['title'] = all_items[i].xpath('//h4[@class ="item-title"]//a[@target = "_blank"]/text()').extract()[i]
            item['price'] = all_items[i].xpath('//span[@class ="price"]//em/text()').extract()[i]
            item['description'] = all_items[i].xpath('//div[@class = "item-description"]/text()').extract()[i]
            item['pic'] = ("https:" + str(all_items[i].xpath('//div[@class = "item-pic sh-pic120"]//img/@src')
                                          .extract()[i])).replace('_120x120','').strip()
            item['area'] = all_items[i].xpath('//div[@class="seller-location"]/text()').extract()[i]
            item["info"] = "https:" + all_items[i].xpath('//a[@target = "_blank"]/@href').extract()[i]
            yield item
