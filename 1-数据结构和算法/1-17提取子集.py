# 从字典中提取子集，最简单便捷使用字典推导
# 用dict的方式也可以完成，速度慢很多
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)
tech_names = {'AAPL', 'ACME'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)
