# 匹配字符串中的指定文本
# 简单的方式可以直接使用str.replace()
# 复杂模式使用re.sub
import re
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# print(re.sub(r'\d+/\d+/\d+',r'\d-\d-\d',text))
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# 同样也可以使用compile提高重复使用率
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))
# subn函数则可以知道有多少数据发生了替换
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext, 'count:', n)
# 如果还需要更复杂的替换的，创建一个替换回调函数
from calendar import month_abbr

# 回调函数，参数必须是match对象
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
print(datepat.sub(change_date, text))
