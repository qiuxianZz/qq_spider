# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo07_sort.py 排序相关
"""
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(
    np.random.randn(10, 2),
    index=[1, 4, 6, 2, 3, 5, 9, 8, 0, 7],
    columns=['col2', 'col1'])
print(unsorted_df)

# 按照行标进行排序
sorted_df = unsorted_df.sort_index()
print(sorted_df)
# 控制排序顺序
sorted_df = unsorted_df.sort_index(ascending=False)
print(sorted_df)


# 排序
d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack',
                        'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}
unsorted_df = pd.DataFrame(d)

# 按照年龄进行排序
sorted_df = unsorted_df.sort_values(by='Age')
print(sorted_df)
sorted_df = unsorted_df.sort_values(
    by=['Age', 'Rating'], ascending=[True, False])
print(sorted_df)
