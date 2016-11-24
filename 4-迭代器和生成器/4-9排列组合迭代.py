# 你想迭代遍历一个集合中元素的所有可能的排列或组合
"""
itertools模块提供三个方法来解决这个问题
itertools.permutations排列
itertools.combinations组合
itertools.combinations_with_replacement元素重复选择
"""
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

a = ['a', 'b', 'c']
for i in permutations(a, 2):
    print(i)
print('--------------------')
'''参数r是int型'''
for i in combinations(a, 2):
    print(i)
print('--------------------')
for i in combinations_with_replacement(a, 2):
    print(i)
