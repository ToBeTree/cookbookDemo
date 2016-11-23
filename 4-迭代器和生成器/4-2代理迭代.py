# 构建的自定义容器对象，里面包含数组、列表或可迭代对象
# 在这个对象迭代，只需要定义__iter__函数，将迭代操作代理到容器内部对象上去


class Node(object):
    """docstring for Node"""

    def __init__(self, value):
        super(Node, self).__init__()
        self._value = value
        self._children = []

    def add_child(self, node):
        self._children.append(node)

    def __repr__(self):
        return 'Node({})'.format(self._value)

    def __iter__(self):
        return iter(self._children)
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)
# iter(s)等价于s.__iter__()