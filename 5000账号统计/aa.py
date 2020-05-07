import time

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
    conn.commit()
    # 关闭连接
    conn.close()




def timeStamp_(Y,m,d,H,M,S):
    tss = '%s-%s-%s %s:%s:%s'%(Y,m,d,H,M,S)
    timeArray = time.strptime(tss, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

# print(timeStamp_(2019, 11, 1, 12, 30, 57))


def save_data(data):
    """储存专辑信息"""
    try:
        conn = get_conn()
        t_data = type(data)
        sql = "insert into weixin_mini_data (sql_id ,uuid,appid,`status`,ban_id,nickname,username,`desc`,service_type,basic_type,type,certified_text,province,city,tax_num,headimg_url,request_domain,output_time,auth3rd,memo,insert_time,update_time,verify_type_info,qrcode_url,source,jh_code )" \
              "VALUES " "{}".format(data)
        execute_sql(sql,conn)
        close_conn(conn)
    except Exception as e:
        print(e)


save_data()
data_list = []
# data = (40819, '233657789E951718FA31A331F8AB7C00', 'wx2bd684b1cb398f2a', 0, 1, '吉利汽车', 'gh_db9e53ac519d', '吉利汽车官方小程序，让您随时掌握吉利最新动态，了解车型信息，预约试乘试驾服务。', '社区/论坛, 汽车厂商, 汽车预售服务', '生活服务', 0, '浙江吉利控股集团汽车销售有限公司', '浙江', None, '91330000746323316J', 'http://wx.qlogo.cn/mmhead/Q3auHgzwzM6bEiaLgpEoD6DsU7SxJCOeKqS5KQiaaOv6QRULNjIKb0hQ/0', 'https://geely.dev.ftms-wechat.com, https://opapi.prod.cloudyoung.cn, https://openapi.dev.cloud-young.cn, https://restapi.amap.com, https://www.geelyminiprogram.com, https://xiaochengxu.geely.com', datetime.datetime(2019, 7, 10, 13, 59, 37), None, None, datetime.datetime(2019, 1, 30, 3, 27, 35), datetime.datetime(2019, 11, 6, 23, 18, 4), None, None, 0, None)
# for i in data:
#     print(i)
#     if i == None:
#         i = null
#     data_list.append(i)
# print(data_list)

# 40819, '233657789E951718FA31A331F8AB7C00', 'wx2bd684b1cb398f2a', 0, 1, '吉利汽车', 'gh_db9e53ac519d', '吉利汽车官方小程序，让您随时掌握吉利最新动态，了解车型信息，预约试乘试驾服务。', '社区/论坛, 汽车厂商, 汽车预售服务', '生活服务', 0, '浙江吉利控股集团汽车销售有限公司', '浙江', '', '91330000746323316J', 'http://wx.qlogo.cn/mmhead/Q3auHgzwzM6bEiaLgpEoD6DsU7SxJCOeKqS5KQiaaOv6QRULNjIKb0hQ/0', 'https://geely.dev.ftms-wechat.com, https://opapi.prod.cloudyoung.cn, https://openapi.dev.cloud-young.cn, https://restapi.amap.com, https://www.geelyminiprogram.com, https://xiaochengxu.geely.com','', '', '', '', '', '', '', 0, ''
# 40819, '233657789E951718FA31A331F8AB7C00', 'wx2bd684b1cb398f2a', 0, 1, '吉利汽车', 'gh_db9e53ac519d', '吉利汽车官方小程序，让您随时掌握吉利最新动态，了解车型信息，预约试乘试驾服务。', '社区/论坛, 汽车厂商, 汽车预售服务', '生活服务', 0, '浙江吉利控股集团汽车销售有限公司', '浙江', '', '91330000746323316J', 'http://wx.qlogo.cn/mmhead/Q3auHgzwzM6bEiaLgpEoD6DsU7SxJCOeKqS5KQiaaOv6QRULNjIKb0hQ/0', 'https://geely.dev.ftms-wechat.com, https://opapi.prod.cloudyoung.cn, https://openapi.dev.cloud-young.cn, https://restapi.amap.com, https://www.geelyminiprogram.com, https://xiaochengxu.geely.com', '', '', '', '', '', '', '', 0, ''
