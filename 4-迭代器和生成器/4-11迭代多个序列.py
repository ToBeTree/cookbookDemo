# 你想同时迭代多个序列，每次分别从一个序列中取一个元素。
"""
zip函数可以做到，zip从两个序列中分别取出一个元素组成元组
zip返回的是一个元组的迭代器对象，zip按照最短序列输入
itertools.zip_longest函数是按照最长序列输出，None代替
"""
a = [1, 2, 3, 4, 5]
b = {'a', 'b', 'c', 'd'}
for i in zip(a, b):
    print(i)
print('------------------')
from itertools import zip_longest
for i in zip_longest(a, b):
    print(i)
