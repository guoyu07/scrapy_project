import random, string,pymongo

client = pymongo.MongoClient('localhost', 27017)

douban = client['douban']

top250 = douban['top250']

for i in top250.find():
    print i['url']

