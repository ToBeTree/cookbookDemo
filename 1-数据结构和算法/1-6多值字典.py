# 构建多值字典
# d = {
#    'a': [1, 2, 3]，
#    'b': {1, 2, 3}
#    }
# 也可以直接使用collections中的defaultdict模块
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(1)
d['c'].append(2)
print(d)
print(d['a'])
