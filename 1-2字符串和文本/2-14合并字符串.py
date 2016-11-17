# 将几个小的字符串合并成一个大的字符串
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
# 如果你想合成的字符串是在一个序列或iterable中，最快的方式 就是使用join函数
print(' '.join(parts))
print(','.join(parts))
# 尽量不要使用+来连接字符串，这会造成大量的资源浪费
a = 'hello' 'world'
print(a)
print('haha', 'hehe', 'gaga', sep='--')
# 最好先收集所有的字符片段再进行连接操作
data = ['ACME', 50, 91.1]
print(','.join(str(c) for c in data))
# 结合I/O操作的混合方案


def sample():
    yield 'Is'
    yield 'Not'


def combine(source, maxsize):
    parts = []
    size = 0
    for p in source:
        parts.append(p)
        size += len(p)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
        yield ''.join(parts)
with open('filename', 'w') as f:
    for part in combine(sample(), 32768):
        f.write(part)
