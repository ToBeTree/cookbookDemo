# 你在代码中使用 while 循环来迭代处理数据，因为它需要调用某个函数或者和一般迭代模式不同的测试条件。 能不能用迭代器来重写这个循环呢
"""
iter函数接收一个可选的callable对象和一个标记值作为输入参数
当以这种方式使用的时候，它会创建一个迭代器
这个迭代器会不断调用callable对象直到返回值和标记值相等为止
"""
with open('somefile.txt', 'r+') as f:
    # r = f.readlines()
    # print(f.readlines())
    for line in iter(lambda: f.readline().strip('\n'), ''):
        print(line)
    print('aa', file=f)
