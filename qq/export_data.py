import re

import pymysql, xlwt, openpyxl
import xlsxwriter


# #url=jdbc:mysql://114.55.181.55:15000/phb_data?useUnicode=true&characterEncoding=UTF-8&autoReconnect=true
# username=acq_qx
# password=L6vS8!XbR7_xLP
def get_conn():
    # 建立链接
    conn = pymysql.Connection(
        host='127.0.0.1',
        # host='114.55.181.55',''
        port=3306,
        # port=15000,
        user='root',
        # user='acq_qx',
        # password='L6vS8!XbR7_xLP',
        password='123456',
        database='qx_data'
        # database='phb_data'
    )
    return conn


def export_excel(sql, table_name):
    conn = get_conn()
    cur = conn.cursor()
    # 读取数据
    cur.execute(sql)
    fileds = [filed[0] for filed in cur.description]
    print(fileds)
    all_date = cur.fetchall()  # 所有数据
    # for result in all_date:
    #     print(result)

    # 写excel

    book = xlwt.Workbook()  # 创建一个book

    sheet = book.add_sheet('result')  # 创建一个sheet表

    for col, filed in enumerate(fileds):
        sheet.write(0, col, filed)

    # 从第一行开始写

    row = 1
    for data in all_date:
        for col, filed in enumerate(data):
            sheet.write(row, col, filed)
        row += 1

    book.save('%s.xls' % table_name)

#
def writetoxlsx(sql):

    conn = get_conn()
    cur = conn.cursor()
    # 读取数据
    cur.execute(sql)
    fileds = [filed[0] for filed in cur.description]
    print(fileds)
    data = cur.fetchall()  # 所有数据
    outwb = openpyxl.Workbook()  # 打开一个将写的文件
    outws = outwb.create_sheet(index=0)  # 在将写的文件创建sheet

    i = 1  # 注意：'cell'函数中行列起始值为1
    ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')

    for line in data:
        for x in range(0,len(line)):
            print(line[x])
            outws.cell(column = x+1 , row = i , value = "%s" % line[x])
        i += 1

    savexlsx = "./results.xlsx"
    outwb.save(savexlsx)  # 保存结果
    data.close()


if __name__ == '__main__':
    # sql = input("sql: ")
    # moble_name = input("moble_name :")
    export_excel("select * from 58_con_data", "58_data")
    # writetoxlsx("select * from 58_con_data")
