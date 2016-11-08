# 字典排序用collections模块中的OrderDict
# 但是需要消耗双倍空间资源
from collections import OrderedDict

d = OrderedDict()
d['food'] = 1
# d['food'] = 2
d['apple'] = 2
d['stupid'] = 3

for key in d:
    print(key, d[key])
# json格式化
import json

a = json.dumps(d)
print(a)
