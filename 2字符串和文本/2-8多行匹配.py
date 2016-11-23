# 使用正则表达式去匹配一大块文本，涉及到多行匹配
import re
text1 = '/* this is a comment */'
text2 = '''/* this is a
multiline comment */
'''
comment = re.compile(r'/\*(.*?)\*/')
print(comment.findall(text1))
print(comment.findall(text2))
# 由于.号不能匹配换行符所以我们需要自己添加
comment_1 = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment_1.findall(text2))
# 或者re.DOTALL可以做到
# 它让.可以匹配任意字符
comment_2 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment_2.findall(text2))
# print(1 - 2 * ((60 - 30 + (-40 / 5) * (9 - 2 * 5 / 3 + 7 / 3 *
#                                        99 / 4 * 2998 + 10 * 568 / 14)) - (-4 * 3) / (16 - 3 * 2)))
