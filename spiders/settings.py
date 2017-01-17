# -*- coding: utf-8 -*-


BOT_NAME = 'scrapy'

SPIDER_MODULES = ['spiders.spiders']
NEWSPIDER_MODULE = 'spiders.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 0

COOKIES_ENABLED = False

MAX_PAGE_COUNT = 100

AUTOTHROTTLE_ENABLED=True

AUTOTHROTTLE_START_DELAY=3

AUTOTHROTTLE_MAX_DELAY=10


MONGODB = {
    # 'db': 'xianyu3',
    # 'collection': 'notebook',
    'host': '127.0.0.1',
    'port': 27017,
}

EXTENSIONS = {

    'scrapy.telnet.TelnetConsole': None,
}

DOWNLOAD_HANDLERS = {
  's3': None,
}

# ITEM_PIPELINES = {
#    'spiders.pipelines.XianyuPipeline': 300,
# }