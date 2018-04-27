#-*- coding: utf-8 -*-

import pymysql as pymy

conn = pymy.connect(host='localhost',user='root',password='redhat',db='test001')
cs = conn.cursor()

data = {
    'id': '2019003',
    'name': 'Charlie',
    'age': '28'
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table,keys=keys,values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
try:
    if cs.execute(sql,tuple(data,values())*2):
        print('Successful')
        conn.commit()
except:
    print('Failed')
    conn.rollback()

conn.close()