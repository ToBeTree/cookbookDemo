# 删除元素集合中的重复元素并保持相对顺序
# 序列值都是散列值（hashable），利用集合和生成器可以做到
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a = [1, 2, 3, 2, 4, 5, 6, 1, 2, 4, 5, 9]
for item in dedupe(a):
    print(item)
# 消除非hash数值（dict），需要关注方法的实现

# 不仅局限于列表，同时可作用于文件消除重复行
def dedupe(items, key=None):
    seen = set()
    for item in items:
        # 表达式：如果key不为空，将item传入lambda
        val = item if key is None else key(item)
        if val not in seen:
            yield item
        seen.add(val)
a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

for item in dedupe(a, key=lambda d: (d['x'], d['y'])):
    print(item)
print('------------------------------')
for item in dedupe(a, key=lambda d: d['x']):
    print(item)
