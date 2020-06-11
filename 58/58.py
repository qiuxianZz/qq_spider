import json
import queue
import re
import threading

import pymysql
import requests

from requests.adapters import HTTPAdapter

from qq.Loggeer import Logger
s = requests.session()

# max_retries=3 重试3次
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))
log_obj = Logger('58.log', level='debug')


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
    return cursor.fetchall()


def close_conn(conn):
    conn.commit()
    # 关闭连接
    conn.close()


def formatData(data):
    """处理sql字符串引号"""
    if (data == None or data == ''):
        return ""
    data = data.replace("'", "\\\'")
    return data.replace('"', '\\\"')


def save_con(con):
    try:
        conn = get_conn()
        select_sql = 'select mobile from 58_con_data where mobile = \'{}\''.format(con["mobile"])
        cursor = conn.cursor()
        cursor.execute(select_sql)
        res = cursor.fetchall()
        if res == ():
            sql = 'INSERT INTO 58_con_data (sign,picurl,company,address,wxCode,mobile,tags,position,real_name) VALUES ' \
                  f'("{con["sign"]}", "{con["picUrl"]}", "{con["company"]}", "{con["address"]}",' \
                  f' "{con["wxCode"]}", "{con["mobile"]}","{con["tags"]}","{con["position"]}","{con["realName"]}") '
            log_obj.logger.info(sql)
            execute_sql(sql, conn)
        close_conn(conn)

    except Exception as e:
        print(e)


def save_mpcardId(cardId):
    try:
        conn = get_conn()
        sql = 'INSERT INTO 58_data (mpcardId) SELECT {} FROM DUAL WHERE NOT EXISTS (SELECT * FROM 58_data where mpcardId = \'{}\')'.format(
            cardId, cardId)
        print(sql)
        execute_sql(sql, conn)
        close_conn(conn)
    except Exception as e:
        print(e)


def select_mpcardId():
    while True:
        try:
            conn = get_conn()
            # print(item)
            # name 关键字 用`name
            # {'album_id': '80535308', 'artist_id': '1873', 'album_name': '火火的歌', 'head_img': 'http://p2.music.126.net/PAlBviJ_B9j3Hm91SDzhjw==/109951164236701524.jpg?param=177y177', 'singer': '阿宝', 'publish_time': '2019-07-21', 'publish_company': '\n墨枫文化\n', 'share_count': '', 'comment_count': '1', 'desc': ''}
            sql = "select mpcardId from 58_data where status = 0 limit 1000"
            print(sql)
            res = execute_sql(sql, conn)
            for item in res:
                con = getcon(item[0])
                if con == {}:
                    upsql = 'update 58_data set status = 1 where mpcardId =\'{}\''.format(item[0])
                    print(upsql)
                    conn.cursor().execute(upsql)
                    conn.commit()
                    continue
                save_con(con)
                upsql = 'update 58_data set status = 1 where mpcardId =\'{}\''.format(item[0])
                print(upsql)
                conn.cursor().execute(upsql)
                conn.commit()
                print("update succeed", item[0])
            close_conn(conn)
        except Exception as e:
            print(e)


# url = 'https://yaofa.58.com/mpcard/get?token=WMJVwKFJcds5muHMqFWstg27DcUjtbxzx122Hh&consumerToken=50ba8310-2e32-4b6a-9796-1c8f48287387&mpcardId=1132315412462985216&test='
# url = 'https://yaofa.58.com/search19/mapp?80q88=undefined&appid=yxlcupqpgJdRt3ry5&userid=71501812732944&releaseId=1258223322563616768&mpId=1258223320056164352&env58=true&test=null&page=100&size={}&cate1=8512&cate2=&cate3=&latitude=30.64242&longitude=104.04311'
#
# 'https://yaofa.58.com/search19/mapp?8i4lq=undefined&appid=yxlcupqpgJdRt3ry5&userid=71501812732944&releaseId=1258223322563616768&mpId=1258223320056164352&env58=true&test=null&page=2&size=20&product=20001&cityId=1'
# 'https://yaofa.58.com/search19/mapp?8gmer=undefined&appid=yxlcupqpgJdRt3ry5&userid=71501812732944&releaseId=1258223322563616768&mpId=1258223320056164352&env58=true&test=null&page=3&size=20&product=20001&latitude=30.64242&longitude=104.04311'

headers = {
    # 'Host': 'yaofa.58.com',
    # 'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    # 'content-type': 'application/json',
    # 'Referer': 'https://servicewechat.com/wx86c7b0019914401c/87/page-frame.html',
    # 'Accept-Encoding': 'gzip, deflate, br'


}


