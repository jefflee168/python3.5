#-*- coding: utf-8 -*-

import csv

# 读取当前目录下的data.csv文件
with open('data.csv','r',encoding='utf-8') as csvfile:
     reader = csv.reader(csvfile)
     for row in reader:
         print(row)