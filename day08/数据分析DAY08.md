# 数据分析DAY08

### 图像

scipy.ndimage中提供了一些简单的图像处理，如高斯模糊、任意角度旋转、边缘识别等功能。

```python
import numpy as np
import scipy.misc as sm
import scipy.ndimage as sn
import matplotlib.pyplot as mp
#读取文件
original = sm.imread('../../data/head.jpg', True)
#高斯模糊
median = sn.median_filter(original, 21)
#角度旋转
rotate = sn.rotate(original, 45)
#边缘识别
prewitt = sn.prewitt(original)
mp.figure('Image', facecolor='lightgray')
mp.subplot(221)
mp.title('Original', fontsize=16)
mp.axis('off')
mp.imshow(original, cmap='gray')
mp.subplot(222)
mp.title('Median', fontsize=16)
mp.axis('off')
mp.imshow(median, cmap='gray')
mp.subplot(223)
mp.title('Rotate', fontsize=16)
mp.axis('off')
mp.imshow(rotate, cmap='gray')
mp.subplot(224)
mp.title('Prewitt', fontsize=16)
mp.axis('off')
mp.imshow(prewitt, cmap='gray')
mp.tight_layout()
mp.show()
```

### 金融相关

```python
import numpy as np
# 终值 = np.fv(利率, 期数, 每期支付, 现值)
# 将1000元以1%的年利率存入银行5年，每年加存100元，
# 到期后本息合计多少钱？
fv = np.fv(0.01, 5, -100, -1000)
print(round(fv, 2))
# 现值 = np.pv(利率, 期数, 每期支付, 终值)
# 将多少钱以1%的年利率存入银行5年，每年加存100元，
# 到期后本息合计fv元？
pv = np.pv(0.01, 5, -100, fv)
print(pv)
# 净现值 = np.npv(利率, 现金流)
# 将1000元以1%的年利率存入银行5年，每年加存100元，
# 相当于一次性存入多少钱？
npv = np.npv(0.01, [
    -1000, -100, -100, -100, -100, -100])
print(round(npv, 2))
fv = np.fv(0.01, 5, 0, npv)
print(round(fv, 2))
# 内部收益率 = np.irr(现金流)
# 将1000元存入银行5年，以后逐年提现100元、200元、
# 300元、400元、500元，银行利率达到多少，可在最后
# 一次提现后偿清全部本息，即净现值为0元？
irr = np.irr([-1000, 100, 200, 300, 400, 500])
print(round(irr, 2))
npv = np.npv(irr, [-1000, 100, 200, 300, 400, 500])
print(npv)
# 每期支付 = np.pmt(利率, 期数, 现值)
# 以1%的年利率从银行贷款1000元，分5年还清，
# 平均每年还多少钱？
pmt = np.pmt(0.01, 5, 1000)
print(round(pmt, 2))
# 期数 = np.nper(利率, 每期支付, 现值)
# 以1%的年利率从银行贷款1000元，平均每年还pmt元，
# 多少年还清？
nper = np.nper(0.01, pmt, 1000)
print(int(nper))
# 利率 = np.rate(期数, 每期支付, 现值, 终值)
# 从银行贷款1000元，平均每年还pmt元，nper年还清，
# 年利率多少？
rate = np.rate(nper, pmt, 1000, 0)
print(round(rate, 2))
```

## pandas基础

### pandas介绍

Python Data Analysis Library

pandas是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。Pandas 纳入 了大量库和一些标准的数据模型，提供了高效地操作大型结构化数据集所需的工具。

### pandas核心数据结构

数据结构是计算机存储、组织数据的方式。 通常情况下，精心选择的数据结构可以带来更高的运行或者存储效率。数据结构往往同高效的检索算法和索引技术有关。

#### Series

Series可以理解为一个一维的数组，只是index名称可以自己改动。类似于定长的有序字典，有Index和 value。

```python
import pandas as pd

# 创建一个空的系列
s = pd.Series()
# 从ndarray创建一个系列
data = np.array(['a','b','c','d'])
s = pd.Series(data)
s = pd.Series(data,index=[100,101,102,103])
# 从字典创建一个系列	
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
# 从标量创建一个系列
s = pd.Series(5, index=[0, 1, 2, 3])
```

