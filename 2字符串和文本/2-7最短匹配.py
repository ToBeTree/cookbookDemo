# 按照最短模式匹配文本
import re
str_pat = re.compile(r'"(.*)"')
print(str_pat.findall('computer say "no." Phone say "yes."'))
str_pat_2 = re.compile(r'"(.*?)"')
print(str_pat_2.findall('computer say "no." Phone say "yes."'))
print('aa.jpg'.split('.')[0])
