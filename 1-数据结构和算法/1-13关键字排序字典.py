# 使用operator.itemgetter函数可很容易实现
# 以下所有方法同时适用于min()、max()等带key的函数
from operator import itemgetter
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
a = sorted(rows, key=itemgetter('fname'))
print(a)
# 还支持多个key
b = sorted(rows, key=itemgetter('lname', 'fname'))
print(b)

# sorted方法中的key值可以使用lambda函数代替
c = sorted(rows, key=lambda s: s['fname'])
print(c)
d = sorted(rows, key=lambda s: (s['lname'], s['fname']))
print(d)
# 验证结果
print(a == c)
print(b == d)
