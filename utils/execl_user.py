# coding=utf-8
import re

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
        host='192.168.2.210',
        port=3306,
        user='phb_data',
        password='phb_2014',
        database='phb_data'
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
        sql = "insert ignore into acq_tt_user  (uid ,name)values (\"%s\",\"%s\")" % (str(uid), str(name))
        # sql = "UPDATE acq_tt_user SET uid = \"%s\",name = \"%s\"  where name = \"%s\" " %  (str(uid), str(name),str(name))
        print(sql)
        execute_sql(sql, conn)
        close_conn(conn)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    excelFile = '5月25日至6月7日头条号.xlsx'
    data = (read_xlrd(excelFile=excelFile))
    for item in data:
        print(item[1])
        uids =  re.findall('user/(.*?)/#mid',item[1],re.S)
        save_data((uids[0]), item[0])
