# 不使用for循环去遍历一个可迭代对象
# 为了手动的遍历可迭代对象，需要使用next函数去获取元素
# next函数会在对象末尾抛出StopIteration异常，需要捕获它


def mual_iter():
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    c = iter(a)
    # a = {'a': 1, 'b': 2}
    try:
        while True:
            b = next(c)
            print(b)
    except StopIteration:
        pass
mual_iter()
