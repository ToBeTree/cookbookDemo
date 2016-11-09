# 使用切片命名的方式可以硬编码切片所带来的冗余
# 切片命名可以使代码可读性提高
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])

SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])

item = [1, 2, 3, 4, 5, 6, 7, 8]
a = slice(2, 5)
print(item[a])
del item[a]
print(item)
# 打印slice
print(a.start, a.stop, a.step)

s = 'Helloword'
# 切片大小会被合理缩放以满边界需要
a.indices(len(s))
print(a)
