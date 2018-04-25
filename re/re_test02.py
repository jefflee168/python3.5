#-*- coding: utf-8 -*-

import re

pattern="\t"
string='''http://hao1314.cn
http://hao123.com'''
result1 = re.search(pattern,string)
print(result1)