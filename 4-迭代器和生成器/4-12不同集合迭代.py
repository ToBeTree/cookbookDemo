# 你想在多个对象执行相同的操作，但是这些对象在不同的容器中，你希望代码在不失可读性的情况下避免写重复的循环。
"""
chain函数为多个对象执行相同的操作
chain将多个对象在逻辑上链接在一起
chainMap将多个字典对象在逻辑上连接在一起
"""
from itertools import chain
a = ['a', 'b', 'c']
b = {1, 2, 3, 4, 5}
for i in chain(a, b):
    print(i)
'''+需要同类型的数据'''
# for i in a + b:
#     print(i)
