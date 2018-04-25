#-*- coding: utf-8 -*-

import re

# 案例：匹配.com 或者.cn

pattern = "[a-zA-Z]+://[^\s]*[.com|.cn]"
string = "<a href='http://www.baidu.com'>百度首页</a>"
result = re.search(pattern,string)
print(result)

# 正则说明："://"为固定的，其前面的为大小字母都可以，其后与.com或者.cn不能有空格
# 不能有空格用 [^\s]* 表示