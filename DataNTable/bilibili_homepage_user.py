import pandas as pd

import pymysql


def newUser():
    conn = pymysql.connect(host="47.111.18.145", port=15003, user="qx_bili", password="VroXGdKa", db="nr-bilibili")
    res =[]

    total_sql = "select count(*) from acq_bilibili_user"
    df = pd.read_sql(total_sql, conn)

    total = df['count(*)'][0]
    res.append(total)
    res =res+["user总数量"]
    for item in ['B站榜单','关注冲榜','网站冲榜','B站推荐']:
        sql = "SELECT count(*) as x from acq_bilibili_user where submit_user = \'{}\'".format(item)
        print(sql)
        df = pd.read_sql(sql, conn)
        total = df['x'][0]
        res.append(total)
        res =res+["{}总数量".format(item)]


    conn.close()
    return res


print(newUser())
