import re
import threading
import time
import pymysql

import  requests
import json
from lxml import etree







def get_brandStoreName(id):
    # print(id)
    url = 'https://mapi.vip.com/vips-mobile/rest/shopping/wap/product/detail/v5?app_name=shop_wap&api_key=8cec5243ade04ed3a02c5972bcda0d3f&productId={}'.format(id)
    print(url)
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://m.vip.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    # print(res.text)
    json_data = json.loads(res.text)

    # brandId = json_data['data']['product']['brandId']
    # productId = json_data['data']['product']['productId']
    try:
        brandStoreName = json_data['data']['product']['brandStoreName']
        # print(brandStoreName)
        storeName = json_data['data']['store']['storeName']
    except KeyError:
        return brandStoreName,brandStoreName
    # print(storeName)
    return brandStoreName,storeName






def updata_sql_commodity():

    coon = pymysql.connect(
        host = '114.55.181.55',user = 'acq_dy',passwd = 'vah$am_dzqEL8',
        port = 15000,charset = 'utf8',database='nr_dy'
    )
    cur = coon.cursor()  #建立游标
    # cur.execute("select `detail_url`  FROM `ana_douyin_promotion_realtime` WHERE promotion_source = 10 AND  acq_status = 0")  #查询数据
    cur.execute("select `product_id`  FROM `ana_douyin_promotion_realtime` WHERE promotion_source = 10")  #查询数据
    res = cur.fetchall()
    print(res)#获取结果
    for item in range(len(res)):
        u_id = res[item]
        # patterns = re.compile('html\?pid=(.*?)&',re.S)
        # result = patterns.findall(u_id[0])
        brandStoreName,storeName = get_brandStoreName(u_id[0])
        # print(brandStoreName,storeName)
        sql = "UPDATE `ana_douyin_promotion_realtime` SET shop_name='{}',brand_name='{}',acq_status=1,acq_time = now() WHERE product_id ='{}'".format(storeName,brandStoreName,u_id[0])
        # cur.execute(sql)
        print(sql)
        # coon.commit()
    cur.close()     #关闭游标
    coon.close()    #关闭连接


updata_sql_commodity()

# 完美日记（PERFECT DIARY）




