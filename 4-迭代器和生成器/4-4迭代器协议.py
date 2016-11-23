# 构建一个自定义迭代操作的对象 ，并实现迭代协议
"""
Python的迭代协议要求__iter__需要返回一个特殊的迭代器对象
这个对象需要实现__next__函数并且使用StopIteration来标志迭代的完成
有一个比较简单的实现方式是将迭代器装换成生成器
"""


class Node():
    def __init__(self, value):
        self._children = []
        self._value = value

    def add_child(self, node):
        self._children.append(node)

    def __repr__(self):
        return 'Node({})'.format(self._value)

    def __iter__(self):
        return iter(self._children)

    def depth_first_iter(self):
        yield self
        # yield from self.depth_first_iter()
        '''需要调用具体的对象的函数'''
        for c in self:
            '''yield from 返回对应元素'''
            yield from c.depth_first_iter()

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    child11 = Node(3)
    child12 = Node(4)
    child21 = Node(5)
    child22 = Node(6)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(child11)
    child1.add_child(child12)
    child2.add_child(child21)
    child2.add_child(child22)
    for ch in root.depth_first_iter():
        print(ch)
