class opera(object):
    def __init__(self):
        pass

    def add(self, l, r):
        return l + r

    def sub(self, l, r):
        return l - r

    def mul(self, l, r):
        return l * r

    def div(self, l, r):
        return l / r
s = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
symbol = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3, ')': 3}
Opera = opera()
print(s.find(')'))
print(s.split('-', 1))
