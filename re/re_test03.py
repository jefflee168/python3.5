#-*- coding: utf-8 -*-

import re

pattern1 = "^abc"
pattern2 = "xyz$"
string1 ="abcasdfasfdsaf"
string2 ="sadfrtwerewxyz"
result1 = re.search(pattern1,string1)
result2 = re.search(pattern2,string2)
print(result1)
print(result2)