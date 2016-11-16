# 1-1 解压序列赋值给多个变量
a, b, c, d = [1, 2, 3, 4]
# 1-2 解压可迭代对象赋值给多个变量
a, *b, c, d = [1, 2, 3, 4, 5, 6, 7, 8]
# 1-3 保留最后N个元素
from collections import deque
history = deque(maxlen=3)
# 1-4 查找最大或最小的N个元素
from heapq import nlargest, nsmallest
nlargest(3, [1, 2, 4, 6, 7, 2, 4])
nsmallest(3, [1, 2, 4, 5, 6, 1, 2], key=lambda s: s)
# 1-5 实现一个优先级队列
from heapq import heappop, heappush
que = []
i = 1
heappush(que, (-i, -1, 'a'))
heappop(que)[-1]
# 1-6 字典中的键映射多个值
from collections import defaultdict
dic = defaultdict()
dic['a'] = 1
# 1-7 字典排序
from collections import OrderedDict
dic_o = OrderedDict()
# 1-8 字典的运算
sorted(zip(dic.values(), dic.keys()))
# 1-9 查找两字典的相同点
dic_1 = {}
dic_2 = {}
dic_1.keys() & dic_2.keys()
# 1-10 删除序列相同元素并保持顺序


def de(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
# 1-11 命名切片
name_slice = slice(1, 10, 2)
# 1-12 序列中出现次数最多的元素
from collections import Counter
word = []
word_count = Counter(word)
word_count.most_common(1)
# 1-13 通过某个关键字排序一个字典列表
from operator import itemgetter
dic = [{'a': 1, 'b': 2}, {'a': 2, 'b': 2}]
sorted(dic, key=itemgetter('a'))
# 1-14 排序不支持原生比较的对象
from operator import attrgetter
# class s():
#     pass
# sorted(S, key=attrgetter(''))
# 1-15 通过某个字段将记录分组
from itertools import groupby
dic = [{'name': 1}, {'name': 2}, {'name': 2}, ]
groupby(dic, key=lambda s: s['name'])
# 1-16 过滤序列元素
mylist = [1, 2, 4, -1, 4, -5, 1, 5]
(n for n in mylist if n < 0)
# 1-17 从字典中提取子集
mylist_1 = {n for n in mylist if n > 0}
# 1-18 映射名称到序列元素
from collections import namedtuple
Stock = namedtuple('stock', ('name', 'age'))
stock = Stock('peter', 18)
# 1-19 转换并同时计算数据
mylist_1 = sum(n * n for n in mylist if n > 0)
# 1-20 合并多个字典或映射
from collections import ChainMap
dic_2 = {'a': 4}
dic_c = ChainMap(dic_1, dic_2)
