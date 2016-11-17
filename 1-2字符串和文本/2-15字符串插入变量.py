# 创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉
# 可以通过format函数来解决这个问题
s = '{name} has {n} message'
print(s.format(name='peter', n=3))
# 如果变量域能 找到变量，使用format_map和var
# 同时var还支持类var(classInstance)
name = 'peter'
n = 4
print(s.format_map(vars()))
# print('%(name) has %(n) messages.' % vars())
# 为了处理变量缺失的问题，定义一个含有__missing__的字典对象


class safesub(dict):
    """防止key找不到"""

    def __missing__(self, key):
        return '{' + key + '}'
del n
print(s.format_map(safesub(vars())))
# 如果经常执行这些操作可以使用工具函数封装起来
import sys


def sub(text):
    # 获取调用者的栈帧，f_locals获取本地变量
    return text.format_map(safesub(sys._getframe(1).f_locals))
name = 'Guido'
n = 33
print(sub('Hello {name}'))
print(sub('you have {n} m'))
print(sub('love {color}'))
