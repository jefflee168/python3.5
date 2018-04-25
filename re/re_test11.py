#-*- coding: utf-8 -*-

import re

# 匹配电子邮箱

pattern = "\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w)*"
string = "<a href='http://www.baidu.com'>百度首页</a><br /><a href='hello@hotmail.cn'>测试电子邮箱</a>"
result = re.search(pattern,string)
print(result)
