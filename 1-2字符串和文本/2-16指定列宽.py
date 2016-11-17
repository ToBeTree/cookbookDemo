# 将字符串以指定的列宽重新格式化
s = "Look into my eyes, look into my eyes, the eyes, the eyes, the eyes, not around the eyes, don't look around the eyes, look into my eyes, you're under."
import textwrap
print(textwrap.fill(s, 70))
print('-----------------')
print(textwrap.fill(s, 40))
print('-----------------')
print(textwrap.fill(s, 40, initial_indent='    '))
print('-----------------')
print(textwrap.fill(s, 40, subsequent_indent='    '))
# 需要输出自动匹配终端大小使用os.get_terminal_size
import os
print(os.get_terminal_size().columns)
