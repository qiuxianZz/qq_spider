# coding=utf-8

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


import pymysql


def get_conn():
    # 建立链接
    conn = pymysql.Connection(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        database='qx_data'
    )
    return conn


def execute_sql(sql, conn):
    # 获取游标
    cursor = conn.cursor()
    cursor.execute(sql)


def close_conn(conn):
    conn.commit()
    # 关闭连接
    conn.close()


def save_data(uid, name):
    try:
        conn = get_conn()
        sql = "insert ignore into jrtt_user  (name ,user)values (\"%s\",\"%s\")" % (str(uid), str(name))
        # sql = "UPDATE acq_tt_user SET uid = \"%s\",name = \"%s\"  where name = \"%s\" " %  (str(uid), str(name),str(name))
        print(sql)
        execute_sql(sql, conn)
        close_conn(conn)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    excelFile = '头条认证.xlsx'
    data = (read_xlrd(excelFile=excelFile))
    for item in data:
        print(item[0], item[1])
        save_data((item[0]), item[1])
