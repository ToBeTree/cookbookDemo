# 寻找字典中的最大最小值

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# 在字典上执行普通的数学运算，仅仅作用于键（第一个参数）
p = sorted(prices)
print(p)
# zip的作用是将参数位置反转，返回的数据是一次性迭代的元组类型
c = zip(prices.values(), prices.keys())
for key in c:
    print(key)

