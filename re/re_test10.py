#-*- coding: utf-8 -*-

import re

# 匹配电话号码

pattern = "\d{4}-\d{7}|\d{3}-\d{8}"
string = "020-3454756867867"
result = re.search(pattern,string)
print(result)