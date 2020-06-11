import json

import requests
import xlrd


def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []

    for rowNum in range(table.nrows):
        # if 去掉表头
        if rowNum > 0:
            dataFile.append(table.row_values(rowNum))

    return dataFile


def get_data(name, alias):
    url = "http://114.215.170.4:45200/xdn/infringement/get?from=1&username={}"
    res = requests.get(url.format(alias))
    data = json.loads(res.text)
    code = data["code"]
    if code == 0:
        nickname = data["nickname"]
        headimgurl = data["headimgurl"]
        print(nickname)
        response = requests.get(headimgurl)
        img = response.content
        # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
        with open('./img/' + nickname + '.png', 'wb') as f:
            f.write(img)
    else:
        print('error-', name, "-", alias)


if __name__ == '__main__':
    excelFile = '公众号头像采集名单(2)(1).xlsx'
    data = (read_xlrd(excelFile=excelFile))
    # for item in data:
    get_data('搜吕梁', 'ads0358')
