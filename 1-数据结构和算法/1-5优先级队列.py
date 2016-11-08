import heapq


class PriorityQueue:
    """使用堆实现的优先级队列"""

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 下面括号里面的东西搞不懂什么意思
        # A：这里第二个参数使用到了元组tuple
        # 存入元组，多个参数便于比较
        # 标负，为了区别堆排序从低到高
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]  # 输出元组的最后一个
q = PriorityQueue()
q.push('haha', 1)
q.push('hehe', 2)
q.push('gaga', 5)
q.push('aaaa', 1)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

print((1, 2, 'haha') < (2, 2, 'gaga'))
