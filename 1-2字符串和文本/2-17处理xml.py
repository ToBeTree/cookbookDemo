# 你想将HTML或者XML实体如 &entity; 或 &#code; 换为对应的文本。
# 再者，你需要转换文本中特定的字符(比如<, >, 或 &)。
s = 'Elements are written as "<tag>text</tag>".'
import html
print(html.escape(s))
print(html.escape(s, quote=False))
# 使用解析器
from html.parser import HTMLParser
s = 'Spicy &quot;Jalape&#241;o&quot.'
p = HTMLParser()
print(p.unescape(s))
