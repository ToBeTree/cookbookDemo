# 你想内存映射一个二进制文件到一个可变字节数组中，目的可能是为了随机访问它的内容或者是原地做些修改
"""
为了随机的访问文件的内容，使用mmap将文件映射到内存中是一个高效和优雅的方法
内容只有在被使用的到的时候才会被映射到内存中，mmap可以在多个解释器中同时读写数据
mmap模块 内存映射文件，无需打开一个大文件
"""
import mmap
import os


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)
size = 10000
with open('data', 'wb') as f:
    f.seek(size - 1)
    f.write(b'\x00')

m = memory_map('data')
print(len(m))
# m.close()
m[0:11] = b'Hello world'
with open('data', 'rb') as f:
    print(f.read(11))
