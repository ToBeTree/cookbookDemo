# 你想将一个多层嵌套的序列展开成一个单层列表
"""
可以写一个包含yield from的递归生成器来完成
yield from会返回所有子例程的值
需要注意字符串和字节数据是可以迭代的
collections.Iterable和isinstance可以帮助判断
ignore_types=(str,byte)
"""
