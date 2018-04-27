#-*- coding: utf-8 -*-

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['test']
collection = db['students']

# 查询数据
result = collection.find_one({'name':'Mark'})
print(type(result))
print(result)