import json

import pymysql
import requests

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123456", db="qx_data")


url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset={}&format=json&keyword=%E7%A7%91%E6%8A%80&autoload=true&count=20&en_qc=1&cur_tab=4&from=media&pd=user&timestamp=1592292251845'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',

}


def get_id(id):
    res = requests.get(url=url.format(id),headers=headers)
    res = json.loads(res.text)
    data = res['data']
    for item in data:
        uid = item['id']
        sql = 'insert INTO acq_tt_user (uid) VALUES ({}) '.format(uid)
        print(sql)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()


id = 0
while True:
    get_id(id)
    id +=20