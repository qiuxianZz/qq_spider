# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo05_ohe.py  独热编码
"""
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array(
    [[1, 3, 2], [7, 5, 4], [1, 8, 6], [7, 3, 9]])
print(raw_samples)
# 独热编码
ohe = sp.OneHotEncoder(sparse=True)
result = ohe.fit_transform(raw_samples)
print(result, type(result))
