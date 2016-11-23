# 反向迭代一个序列
"""
反向迭代只有在对象的大小确定或对象实现了__reversed__函数之后才能生效
如果2者都不满足就需要将对象先转换成列表（可能造成内存浪费）
使用reversed可以实现非类对象的反迭代
实现类对象的反迭代需要类实现了__reversed__函数
"""
a = [1, 2, 3, 4]
for c in reversed(a):
    print(c)
with open('somefile.txt', 'r') as f:
    for line in reversed(list(f)):
        print(line)


class Countdown(object):
    """docstring for ClassName"""

    def __init__(self, star):
        super(Countdown, self).__init__()
        self.star = star

    def __iter__(self):
        n = self.star
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.star:
            yield n
            n += 1
for rr in reversed(Countdown(5)):
    print(rr)
for rr in Countdown(5):
    print(rr)
