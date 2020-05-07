# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo02_series.py   测试pandas的series对象
"""
import pandas as pd
import numpy as np

data = np.array(['Tom', 'Lily', 'Jerry', 'Lilei'])
s = pd.Series(data)
print(s)
s = pd.Series(data, index=[10, 20, 30, 40])
print(s)
# 访问Series中的元素
print(s[10])

# 通过字段创建Series对象
print('-' * 45)
data = {'a': 0, 'b': 1, 'c': 2}
s = pd.Series(data)
print(s + 1, s['a'])

# 通过标量创建Series对象
print('-' * 45)
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)

# 访问Series中的元素
s = pd.Series([75, 33, 59, 60, 90],
              index=['a', 'b', 'c', 'd', 'e'])
# 访问下标为0的元素，  访问index为'a'的元素
print(s[0], s['a'])
print(s[:3])


# pandas识别的日期字符串格式
print('-' * 45)
dates = pd.Series(
    ['2011', '2011-02', '2011-03-01',
     '2011/04/01', '2011/05/01 01:01:01',
     '01 Jun 2011'])
print(dates)
dates = pd.to_datetime(dates)
print(dates)

# 日期运算
delta = dates - pd.to_datetime('1970-01-01')
print(delta, type(delta))

# 通过Series的dt接口 访问 偏移量数据
print(delta.dt.days)
print(dates.dt.month)