访问Series中的数据：

```python
# 使用索引检索元素
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s[0], s[:3], s[-3:])
# 使用标签检索数据
print(s['a'], s[['a','c','d']])
```

**pandas日期处理**

```python
# pandas识别的日期字符串格式
dates = pd.Series(['2011', '2011-02', '2011-03-01', '2011/04/01', '2011/05/01 01:01:01', '01 Jun 2011'])
# to_datetime() 转换日期数据类型
dates = pd.to_datetime(dates)
print(dates, dates.dtype, type(dates))
# datetime类型数据支持日期运算
delta = dates - pd.to_datetime('1970-01-01')
# 获取天数数值
print(delta.dt.days)
```

Series.dt提供了很多日期相关操作，如下：

```python
Series.dt.year	The year of the datetime.
Series.dt.month	The month as January=1, December=12.
Series.dt.day	The days of the datetime.
Series.dt.hour	The hours of the datetime.
Series.dt.minute	The minutes of the datetime.
Series.dt.second	The seconds of the datetime.
Series.dt.microsecond	The microseconds of the datetime.
Series.dt.week	The week ordinal of the year.
Series.dt.weekofyear	The week ordinal of the year.
Series.dt.dayofweek	The day of the week with Monday=0, Sunday=6.
Series.dt.weekday	The day of the week with Monday=0, Sunday=6.
Series.dt.dayofyear	The ordinal day of the year.
Series.dt.quarter	The quarter of the date.
Series.dt.is_month_start	Indicates whether the date is the first day of the month.
Series.dt.is_month_end	Indicates whether the date is the last day of the month.
Series.dt.is_quarter_start	Indicator for whether the date is the first day of a quarter.
Series.dt.is_quarter_end	Indicator for whether the date is the last day of a quarter.
Series.dt.is_year_start	Indicate whether the date is the first day of a year.
Series.dt.is_year_end	Indicate whether the date is the last day of the year.
Series.dt.is_leap_year	Boolean indicator if the date belongs to a leap year.
Series.dt.days_in_month	The number of days in the month.
```



#### DateTimeIndex

通过指定周期和频率，使用`date_range()`函数就可以创建日期序列。 默认情况下，范围的频率是天。

```python
import pandas as pd
# 以日为频率
datelist = pd.date_range('2019/08/21', periods=5)
print(datelist)
# 以月为频率
datelist = pd.date_range('2019/08/21', periods=5,freq='M')
print(datelist)
# 构建某个区间的时间序列
start = pd.datetime(2017, 11, 1)
end = pd.datetime(2017, 11, 5)
dates = pd.date_range(start, end)
print(dates)
```

`bdate_range()`用来表示商业日期范围，不同于`date_range()`，它不包括星期六和星期天。

```python
import pandas as pd
datelist = pd.bdate_range('2011/11/03', periods=5)
print(datelist)
```

#### DataFrame

DataFrame是一个类似于表格的数据类型，可以理解为一个二维数组，索引有两个维度，可更改。DataFrame具有以下特点：

