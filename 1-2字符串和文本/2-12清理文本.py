# 清理文本文件中的奇怪字符
# 在简单情况下可以使用str.upper/str.lower将字符转成标准格式
# str.replace/re.sub则可以删除/替换文本字符
# unicodedata.normalize则可以将Unicode文本标准化
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)
# 构建一个表格然后使用translate
remap={ord('\t'):' ',ord('\f'):' ',ord('\r'):None}
print(s.translate(remap))
# 以上面为基础构建一个更大的表格，删除所有和音符
import unicodedata
import sys
cmd_chrs=dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD',s.translate(remap))
print(b.translate(cmd_chrs))