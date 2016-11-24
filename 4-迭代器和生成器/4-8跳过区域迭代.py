# 你想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们。
"""
itertools.dropwhile
itertools.islice
dropwhile需要一个可调用对象（lambda）
不想遍历的开头部分可以直接跳过
迭代过程不可逆，所以islice也可以做到
"""
from itertools import dropwhile
a = [-1, -2, -3, 0, 1, 2, 3, 4]
for i in dropwhile(lambda s: s < 0, a):
    print(i)

from itertools import islice
for i in islice(a, 4, None):
    print(i)
