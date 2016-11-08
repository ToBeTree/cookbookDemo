# from heapq import nlargest, nsmallest #堆排序
# lambda is a funcation
# def f():
#     return lambda s: s[1]
# s = [1, 2, 3, 4, 5, 6, 7]
# print(f()(s))

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

print(heapq.nlargest(3, nums, key=None))  # sort by key
print(heapq.nsmallest(3, nums))

heapq.heapify(nums)
print(nums)  # heapq.heappop(nums) pop min in list

# 当查找唯一一个时，max、min方法是最好的
print(max(nums))
print(min(nums))

# 查找数量接近集合大小时，使用切片更便捷
# sorted(nums)[:N]
# sorted(nums)[-N:]
