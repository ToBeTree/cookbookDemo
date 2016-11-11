# 需要灵活使用生成器，避免内存消耗
s = {'name', 12, 11.11}
print(','.join(str(a) for a in s))
nums = [1, 2, 3, 6, 7]
# 生成器
s = sum(s * s for s in nums)
print(s)
# 下面的方式会生成一个临时的列表
s = sum([s * s for s in nums])
print(s)

# 命名元组不能修改但是_replace可以创建一个新的对象替代
from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'date', 'grade'])
s1 = Student('peter', '21', None, None)
s2 = Student('ali', '22', '0824', '10')
print(s1)
print(s2)
s1_c = s1._replace(name='wyq')
print('after change:', s1_c)
