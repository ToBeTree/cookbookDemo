# 你想在迭代一个序列的同时跟踪正在被处理的元素索引
"""
使用内置函数enumerate
enumerate函数返回索引值和值的元组
"""
a = ['a', 'b', 'c', 'd']
for i, value in enumerate(a):
    print(i, value)
print('--------设置下标开始-------')
for i, value in enumerate(a, 3):
    print(i, value)
