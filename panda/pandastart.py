from pandas import Series, DataFrame
import pandas as pd
# Series是一种类似于一维数组的对象，它由一组数据以及一组与之相关的数据标签组成
# DataFrame
obj = Series([4, 7, -5, 2], index=['a', 'b', 'c', 'd'])
print(obj)
print(obj['d'])
obj.name = 'dic'
obj.index.name = 'en'
print(obj)
