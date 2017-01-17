# -*- coding: utf-8 -*-

from settings import MONGODB
import pymongo


class Top250Pipeline(object):

    def process_item(self, item, spider):

        if spider.name == 'top250':

            self._db = 'douban'
            self._collection = 'top250'
            self._host = MONGODB.get('host')
            self._port = MONGODB.get('port')
            self._client = pymongo \
                .MongoClient(host=self._host, port=self._port) \
                .get_database(self._db) \
                .get_collection(self._collection)

            for data in item:
                if not data:
                    print ('Missing data!')
            self._client.create_index([('url', pymongo.DESCENDING)], background=True)
            self._client.update_one(filter={'url': item['url']}, update={'$set': dict(item)}, upsert=True)

        elif spider.name == 'top250_info':

            self._db = 'douban'
            self._collection = 'top250_info'
            self._host = MONGODB.get('host')
            self._port = MONGODB.get('port')
            self._client = pymongo \
                .MongoClient(host=self._host, port=self._port) \
                .get_database(self._db) \
                .get_collection(self._collection)

            for data in item:
                if not data:
                    print ('Missing data!')
            self._client.create_index([('title', pymongo.DESCENDING)], background=True)
            self._client.update_one(filter={'title': item['title']}, update={'$set': dict(item)}, upsert=True)
            return item


