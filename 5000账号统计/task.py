import pymysql





def get_conn():
    # 建立链接
    conn = pymysql.Connection(
        host='192.168.2.215',
        port=3306,
        user='test1',
        password='test1',
        database='others'
    )
    return conn


def execute_sql(sql, conn):
    # 获取游标
    cursor = conn.cursor()
    cursor.execute(sql)


def close_conn(conn):
    # conn.commit()
    # 关闭连接
    conn.close()




def save_data(data):
    """储存专辑信息"""
    try:
        conn = get_conn()
        # t_data = tuple(data)
        sql = "insert ignore into weixin_data (uid ,uuid,appid,`status`,ban_id,nickname,username,`desc`,service_type,basic_type,type,certified_text,province,city,tax_num,headimg_url,request_domain,output_time,auth3rd,memo,insert_time,update_time,verify_type_info,qrcode_url,source,jh_code )" \
              "VALUES " '('"{}"')'.format(data)
        print(sql)
        execute_sql(sql,conn)
        close_conn(conn)
    except Exception as e:
        print(e)





def get_appid(uid):
    """
    通过uid拿到appid
    :param uid:
    :return:
    """
    coon = pymysql.connect(
        host = '112.124.50.233',user = 'phb_read',passwd = 'jKWlUtN3nkR#',
        port = 15858,charset = 'utf8',database='phb_main'
        #port必须写int类型
        #charset必须写utf8，不能写utf-8
    )
    cur = coon.cursor()  #建立游标
    cur.execute("SELECT `uid`,`appid`,`insert_time` from `mini_program_and_user` where `uid` = {} ".format(uid))  #查询数据

    res = cur.fetchall()
    #获取结果
    print(res)
    return res

    # cur.close()     #关闭游标
    # coon.close()    #关闭连接
# uid
# 269666
# 278380
# 312877
# 18767
# 377
# 7121
# 70486
# 588189
# 543619
# 18694
# 18690
# 245036
# 107637
# 173883
# 308328

get_appid(278380)


def get_data(appid):
    # print(appid)
    coon = pymysql.connect(
        host = '112.124.50.233',user = 'phb_read',passwd = 'jKWlUtN3nkR#',
        port = 15858,charset = 'utf8',database='phb_main'
        #port必须写int类型
        #charset必须写utf8，不能写utf-8
    )
    cur = coon.cursor()  #建立游标
    cur.execute('select * FROM `weixin_mini_program` WHERE `appid` = "%s"' % appid)  #查询数据

    res = cur.fetchall()    #获取结果
    print(res)
    return res

get_data('wx9edfaf4ccb6fa37b')