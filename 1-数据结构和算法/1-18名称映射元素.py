# 使用collections.nametuple来避免使用下标的方式去访问元素

from collections import namedtuple

Subcriber = namedtuple('Subcriber', ['addr', 'joined'])
sub = Subcriber('***@qq.com', '2012-10')
print(sub)
# 命名元组的方式让你的代码意思更清晰
stock = namedtuple('Stock', ['name', 'share', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = stock(*rec)
        total += s.share * s.price
    return total
# 命名元组是不可更改的，但是通过_replace函数可以修改
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)


def dict_to_stock(s):
    return stock_prototype._replace(**s)
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
