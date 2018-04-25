#-*- coding: utf-8 -*-

import urllib.request
import urllib.error

try:
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.URLError as e:
    print(e.code)
    print(e.reason)