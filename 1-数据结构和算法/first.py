print('read cookbook-python agin')


class clazz():
    def __init__(self):
        print('clazz init...')
        self.arg1 = 1
        self.__arg2 = 2
c = clazz()
print(c.arg1)
c.arg1 = 2
print(c.arg1)
