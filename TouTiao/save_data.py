import pymysql



def get_appid():
    coon = pymysql.connect(
        host = '114.55.181.55',user = 'phb_read',passwd = 'deidvWWU%f9Xp4f',
        port = 15000,charset = 'utf8',database='cb_jrtt_account'
        # host = '192.168.2.215',user = 'test1',passwd = 'test1',
        # port = 3306,charset = 'utf8',database='others'
    )
    cur = coon.cursor()  #建立游标
    cur.execute("SELECT user_id from cb_jrtt_account")  #查询数据

    res = cur.fetchall()
    #获取结果
    print(res)
    return res

    # cur.close()     #关闭游标
    # coon.close()    #关闭连接

get_appid()