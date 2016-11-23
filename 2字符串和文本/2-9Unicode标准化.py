# 确保所有字符串在底层有相同的表示
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
# 同样的文本采用不同的编码得到不同的结果
print(s1, s2, s1 == s2, len(s1), len(s2))
# 为了解决这个问题可以采用unicodedata将文本标准化
import unicodedata
# normalize将字符串按照指定的标准标准化
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
# 标准形式有：NFD、NFKC、NFKD
t1 = unicodedata.normalize('NFD', s1)
# combining函数测试一个字符是否为合音字符
# unicodedata还有其他类似的函数
print(''.join(c for c in t1 if not unicodedata.combining(c)))
