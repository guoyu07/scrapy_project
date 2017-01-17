# -*- coding: utf-8 -*-

from settings import MONGODB
import pymongo


class XianyuPipeline(object):

    def __init__(self):
        self._db = 'xianyu3'
        self._collection = 'notebook'
        self._host = MONGODB.get('host')
        self._port = MONGODB.get('port')
        self._client = pymongo \
            .MongoClient(host=self._host, port=self._port) \
            .get_database(self._db) \
            .get_collection(self._collection)

    def process_item(self, item, spider):
        for data in item:
            if not data:
                print ('Missing data!')
        self._client.create_index([('title', pymongo.DESCENDING)], background=True)
        self._client.update_one(filter={'title': item['title']}, update={'$set': dict(item)}, upsert=True)
        return item
