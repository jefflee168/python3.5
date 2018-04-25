#-*- coding: utf-8 -*-

import re

# 以下演示全局匹配函数

string = """dsafdfgadhellosxxcvxcv.xvxcvxwerewrhellotewte
           02840hello0808024324dsfahello4234324"""

# 预编译
pattern1 = ".hello."

# 找出所有结果
result1 = re.compile(pattern1).findall(string)

# 打印结果
print(result1)