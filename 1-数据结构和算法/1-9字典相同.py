# 字典的items和keys都是能够进行集合运算的
# values由于值的不确定性不能进行 集合运算，可以先将其转换成set再进行运算
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}
# 打印两字典相等的key
print(a.keys() & b.keys())
# 打印两字典不同的key
print(a.keys() - b.keys())
# 找相同
print(a.items() & b.items())
# 排除指定的键值对（可以注意表达式的样式）
c = {key: a[key] for key in a.keys() - {'z'}}
print(c)
