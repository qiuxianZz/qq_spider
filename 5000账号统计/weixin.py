
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




def save_data():
    """储存专辑信息"""
    try:
        conn = get_conn()
        # t_data = tuple(data)
        sql = "SELECT uid,count(*) as num,GROUP_CONCAT(nickname) as names,GROUP_CONCAT(service_type) as types FROM `WeiXin_data`  WHERE  insert_time <= '2019-03-01' group by uid "
        print(sql)
        execute_sql(sql,conn)
        close_conn(conn)
    except Exception as e:
        print(e)

save_data()