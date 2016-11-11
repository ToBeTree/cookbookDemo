# 使用collections.chainmap将两个字典合并成一个字典
# 在逻辑上合并，实际不是
# 合并时有相同的键/值，采用第一个字典的键/值
from collections import ChainMap
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
# sorted(nums, key=lambda s: s['key', 'numeric'])
print(len(c))
print(list(c.keys()))
print(list(c.values()))

# 添加子元素,类似于
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
# 删除子元素
values = values.parents
print(values)
