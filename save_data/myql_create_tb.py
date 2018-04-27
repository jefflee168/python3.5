#-*- coding: utf-8 -*-

import pymysql as pymy

# 创建表格 students

conn = pymy.connect(host='localhost',user='root',password='redhat',db='test001')
cs = conn.cursor()
sql = """ CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,
          age INT NOT NULL,PRIMARY KEY (id))"""

cs.execute(sql)
conn.close()