# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo04_df.py  DataFrame对象
"""
import pandas as pd
import numpy as np

data = [['Alex', 10], ['Tom', 12], ['Jerry', 13]]
# 通过二维数组创建DataFrame对象
df = pd.DataFrame(data)
print(df)

# 指定columns: 列名
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)
print(df.dtypes)  # 访问元素数据类型

# 指定dtype: 元素类型
df = pd.DataFrame(
    data, columns=['Name', 'Age'], dtype=float)
print(df)
print(df.dtypes)  # 访问元素数据类型

# 通过字典的方式创建DataFrame对象
# 字典的key表示列名， value表示当列值的列表
data = {'Name': ['Tom', 'Jerry', 'Bob'],
        'Age': [12, 13, 14]}
df = pd.DataFrame(data)
print(df)

# 构建DataFrame对象的同时指定行标（index）
df = pd.DataFrame(data, index=['A', 'B', 'C'])
print(df)
df = pd.DataFrame(
    data, index=pd.date_range(
        '2019-01-01', periods=3))
print(df)

# 其他情况   （每个字段一行记录）
data = [{'a': 1, 'b': 2},
        {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
