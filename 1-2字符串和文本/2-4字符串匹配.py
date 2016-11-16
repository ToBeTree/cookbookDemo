# 匹配和搜索特殊文本
import re
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
if re.match(r'\d+/\d+/\d+', text1):
    print(True)
else:
    print(False)
# 使用一个模式去匹配多个文本
# 单次匹配可以不用使用compile
datepat = re.compile(r'\d+/\d+/\d+')
datepat.match(text1)
datepat.match(text2)
# match是从字符串开始进行匹配的，要想匹配任意位置的使用findall函数
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))
# 利用括号去捕获分组
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/16/2016')
print(m.groups())
print(m.group(1))
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))
# 也可以使用迭代的方式去返回所有匹配
for m in datepat.finditer(text):
    print(m.groups())
