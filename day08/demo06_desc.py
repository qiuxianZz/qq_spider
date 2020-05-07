# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo06_desc.py  dataframe的描述性统计
"""
import pandas as pd
import numpy as np

# 创建DF
d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack',
                        'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}

df = pd.DataFrame(d)
print(df)
# 测试描述性统计函数
print('-' * 45)
print(df.sum())
print(df.sum(1))
print(df.mean())
print(df.mean(1))

# describe 描述性统计函数
print('-' * 45)
print(df.describe(include=['number']))
