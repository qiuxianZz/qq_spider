import datetime
import pandas as pd
import time

# a = (46816, 'FB435852F8B098867678593FFAA3AFB6', 'wx1d5302b1f090b8e8', 0, 1, '几何汽车Geometry', 'gh_97d1f1bee2b1', '几何汽车官方小程序，打开了解更多。', '汽车厂商', '生活服务', 0, '浙江吉利控股集团汽车销售有限公司', '浙江', None, '91330000746323316J', 'http://wx.qlogo.cn/mmhead/Q3auHgzwzM44OgnvjrW8jVVd9qk50We7jAe9hvxcLhhcNDNBaMHKdA/0', 'https://apis.map.qq.com, https://campaign.geely.com, https://geely.dev.ftms-weixin.com, https://geely.test.ftms-weixin.com, https://geometryxcx.geely.com, https://restapi.amap.com, https://www1.pcauto.com.cn', datetime.datetime(2019, 6, 26, 18, 10, 37).strftime("%Y-%m-%d %H:%M:%S"), '宁波邻家网络科技有限公司', None, str(datetime.datetime(2019, 6, 26, 18, 10, 37)), datetime.datetime(2019, 11, 6, 23, 29, 22), None, None, 0, None)
#
# print(a)
# # a = datetime.datetime(2019, 6, 26, 18, 10, 37)
# # print(a)
# # 2019-10-17 11:16:15
# # 2019-06-26 18:10:37
# #
# # for i in a:
# #     print(i)
#
# print(str(datetime.datetime(2019, 6, 26, 18, 10, 37)))
#
# t = datetime.datetime.strptime("2019-06-26 18:10:37", "%Y-%m-%d %H:%M:%S")
# print (type(t))

# a = (46816, 'FB435852F8B098867678593FFAA3AFB6', 'wx1d5302b1f090b8e8', 0, 1, '几何汽车Geometry', 'gh_97d1f1bee2b1', '几何汽车官方小程序，打开了解更多。', '汽车厂商', '生活服务', 0, '浙江吉利控股集团汽车销售有限公司', '浙江', None, '91330000746323316J', 'http://wx.qlogo.cn/mmhead/Q3auHgzwzM44OgnvjrW8jVVd9qk50We7jAe9hvxcLhhcNDNBaMHKdA/0', 'https://apis.map.qq.com, https://campaign.geely.com, https://geely.dev.ftms-weixin.com, https://geely.test.ftms-weixin.com, https://geometryxcx.geely.com, https://restapi.amap.com, https://www1.pcauto.com.cn', str(datetime.datetime(2019, 6, 26, 18, 10, 37)), '宁波邻家网络科技有限公司', None, str(datetime.datetime(2019, 4, 12, 12, 8, 36)), str(datetime.datetime(2019, 11, 6, 23, 29, 22)), None, None, 0, None)
# # print(a)

# a = (63439, '1E1914048496E1CF65AAA6F791E2F22F', 'wxf52daf77fffdcc13', 0, 1, 'ProWine', 'gh_bf94a678e29f', 'International Trade Fair for Wines and Spirits   国际葡萄酒和烈酒贸易展览会', '会展服务', '生活服务', 0, '杜塞尔多夫展览(上海)有限公司', None, None, '91310115692911015J', 'http://wx.qlogo.cn/mmhead/Q3auHgzwzM4IIBk2b7icgicweGts5k1Z6swlDvDCdC46ibW26PncSX4gA/0', 'https://prowine.winewin9.com', datetime.datetime(2019, 11, 1, 12, 30, 57), None, None, datetime.datetime(2019, 10, 7, 5, 22, 16), datetime.datetime(2019, 11, 7, 0, 0, 57), None, None, 0, None)


def transform(data):
    data_list = []
    for i in a:
        if i ==  None:
            i = ''
        x = (str(i))
        data_list.append(x)
    return str(data_list)[1:-1:]


# prtransform(a)



# data = pd.read_excel('10月企业.xlsx')


# Use the multi-axes indexing funtion

# print (data.loc[[1,3,5],['uid']]) #读取第1、3、5行的标签为salary、name的数据

# for i in range(1,5):
#     a = (data.loc[[i],['uid']])
#
#     print(str(a))



#
#
# def timeStamp_(Y,m,d,H,M,S):
#     tss = '%s-%s-%s %s:%s:%s'%(Y,m,d,H,M,S)
#     timeArray = time.strptime(tss, "%Y-%m-%d %H:%M:%S")
#     timeStamp = int(time.mktime(timeArray))
#     return timeStamp

# print(timeStamp_(2019, 11, 1, 12, 30, 57))




