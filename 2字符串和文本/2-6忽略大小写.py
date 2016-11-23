# 需要忽略大小写的方式搜索/替换文本
import re
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
# 替换字符串不会自动匹配字符串大小
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))
# 自动匹配原字符串大小，需要构造回调函数

# 装饰器
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))
