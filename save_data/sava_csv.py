#-*- coding: utf-8 -*-

import csv

with open("data.csv",'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerows([['8886','Jeff','26'],['9999', 'Mike', '22'],['6666', 'Rose', '23']])
