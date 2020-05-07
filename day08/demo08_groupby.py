# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo08_groupby.py  分组操作
"""
import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
                     'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
            'Rank': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
            'Year': [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
            'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690]}
df = pd.DataFrame(ipl_data)
print(df)

grouped = df.groupby('Year')
print(grouped)
print(grouped.groups)

# 遍历每个分组
for year, group in grouped:
    print(year)
    print(group)

print('-' * 45)
print(grouped.get_group(2014))


print('-' * 45)
# 聚合每一年的平均的分
print(grouped['Points'].agg(np.mean))
# 聚合每一年的分数之和、平均分、标准差
grouped = df.groupby('Year')
agg = grouped['Points'].agg([np.sum, np.mean, np.std])
print(agg)
