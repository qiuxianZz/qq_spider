# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pandas as pd

left = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'student_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung', 'Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'class_id': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]})
right = pd.DataFrame(
    {'class_id': [1, 2, 3, 5],
     'class_name': ['ClassA', 'ClassB', 'ClassC', 'ClassE']})
print(left)
print("========================================")
print(right)
print("========================================")
# 合并两个DataFrame
rs = pd.merge(left, right, how='right')
print(rs)
