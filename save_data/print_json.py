#-*- coding: utf-8

import json

data = [{
    'name':'jeff',
    'gender':'male',
    'birthday':'1988-02-28'
}]
with open('data.json','w') as file:
    file.write(json.dumps(data))