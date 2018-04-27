#-*- coding: utf-8 -*-

import pymongo

# 连接方法1
client = pymongo.MongoClient(host='localhost',port=27017)

# 连接方法2
# client = pymongo.MongoClient('mongodb://localhost:27017/')

# 指定数据库
db = client['test']

# 指定集合名称 students
collection = db['students']

# 插入数据
student1 = {
    'id': '20180222',
    'name': 'jeff',
    'gender': 'male'
}
student2 = {
    'id': '20180111',
    'name': 'Mark',
    'gender': 'male'
}
# 调用collection的insert()方法插入数据
result = collection.insert([student1,student2])
print(result)
