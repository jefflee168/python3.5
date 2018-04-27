#-*- coding: utf-8 -*-

import pymysql as pymy

conn = pymy.connect(host='localhost',user='root',password='redhat',db='test001')
cs = conn.cursor()
id = '2018001'
name = 'Jeff'
age = 26

sql = "INSERT INTO students(id,name,age) VALUES (%s,%s,%s)"

try:
    cs.execute(sql,(id,name,age))
    conn.commit()
except:
    conn.rollback()

conn.close()