def getreleaseId(page, cityid):
    url = 'https://yaofa.58.com/search19/mapp?8i2ox=undefined&appid=yxlcupqpgJdRt3ry5&userid=71501812732944&releaseId=1258223322563616768&mpId=1258223320056164352&env58=true&test=null&page={}&size=60&sort=visit_desc&product=20001&cityId={}'
    res = s.get(url.format(page, cityid), headers=headers, timeout=15)
    releaseId_list = []
    data = json.loads(res.text)
    data = data["data"]
    # if len(data) != 60:
    #     return 1
    if data == None or data == []:
        return releaseId_list
    for item in data:
        releaseId = item["releaseId"]
        releaseId_list.append(releaseId)
    return releaseId_list


def getcardId(releaseId):
    url = 'https://yaofa.58.com/search/detail?7wgn8=undefined&appid=yxlcupqpgJdRt3ry5&userid=42419989824019&releaseId={}&mpId=1258223320056164352&env58=true&test=null&userId=&appId=&consumerToken=cb448eb3-42e1-46c1-85e1-1c4ae7d38131'
    res = s.get(url.format(releaseId), headers=headers, timeout=15)
    data = json.loads(res.text)
    try:
        data = data["data"]
        if data == None:
            return
        cardId = data["extJson"]["ext"]["cardId"]
        return (cardId)
    except KeyError:
        cardId = re.findall('"cardId":"(.*?)"', res.text, re.S)
        return cardId[0]


def getcon(mpcardId):
    # url = 'https://yaofa.58.com/mpcard/get?token=WMJVwKFJcds5muHMqFWstg27DcUjtbxzx122Hh&consumerToken=50ba8310-2e32-4b6a-9796-1c8f48287387&mpcardId={}&test='
    url = 'https://yaofa.58.com/mpcard/get?token=XYdmgFMPbVqjGzU28xvTogS6JHCWfw8n4AbiqH&consumerToken=ffa1f814-3510-47f0-85a4-b0acea13acf7&mpcardId={}&test=null'
    res = s.get(url.format(mpcardId), headers=headers, timeout=15)
    data = json.loads(res.text)
    con = {}
    data = data["data"]
    if data == None:
        return {}
    sign = data["sign"]
    con["sign"] = sign
    picUrl = data["picUrl"]
    con["picUrl"] = 'https://t2.58cdn.com.cn' + picUrl
    company = data["company"]
    con["company"] = company
    address = data["address"]
    con["address"] = address
    wxCode = data["wxCode"]
    con["wxCode"] = wxCode
    mobile = data["mobile"]
    con["mobile"] = mobile
    tags = data["tags"]
    con["tags"] = tags
    position = data["position"]
    con["position"] = position
    realName = data["realName"]
    con["realName"] = realName
    return con


def main():
    page = 1
    cityid = 23869
    while True:
        print(page, "============================")
        print(cityid, "=======================")
        res = getreleaseId(page, cityid)
        if res == []:
            page = 1
            cityid += 1
        page += 1
        print(len(res))
        for item in res:
            cardId = getcardId(item)
            if cardId == None:
                continue
            save_mpcardId(cardId)
            # con = getcon(cardId)
            # save_con(con)


q = queue.Queue()

gLock = threading.Lock()


def Producer():
    conn = get_conn()
    sql = "select mpcardId from 58_data where status = 0 limit 1000"
    log_obj.logger.info(sql)
    res = execute_sql(sql, conn)
    for item in res:
        q.put(item[0])
    log_obj.logger.info(q.qsize())
    # gLock.release()


def Consumer():
    '''消费者'''
    while True:
        gLock.acquire()
        i = q.get()  # 从队列中取数据
        if q.qsize() < 100:
            Producer()
        gLock.release()
        con = getcon(i)
        conn = get_conn()
        if con == {}:
            upsql = 'update 58_data set status = 1 where mpcardId =\'{}\''.format(i)
            log_obj.logger.info(upsql)
            conn.cursor().execute(upsql)
            conn.commit()
            continue
        save_con(con)
        upsql = 'update 58_data set status = 1 where mpcardId =\'{}\''.format(i)
        log_obj.logger.info(upsql)
        conn.cursor().execute(upsql)
        conn.commit()
        log_obj.logger.info("update succeed : " + i)
        # time.sleep(1)


def run():
    p = threading.Thread(target=Producer)
    p.start()
    threads = [threading.Thread(target=Consumer) for _ in range(30)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    run()
    # Producer()
    # main()
    # select_mpcardId()