#
# import xlrd
# import sys
# def open_excel(excel_file):
#     try:
#         book = xlrd.open_workbook(excel_file)  # 文件名，把文件与py文件放在同一目录下
#         print(sys.getsizeof(book))
#         return book
#     except:
#         print("open excel file failed!")
#
#
# open_excel('10月企业.xlsx')

# import xlrd
# worksheet = xlrd.open_workbook('10月企业.xlsx')
# sheet_names= worksheet.sheet_names()
# for sheet_name in sheet_names:
#     sheet2 = worksheet.sheet_by_name(sheet_name)
# # print(sheet_name rows) = sheet2.row_values(3) # 获取第四行内容
# cols = (sheet2.col_values(0))
# print(cols)

# for item in range(12):
#     print(sheet2.col_values(item))

# df=pd.read_excel('10月企业.xlsx')#这个会直接默认读取到这个Excel的第一个表单
# data=df.head(5000)#默认读取前5行的数据
# print("获取到所有的值:\n{0}".format(data))#格式化输出

# df=pd.read_excel('10月企业.xlsx')#这个会直接默认读取到这个Excel的第一个表单
# data=df.ix[0].values#0表示第一行 这里读取数据并不包含表头，要注意哦！
# print(data)
import requests
import json
import xlrd
from lxml import html

#路径前加 r，读取的文件路径
def export_data(excle_data:str):
    """
    :param excle_data: 文件路径
    :return:
    """
    file_path = excle_data
    workbook = xlrd.open_workbook(file_path)

    # 根据sheet索引或者名称获取sheet内容
    Data_sheet = workbook.sheets()[0] # 通过索引获取

    rowNum = Data_sheet.nrows # sheet行数
    colNum = Data_sheet.ncols # sheet列数

    # 获取所有单元格的内容
    list = []
    for i in range(rowNum):
        rowlist = []
        for j in range(colNum):
            rowlist.append(Data_sheet.cell_value(i, j))
        list.append(rowlist)

    return list

data = (export_data('./10月企业.xlsx'))

data_list = []

a = data[0]
for i in range(1,len(data)):
    b= data[i]
    d={}
    for x in range(len(a)):
        if a[x] in d:

            d[a[x]]+=b[x]
        else:

            d[a[x]]=b[x]
    data_list.append(d)
    # time.sleep(1)

import xlwt

# 1.创建 Workbook
wb = xlwt.Workbook()

# 2.创建 worksheet
ws = wb.add_sheet('test_sheet')

# 3.写入第一行内容  ws.write(a, b, c)  a：行，b：列，c：内容
# ws.write(0, 0, '球队')
# ws.write(0, 1, '号码')
# ws.write(0, 2, '姓名')
# ws.write(0, 3, '位置')


for i in range(len(data[0])):
    # print(i,data[0][1])
    ws.write(0, i, data[0][i])


# print(data_list)
# print(data[0])
#
for i, item in enumerate(data_list):
    ws.write(i+1, 0, item['账号名称'])
    ws.write(i+1, 1, item['账号ID'])
    ws.write(i+1, 2, item['类别'])
    ws.write(i+1, 3, item['发布次数'])
    ws.write(i+1, 4, item['文章数'])
    ws.write(i+1, 5, item['阅读数'])
    ws.write(i+1, 6, item['平均阅读数'])
    ws.write(i+1, 7, item['在看数'])
    ws.write(i+1, 8, item['头条阅读数'])
    ws.write(i+1, 9, item['最高阅读数'])
    ws.write(i+1, 10, item['新榜指数'])
    ws.write(i+1, 11, item['uid'])


wb.save('./myExcel.xls')



# 保存文件
# wb.save('./myExcel.xls')
















#
# data = [
#     {
#         'Team': '湖人',
#         'Number': '34',
#         'Name': '奥尼尔',
#         'Positions': '中锋'
#     },
#     {
#         'Team': '湖人',
#         'Number': '24',
#         'Name': '科比',
#         'Positions': '后卫'
#     },
#     {
#         'Team': '湖人',
#         'Number': '23',
#         'Name': '詹姆斯',
#         'Positions': '前锋'
#     },
#     {
#         'Team': '湖人',
#         'Number': '23',
#         'Name': '詹姆斯',
#         'Positions': '前锋'
#     },
#     {
#         'Team': '湖人',
#         'Number': '23',
#         'Name': '詹姆斯',
#         'Positions': '前锋'
#     }
#
#
# ]

# for i, item in enumerate(data):
#     ws.write(i+1, 0, item['Team'])
#     ws.write(i+1, 1, item['Number'])
#     ws.write(i+1, 2, item['Name'])
#     ws.write(i+1, 3, item['Positions'])
#
# wb.save('./myExcel.xls')
#
