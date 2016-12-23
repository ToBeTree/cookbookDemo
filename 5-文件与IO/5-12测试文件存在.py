#　你想测试一个文件或目录是否存在
"""
同样对于文件名的操作使用os.path来进行
os.path提供了很多对于文件名的操作函数
对于文件路径加上非转义字符串标识
"""
path = '/user/data/data/csv'
import os
print(os.path.exists(path))
path_1 = r'E:\\sub_extensions\\5-文件与IO'
print(os.path.isfile(r'E:\\sub_extensions\\5-文件与IO\\5-10内存映射文件.py'))
print(os.path.isdir(path_1))
print(os.path.isabs(path_1))
print(os.path.getmtime(path_1))
print(os.path.getctime(path_1))
import time
print(time.ctime(os.path.getmtime(path_1)))
print(time.ctime(os.path.getctime(path_1)))
