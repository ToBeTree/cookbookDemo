# 利用数据规则提取需要的值
# 最简单的办法就是列表推导，内存占用较大
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])
# print([n if n < 0 for n in mylist])
# print([n for n in mylist if n > 0 else 0])
# 在推导过程中转换数据
print([n if n > 0 else 0 for n in mylist])
# 生成器推导，内存占用较少（不会直接返回大量的结果）
pos = (n for n in mylist if n > 0)
print(pos)
for x in pos:
    print(x)
# 过滤复杂时，使用filter函数
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

# filter函数过滤数据根据构建函数的返回值true/false


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
# filter返回的是迭代器对象
print(list(filter(is_int, values)))
# 使用itertools.compress过滤
# itertools.compress和filter类似都是返回迭代器对象
# 不同之处在于判定条件的传入（函数和序列）
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 = [n > 5 for n in counts]
print(list(compress(addresses, more5)))
