# 删除序列中的重复元素可以使用opreator.itemgetter方法
# 也可以使用key = lambda的方式
# 类似的在类关键字排序中同样使用上述方法
# 带key参数的函数很多又可以这么使用（lambda）
# 模块函数的运行速度会快一点
from operator import attrgetter


class clazz(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'clazz({})'.format(self.user_id)


def sort_by_user_id():
    users = [clazz(1), clazz(19), clazz(9)]
    print(users)
    print(sorted(users, key=lambda s: s.user_id))
    print(users)
    print(sorted(users, key=attrgetter('user_id')))
sort_by_user_id()
