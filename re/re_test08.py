#-*- coding: utf-8 -*-

import re

# 以下演示re.sub()函数:其功能为实现字符替换

string = "wehisfasfhi90090hifsdafashillkj"
pattern = ".hi."

# 替换所有
result1 = re.sub(pattern,"hey",string)

# 最多替换2个
result2 = re.sub(pattern,'hello',string,2)

# 打印结果
print(result1)
print(result2)
