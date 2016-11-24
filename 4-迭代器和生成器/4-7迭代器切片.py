# 你想得到一个由迭代器生成的切片对象，但是标准切片操作并不能做到。
"""
itertools.islice
迭代器不可逆
"""
from itertools import islice
a = [-1, -2, -3, 1, 2, 3, 4, 5, 6, 7, 8]
for c in islice(a, 2, 4):
    print(c)
"""
由于迭代器迭代过程是不可逆
如果需要重新访问它需要先将它放入列表中
"""
