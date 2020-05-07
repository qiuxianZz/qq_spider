# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo04_bin.py   二值化
"""
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])

bin = sp.Binarizer(threshold=80)
r = bin.transform(raw_samples)
print(r)

raw_samples[raw_samples <= 80] = 0
raw_samples[raw_samples > 80] = 1
print(raw_samples)
