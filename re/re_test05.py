#-*- coding: utf-8 -*-

import re

# 以下演示re.match()函数的使用

string = "bpythonsfasdfapythondfsdfsad"
pattern1 = ".python."
result1 = re.match(pattern1,string)
result2 = re.match(pattern1,string).span()
print(result1)
print(result2)