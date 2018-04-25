#-*- coding: utf-8 -*-

import re

pattern1 = "p.*y"
pattern2 = "p.?y"
string1 = "pypyasdfapysdfpy"
result1 = re.search(pattern1,string1)
result2 = re.search(pattern2,string1)
print(result1)
print(result2)