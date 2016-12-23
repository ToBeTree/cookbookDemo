# 使用Unix Shell匹配文本字符串
# fnmatch是大小写敏感的，但是win下是不敏感的
# fnmatchcase无论何种os都是大小写敏感
from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('Dat9.csv', 'Dat[0-9].csv'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat[0-9].csv')])

print(fnmatch('re.txt', '*.TXT'))
print(fnmatchcase('re.txt', '*.TXT'))

from collections import deque
# deque
import optparse
parse = optparse.OptionParser()
parse.add_option()
parse.add_options()

