# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo09_lr.py  线性回归
"""
import numpy as np
import matplotlib.pyplot as mp

train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.5, 6.2, 7.0])

# 梯度下降求得回归线
times = 1000
lrate = 0.01  # 学习率
w0, w1 = [1], [1]
for i in range(1, times + 1):
    # 求w0方向上的偏导数
    d0 = (w0[-1] + w1[-1] * train_x - train_y).sum()
    # 求w1方向上的偏导数
    d1 = (train_x * (w0[-1] + w1[-1] *
                     train_x - train_y)).sum()
    w0.append(w0[-1] - lrate * d0)
    w1.append(w1[-1] - lrate * d1)

# 通过最优的w0与w1，求得所有样本x的预测输出y
pred_y = w0[-1] + w1[-1] * train_x

# 绘制样本点
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=16)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.grid(linestyle=':')
mp.scatter(train_x, train_y, marker='D', s=70,
           label='Samples', color='dodgerblue')
mp.plot(train_x, pred_y, color='orangered',
        label='Regression Line', linewidth=2)
mp.legend()
mp.show()
