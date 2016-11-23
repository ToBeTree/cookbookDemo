# 对齐字符串，格式化字符串
# 对于基本的字符串，使用ljust/rjust/center函数来格式化
text = 'hello world'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
# 这些方法都支持字符填充
print(text.ljust(20,'='))
print(text.rjust(20,'='))
print(text.center(20,'='))
# 函数format也可以用来对齐字符串
print(format(text,'<20'))
print(format(text,'>20'))
print(format(text,'^20'))
# format也支持字符填充
print(format(text,'=<20'))
print(format(text,'=>20'))
print(format(text,'=^20'))
# format是非常强大的，还支持数字的格式化不仅仅是字符串
print('{:=>10s} {:=>10}'.format('hellow','world'))
print('{}-{}-{}'.format('2016','11','17'))
print(format(1.22,'>10'))
