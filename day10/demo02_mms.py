# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo02_mms.py   范围缩放
"""
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])

# 把没列数据 缩放到[0,1]区间
mms = sp.MinMaxScaler(feature_range=(0, 1))
r = mms.fit_transform(raw_samples)
print(r)

# 手动实现缩放功能
mms_samples = raw_samples.copy()
for col in mms_samples.T:
    col_min = col.min()
    col_max = col.max()
    # 整理A与B，求出k与b
    A = np.array([[col_min, 1], [col_max, 1]])
    B = np.array([0, 1])
    x = np.linalg.lstsq(A, B)[0]
    col *= x[0]
    col += x[1]
print(mms_samples)
