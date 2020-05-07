# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo03_dtindex.py  日期序列
"""
import pandas as pd
import numpy as np

dates = pd.date_range('2019-08-20', periods=5)
print(dates)

dates = pd.date_range(
    '2019-08-20', periods=5, freq='M')
print(dates)

start = pd.datetime(2019, 8, 1)
end = pd.to_datetime('2019/08/30')
dates = pd.date_range(start, end)
print(dates)
print(pd.Series(dates).dt.day)

# bdate_range()
dates = pd.bdate_range('2019/08/01', periods=7)
print(dates)