- 列可以是不同的类型
- 大小可变
- 标记轴(行和列)
- 可以对行和列执行算术运算

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo04_df.py  DataFrame对象
"""
import pandas as pd
import numpy as np

data = [['Alex', 10], ['Tom', 12], ['Jerry', 13]]
# 通过二维数组创建DataFrame对象
df = pd.DataFrame(data)
print(df)

# 指定columns: 列名
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)
print(df.dtypes)  # 访问元素数据类型

# 指定dtype: 元素类型
df = pd.DataFrame(
    data, columns=['Name', 'Age'], dtype=float)
print(df)
print(df.dtypes)  # 访问元素数据类型

# 通过字典的方式创建DataFrame对象
# 字典的key表示列名， value表示当列值的列表
data = {'Name': ['Tom', 'Jerry', 'Bob'],
        'Age': [12, 13, 14]}
df = pd.DataFrame(data)
print(df)

# 构建DataFrame对象的同时指定行标（index）
df = pd.DataFrame(data, index=['A', 'B', 'C'])
print(df)
df = pd.DataFrame(
    data, index=pd.date_range(
        '2019-01-01', periods=3))
print(df)

# 其他情况   （每个字段一行记录）
data = [{'a': 1, 'b': 2},
        {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)

# 从字典来创建DataFrame
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['s1','s2','s3','s4'])
print(df)
data = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(data)
print(df)
```

#### 核心数据结构操作

**列访问**

DataFrame的单列数据为一个Series。根据DataFrame的定义可以 知晓DataFrame是一个带有标签的二维数组，每个标签相当每一列的列名。

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df['one'])
print(df[['one', 'two']])
```

**列添加**

DataFrame添加一列的方法非常简单，只需要新建一个列索引。并对该索引下的数据进行赋值操作即可。

```python
import pandas as pd

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['s1','s2','s3','s4'])
df['score']=pd.Series([90, 80, 70, 60], index=['s1','s2','s3','s4'])
print(df)
```

**列删除** 

删除某列数据需要用到pandas提供的方法pop，pop方法的用法如下：

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
     'three' : pd.Series([10, 20, 30], index=['a', 'b', 'c'])}
df = pd.DataFrame(d)
print("dataframe is:")
print(df)

# 删除一列： one
del(df['one'])
print(df)

#调用pop方法删除一列
df.pop('two')
print(df)
```

**行访问**

如果只是需要访问DataFrame某几行数据的实现方式则采用数组的选取方式，使用 ":" 即可：

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df[2:4])

```

**loc**方法是针对DataFrame索引名称的切片方法。loc方法使用方法如下：

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df.loc['b'])
print(df.loc[['a', 'b']])
```

**iloc**和loc区别是iloc接收的必须是行索引和列索引的位置。iloc方法的使用方法如下：

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df.iloc[2])
print(df.iloc[[2, 3]])
```

**行添加**

```python
import pandas as pd

df = pd.DataFrame([['zs', 12], ['ls', 4]], columns = ['Name','Age'])
df2 = pd.DataFrame([['ww', 16], ['zl', 8]], columns = ['Name','Age'])

df = df.append(df2)
print(df)
```

**行删除**

使用索引标签从DataFrame中删除或删除行。 如果标签重复，则会删除多行。

```python
import pandas as pd

df = pd.DataFrame([['zs', 12], ['ls', 4]], columns = ['Name','Age'])
df2 = pd.DataFrame([['ww', 16], ['zl', 8]], columns = ['Name','Age'])
df = df.append(df2)
# 删除index为0的行
df = df.drop(0)
print(df)
```

**修改DataFrame中的数据**

更改DataFrame中的数据，原理是将这部分数据提取出来，重新赋值为新的数据。

```python
import pandas as pd

df = pd.DataFrame([['zs', 12], ['ls', 4]], columns = ['Name','Age'])
df2 = pd.DataFrame([['ww', 16], ['zl', 8]], columns = ['Name','Age'])
df = df.append(df2)
df['Name'][0] = 'Tom'
print(df)

```

**DataFrame常用属性**

| 编号 | 属性或方法 | 描述                                |
| ---- | ---------- | ----------------------------------- |
| 1    | `axes`     | 返回 行/列 标签（index）列表。      |
| 2    | `dtype`    | 返回对象的数据类型(`dtype`)。       |
| 3    | `empty`    | 如果系列为空，则返回`True`。        |
| 4    | `ndim`     | 返回底层数据的维数，默认定义：`1`。 |
| 5    | `size`     | 返回基础数据中的元素数。            |
| 6    | `values`   | 将系列作为`ndarray`返回。           |
| 7    | `head()`   | 返回前`n`行。                       |
| 8    | `tail()`   | 返回最后`n`行。                     |

实例代码：

```python
import pandas as pd

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['s1','s2','s3','s4'])
df['score']=pd.Series([90, 80, 70, 60], index=['s1','s2','s3','s4'])
print(df)
print(df.axes)
print(df['Age'].dtype)
print(df.empty)
print(df.ndim)
print(df.size)
print(df.values)
print(df.head(3)) # df的前三行
print(df.tail(3)) # df的后三行

```



## pandas核心

### pandas描述性统计

数值型数据的描述性统计主要包括了计算数值型数据的完整情况、最小值、均值、中位 数、最大值、四分位数、极差、标准差、方差、协方差等。在NumPy库中一些常用的统计学函数也可用于对数据框进行描述性统计。

```python
np.min	最小值 
np.max	最大值 
np.mean	均值 
np.ptp	极差 
np.median	中位数 
np.std	标准差 
np.var	方差 
np.cov	协方差
```

实例：

```python
import pandas as pd
import numpy as np

# 创建DF
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

df = pd.DataFrame(d)
print(df)
# 测试描述性统计函数
print(df.sum())
print(df.sum(1))
print(df.mean())
print(df.mean(1))
```

pandas提供了统计相关函数：

| 1    | `count()`   | 非空观测数量     |
| ---- | ----------- | ---------------- |
| 2    | `sum()`     | 所有值之和       |
| 3    | `mean()`    | 所有值的平均值   |
| 4    | `median()`  | 所有值的中位数   |
| 5    | `std()`     | 值的标准偏差     |
| 6    | `min()`     | 所有值中的最小值 |
| 7    | `max()`     | 所有值中的最大值 |
| 8    | `abs()`     | 绝对值           |
| 9    | `prod()`    | 数组元素的乘积   |
| 10   | `cumsum()`  | 累计总和         |
| 11   | `cumprod()` | 累计乘积         |

pandas还提供了一个方法叫作describe，能够一次性得出数据框所有数值型特征的非空值数目、均值、标准差等。

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print(df.describe())
print(df.describe(include=['object']))
print(df.describe(include=['number']))

```

### pandas排序

*Pandas*有两种排序方式，它们分别是按标签与按实际值排序。

```python
import pandas as pd
import numpy as np

unsorted_df=pd.DataFrame(np.random.randn(10,2),
                         index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print(unsorted_df)
```

**按行标签排序**

使用`sort_index()`方法，通过传递`axis`参数和排序顺序，可以对`DataFrame`进行排序。 默认情况下，按照升序对行标签进行排序。

```python
import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
unsorted_df = pd.DataFrame(d)
# 按照行标进行排序
sorted_df=unsorted_df.sort_index()
print (sorted_df)
# 控制排序顺序
sorted_df = unsorted_df.sort_index(ascending=False)
print (sorted_df)
```

**按列标签排序**

```python
import numpy as np

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
unsorted_df = pd.DataFrame(d)
# 按照列标签进行排序
sorted_df=unsorted_df.sort_index(axis=1)
print (sorted_df)
```

**按某列值排序**

像索引排序一样，`sort_values()`是按值排序的方法。它接受一个`by`参数，它将使用要与其排序值的`DataFrame`的列名称。

```python
import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
unsorted_df = pd.DataFrame(d)
# 按照年龄进行排序
sorted_df = unsorted_df.sort_values(by='Age')
print (sorted_df)
# 先按Age进行升序排序，然后按Rating降序排序
sorted_df = unsorted_df.sort_values(by=['Age', 'Rating'], ascending=[True, False])
print (sorted_df)

```

### pandas分组

在许多情况下，我们将数据分成多个集合，并在每个子集上应用一些函数。在应用函数中，可以执行以下操作 :

- *聚合* - 计算汇总统计
- *转换* - 执行一些特定于组的操作
- *过滤* - 在某些情况下丢弃数据

```python
import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print(df)

```

#### 将数据拆分成组

```python
# 按照年份Year字段分组
print (df.groupby('Year'))
# 查看分组结果
print (df.groupby('Year').groups)

```

#### 迭代遍历分组

groupby返回可迭代对象，可以使用for循环遍历：

```python
print (df.groupby('Year').groups)
# 遍历每个分组
for year,group in grouped:
    print (year)
    print (group)

```

#### 获得一个分组细节

```python
grouped = df.groupby('Year')
print (grouped.get_group(2014))

```

#### 分组聚合

聚合函数为每个组返回聚合值。当创建了分组(*group by*)对象，就可以对每个分组数据执行求和、求标准差等操作。

```python
# 聚合每一年的平均的分
grouped = df.groupby('Year')
print (grouped['Points'].agg(np.mean))
# 聚合每一年的分数之和、平均分、标准差
grouped = df.groupby('Year')
agg = grouped['Points'].agg([np.sum, np.mean, np.std])
print (agg)
```

#### pandas透视表与交叉表

有如下数据：

```python
import pandas as pd
left = pd.DataFrame({
         'student_id':[1,2,3,4,5,6,7,8,9,10],
         'student_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung', 'Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'class_id':[1,1,1,2,2,2,3,3,3,4]})
right = pd.DataFrame(
         {'class_id':[1,2,3,5],
         'class_name': ['ClassA', 'ClassB', 'ClassC', 'ClassE']})
# 合并两个DataFrame
data = pd.merge(left,right)
print(data)
```

**透视表**

透视表(pivot table)是各种电子表格程序和其他数据分析软件中一种常见的数据汇总工具。**它根据一个或多个键对数据进行分组聚合，并根据每个分组进行数据汇总**。

```python
# 以class_id与gender做分组汇总数据，默认聚合统计所有列
print(data.pivot_table(index=['class_id', 'gender']))

# 以class_id与gender做分组汇总数据，聚合统计score列
print(data.pivot_table(index=['class_id', 'gender'], values=['score']))

# 以class_id与gender做分组汇总数据，聚合统计score列，针对age的每个值列级分组统计
print(data.pivot_table(index=['class_id', 'gender'], values=['score'], 
                       columns=['age']))

# 以class_id与gender做分组汇总数据，聚合统计score列，针对age的每个值列级分组统计，添加行、列小计
print(data.pivot_table(index=['class_id', 'gender'], values=['score'], 
                       columns=['age'], margin=True))

# 以class_id与gender做分组汇总数据，聚合统计score列，针对age的每个值列级分组统计，添加行、列小计
print(data.pivot_table(index=['class_id', 'gender'], values=['score'], 
                       columns=['age'], margins=True, aggfunc='max'))

```

**交叉表**

交叉表(cross-tabulation, 简称crosstab)是一种用于**计算分组频率的特殊透视表**：

```python
# 按照class_id分组，针对不同的gender，统计数量
print(pd.crosstab(data.class_id, data.gender, margins=True))

```



### pandas数据表关联操作

Pandas具有功能全面的高性能内存中连接操作，与SQL等关系数据库非常相似。
Pandas提供了一个单独的`merge()`函数，作为DataFrame对象之间所有标准数据库连接操作的入口。

**合并两个DataFrame：**

```python
import pandas as pd
left = pd.DataFrame({
         'student_id':[1,2,3,4,5,6,7,8,9,10],
         'student_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung', 'Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'class_id':[1,1,1,2,2,2,3,3,3,4]})
right = pd.DataFrame(
         {'class_id':[1,2,3,5],
         'class_name': ['ClassA', 'ClassB', 'ClassC', 'ClassE']})
print (left)
print("========================================")
print (right)
print("========================================")
# 合并两个DataFrame
rs = pd.merge(left,right)
print(rs)
```

**使用“how”参数合并DataFrame：**

```python
# 合并两个DataFrame (左连接)
print("========================================")
rs = pd.merge(left, right, how='left')
print(rs)
```

其他合并方法同数据库相同：

| 合并方法 | SQL等效            | 描述             |
| -------- | ------------------ | ---------------- |
| `left`   | `LEFT OUTER JOIN`  | 使用左侧对象的键 |
| `right`  | `RIGHT OUTER JOIN` | 使用右侧对象的键 |
| `outer`  | `FULL OUTER JOIN`  | 使用键的联合     |
| `inner`  | `INNER JOIN`       | 使用键的交集     |

试验：

```python
# 合并两个DataFrame (左连接)
rs = pd.merge(left,right,on='subject_id', how='right')
print(rs)
# 合并两个DataFrame (左连接)
rs = pd.merge(left,right,on='subject_id', how='outer')
print(rs)
# 合并两个DataFrame (左连接)
rs = pd.merge(left,right,on='subject_id', how='inner')
print(rs)

```

### pandas可视化

**基本绘图：绘图**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp 

df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('2018/12/18',
   periods=10), columns=list('ABCD'))
df.plot()
mp.show()
```

plot方法允许除默认线图之外的少数绘图样式。 这些方法可以作为`plot()`的`kind`关键字参数。这些包括 ：

- `bar`或`barh`为条形
- `hist`为直方图
- `scatter`为散点图

**条形图**

```python
df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar()
# df.plot.bar(stacked=True)
mp.show()
```

**直方图**

```python
df = pd.DataFrame()
df['a'] = pd.Series(np.random.normal(0, 1, 1000)-1)
df['b'] = pd.Series(np.random.normal(0, 1, 1000))
df['c'] = pd.Series(np.random.normal(0, 1, 1000)+1)
print(df)
df.plot.hist(bins=20)
mp.show()
```

**散点图**

```python
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b')
mp.show()
```

**饼状图**

```python
df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True)
mp.show()

```



## Jupyter notebook

Jupyter Notebook（此前被称为 IPython notebook）是一个交互式笔记本，支持运行 40 多种编程语言。使用浏览器作为界面，向后台的IPython服务器发送请求，并显示结果。 Jupyter Notebook 的本质是一个 Web 应用程序，便于创建和共享文学化程序文档，支持实时代码，数学方程，可视化和 markdown。 

IPython 是一个 python 的交互式 shell，比默认的python shell 好用得多，支持变量自动补全，自动缩进，支持 bash shell 命令，内置了许多很有用的功能和函数。

**安装ipython**

**windows：** 	前提是有numpy，matplotlib  pandas 

​			采用pip安装  ```pip install ipython```

**OS X：**		AppStore下载安装苹果开发工具Xcode。

​			使用easy_install或pip安装IPython，或者从源文件安装。

**安装Jupyter notebook**

```python
pip3 install jupyter
```

#### 数据读取与存储

**读取与存储csv：**

```python
# filepath 文件路径。该字符串可以是一个URL。有效的URL方案包括http，ftp和file 
# sep 分隔符。read_csv默认为“,”，read_table默认为制表符“[Tab]”。
# header 接收int或sequence。表示将某行数据作为列名。默认为infer，表示自动识别。
# names 接收array。表示列名。
# index_col 表示索引列的位置，取值为sequence则代表多重索引。 
# dtype 代表写入的数据类型（列名为key，数据格式为values）。
# engine 接收c或者python。代表数据解析引擎。默认为c。
# nrows 接收int。表示读取前n行。

pd.read_table(
    filepath_or_buffer, sep='\t', header='infer', names=None, 
    index_col=None, dtype=None, engine=None, nrows=None) 
pd.read_csv(
    filepath_or_buffer, sep=',', header='infer', names=None, 
    index_col=None, dtype=None, engine=None, nrows=None)
```

```python
DataFrame.to_csv(excel_writer=None, sheetname=None, header=True, index=True, index_label=None, mode=’w’, encoding=None) 
```

**读取与存储excel：**

```python
# io 表示文件路径。
# sheetname 代表excel表内数据的分表位置。默认为0。 
# header 接收int或sequence。表示将某行数据作为列名。默认为infer，表示自动识别。
# names 表示索引列的位置，取值为sequence则代表多重索引。
# index_col 表示索引列的位置，取值为sequence则代表多重索引。
# dtype 接收dict。数据类型。
pandas.read_excel(io, sheetname=0, header=0, index_col=None, names=None, dtype=None)
```

```python
DataFrame.to_excel(excel_writer=None, sheetname=None, header=True, index=True, index_label=None, mode=’w’, encoding=None) 
```

**读取与存储JSON：**

```python
# 通过json模块转换为字典，再转换为DataFrame
pd.read_json('../ratings.json')
```



## movielens电影评分数据分析

需求如下：

1. 读取数据，从用户表读取用户信息、同样方法，导入电影评分表、电影数据表。
2. 合并数据表
3. 对数据初步描述分析
4. 查看每一部电影不同性别的平均评分并计算分歧差值，之后排序
5. 算出每部电影平均得分并对其进行排序
6. 查看评分次数多的电影并进行排序 
7. 过滤掉评分条目数不足250条的电影
8. 评分最高的十部电影
9. 查看不同年龄的分布情况并且采用直方图进行可视化
10. 在原数据中标记出用户位于的年龄分组
11. 可视化显示movies_ratings中不同类型电影的频数











