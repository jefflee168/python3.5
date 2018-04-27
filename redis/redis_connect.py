#-*- coding:utf-8 -*-

from redis import StrictRedis

redis = StrictRedis(host='localhost',port=6379,db=0,password='redhat')
redis.set('name','jeff')
print(redis.get('name'))