# 你想定义一个生成器函数，但是它会调用某个你想暴露给用户使用的外部状态值。
"""
可以将生成器放在类中的__iter__函数中实现
在__iter__函数中实现生成器
你可以通过访问类的属性来改变迭代对象的值
"""


class Countdown(object):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        for i in range(0, self.value):
            yield i

    def change_value(self, value):
        self.value = value

count = Countdown(6)
for i in count:
    print(i)
count.change_value(3)
for i in count:
    print(i)
