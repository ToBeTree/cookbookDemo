# str.split函数只能分割相当规则字符串
import re
line = 'a,b,c,d,e'
print(line.split(','))
# 正则表达式的split函数
# 正则表达式不能老是忘啊
line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line))
# 小括号会保留分割字符串
print(re.split(r'(;|,|\s)\s*', line))
# (?:...)不会保留分割字符串
print(re.split(r'(?:;|,|\s)\s*', line))
