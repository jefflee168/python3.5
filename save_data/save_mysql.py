#-*- coding: utf-8 -*-

import pymysql

conn = pymysql.connect(host='localhost',user='root',password='redhat',port=3306)
cursor = conn.cursor()
# 查询mysql版本
cursor.execute('SELECT VERSION()')
data = cursor.fetchall()
print('Data version:',data)

# 创建数据库test001
cursor.execute('CREATE DATABASE test001 DEFAULT CHARACTER SET utf8')
conn.close()