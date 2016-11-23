# 实现一个自定义的模式
# 一个生成器的主要特征是只回应next的操作
# 一个函数有yield就可以是生成器了
def frange(star, stop, step):
    n = star
    while n < stop:
        yield n
        n += step

for i in frange(1, 3, 0.5):
    print(i)
# 原生的range函数不支持浮点型step
# for i in range(1, 10, 0.5):
#     print(i)
