# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo05_dfattr.py  dataframe的常用属性
"""
import numpy as np
import pandas as pd

data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'],
        'Age': [28, 34, 29, 42]}
df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4'])
df['score'] = pd.Series(
    [90, 80, 70, 60], index=['s1', 's2', 's3', 's4'])

print(df)
print(df.axes)
print(df['Age'].dtype)
print(df.empty)
print(df.ndim)
print(df.size)
print(df.values)
print(df.head(3))  # df的前三行
print(df.tail(3))  # df的后三行
