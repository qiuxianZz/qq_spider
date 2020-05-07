# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo07_3dsurface.py   3d曲面图
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

# 整理数据
n = 1000
w0, w1 = np.meshgrid(np.linspace(-100, 100, n),
                     np.linspace(-100, 100, n))
# 计算损失函数
xs = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
ys = np.array([5.0, 5.5, 6.0, 6.8, 7.0])
loss = np.zeros_like(w0)
for x, y in zip(xs, ys):
    loss += (w0 + w1 * x - y)**2 / 2

# 绘制
mp.figure('3D Surface', facecolor='lightgray')
mp.title('3D Surface', fontsize=18)
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('w0', fontsize=14)
ax3d.set_ylabel('w1', fontsize=14)
ax3d.set_zlabel('loss', fontsize=14)
ax3d.plot_surface(
    w0, w1, loss, cmap='jet', rstride=30, cstride=30)
mp.tight_layout()
mp.show()
