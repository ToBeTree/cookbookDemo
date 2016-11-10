# 根据特定字段对字典分组
# groupby函数查找连续相同的值并返回一个值和一个迭代器对象
# 由于groupby函数只查找检查连续的元素，所以要对序列先排序
from operator import itemgetter
from itertools import groupby
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
rows_1 = rows
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for item in items:
        print(' ', item)
# 如果只是想访问数据，并且对内存不是很关心的话使用defaultDict
print('---------------------')
from collections import defaultdict
d = defaultdict(list)
for row in rows:
    d[row['date']].append(row)
for r in d['07/01/2012']:
    print(r)
