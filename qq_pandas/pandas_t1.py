#代码
#matplotlib库仅用于show()
import pandas as pd
import matplotlib.pyplot as plt
file='d_train_20180102.csv'
data=pd.read_csv(file,encoding='gbk')
tr_y = data.loc[:,'血糖']
print(type(tr_y))
#直方图
tr_y.hist(bins=500)
plt.show()
#直方图，xy轴相反
tr_y.plot()
plt.show()