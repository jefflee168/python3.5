#-*- coding: utf-8 -*-

import re

# 以下演示re.search()函数的使用方法

string = "uouewrelpythonsfsljlljpythonfgl"
pattern1 = ".python."
result1 = re.search(pattern1,string)
result2 = re.match(pattern1,string)
print(result1)
print(result2)