# 去除字符串中的空白
s = ' hello word \n'
# strip函数可以做到这点，lstrip和rstrip分别从左和右执行删除操作
print(s.strip())
print(s.lstrip())
print(s.rstrip())
# 默认情况下strip函数会去掉空白字符，但你也可以指定去除的字符
t = '-----hello======'
print(t.strip('-'))
print(t.strip('-='))
# 去除操作不会影响中间字符
# 要去除中间字符需要借助其他技术
s = 'hello  ,  word'
print(s.replace(' ', ''))
import re
print(re.sub('\s', '', s))
# 去除文本文件中的空白字符
# whit open(filename) as f:
#     # 生成器
#     lines = (line.strip() for line in f)
#     for line in lines:
#         print(line)
