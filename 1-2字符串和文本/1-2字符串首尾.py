# 检查文件开头/结尾，使用str.starstwith和str.endswith
filename = 'span.txt'
print(filename.startswith('file:'))
print(filename.endswith('.txt'))
# 匹配多组数据时，需要将规则放入一个元组（tuple)中
import os
listfile = os.listdir('../')
print([name for name in listfile if name.endswith(('.py', '.md'))])
