import hashlib
from random import random

import execjs
import xlrd


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

print(export_data('./5月25日至6月7日头条号.xlsx'))





def non():
    """随机数"""
    li = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    nonce = ''.join(li[random.randint(0, 15)] for _ in range(9))
    print(nonce)
    return nonce




def formatData(data):
    """处理sql字符串引号"""
    if(data == None or data == ''):
        return  ""
    data=data.replace("'","\\\'")
    return  data.replace('"','\\\"')


def md5(parm):
    """生成md5"""
    hl = hashlib.md5()
    hl.update(parm.encode(encoding='utf-8'))
    sign = hl.hexdigest()
    print((sign))
    return sign

import execjs

# 读取js文件
# with open('Toutiao.js', encoding='utf-8') as f:
#     js = f.read()
#
# 通过compile命令转成一个js对象
# docjs = execjs.compile(js)
#
# 调用function方法
# res = docjs.call('qq')
# print(res)
#
# 调用变量方法
# res = docjs.eval('asd')
# print(res)
