# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo10_pivot.py  透视表
"""
import pandas as pd
left = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'student_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung', 'Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'gender': ['M', 'M', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'class_id': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
    'age': [13, 14, 12, 12, 12, 13, 21, 22, 12, 12],
    'score': [98, 97, 97, 97, 89, 79, 99, 97, 97, 78]})
right = pd.DataFrame(
    {'class_id': [1, 2, 3, 5],
     'class_name': ['ClassA', 'ClassB', 'ClassC', 'ClassE']})
# 合并两个DataFrame
data = pd.merge(left, right)
print(data)

print('-' * 45)
print(data.pivot_table(index=['class_id', 'gender']))

print(data.pivot_table(
    index=['class_id', 'gender'], values=['score']))

# 以class_id与gender做分组汇总数据，聚合统计score列，针对age的每个值列级分组统计
print(data.pivot_table(index=['class_id', 'gender'],
                       values=['score'], columns=['age']))
