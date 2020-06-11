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


def save_result_album(data):
    try:
        conn = get_conn()
        # sql = 'INSERT INTO vvic_user (uid) SELECT {} FROM DUAL WHERE NOT EXISTS (SELECT * FROM vvic_user where uid = {})'.format(
        #     uid, uid)
        # print(sql)
        add = data[2]
        city = data[0]
        name = data[1]
        tel = data[3]
        qq = data[4]
        vx = data[5]
        sql = "INSERT INTO precise_data (`add`,city,`name`,tel,qq,vx) VALUES ('{}','{}','{}','{}','{}','{}')".format(add,city,name,tel,qq,vx)
        print(sql)
        execute_sql(sql, conn)
        close_conn(conn)
    except Exception as e:
        print(e)


def insert_data():
    try:
        # 打开数据库连接
        conn = get_conn()

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = conn.cursor()

        # SQL 查询语句
        sql = "SELECT city,user_name,worker_org_addr,tel from hsfdj "
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            print(row)
            data = []
            data.append(row[0])
            data.append(row[1])
            data.append(row[2])
            data.append(row[3])
            data.append('')
            data.append('')
            save_result_album(data)
            # print("name=%s,age=%s,phone=%s," % (name, age, phone))
        # 关闭游标
        cursor.close()
        # 关闭链接
        conn.close()
        # 发生错误时回滚

    except Exception as e:
        print(e)

insert_data()
