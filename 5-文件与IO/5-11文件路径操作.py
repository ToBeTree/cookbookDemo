# 你需要使用路径名来获取文件名，目录名，绝对路径等等
"""
使用os.path模块中的函数来操作文件名，使得编写的脚本跨系统运行
"""
import os
path = '/user/data/data.csv'
print(os.path.basename(path))
print(os.path.dirname(path))
path = '~/data/data.csv'
print(os.path.expanduser(path))
print(os.path.splitext(path))
