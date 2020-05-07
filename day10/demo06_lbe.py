# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo06_lbe.py  标签编码
"""
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array(
    ['audi', 'ford', 'audi', 'toyota',
     'ford', 'bmw', 'toyota', 'ford',
     'audi'])
lbe = sp.LabelEncoder()
result = lbe.fit_transform(raw_samples)
print(result)

r = lbe.inverse_transform(
    [0, 1, 1, 2, 2, 0, 1, 0])
print(r)
