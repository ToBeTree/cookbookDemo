# 利用collections.Counter可以很便捷的得到一个序列中元素出现次数的前n位
# 你也可以选择手动计数，将元素作为key来统计次数也是个可行的方法
# collections.Counter返回的是一个列表对象，这意味着它的返回值是可以进行集合（数学）运算的
from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

a = Counter(words)
print(a.most_common(3)) # 打印出出现次数前三的元素
# a.update(words)

