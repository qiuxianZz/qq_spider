# # # import json
# # # import re
# # # import threading
# # # import urllib
# # # import time
# # # import requests
# # # import hashlib
# # # import time
# # # import execjs
# # #
# # #
# # #
# # # from db_helper import get_conn, execute_sql, close_conn
# # # from qq_function import formatData
# # # from db_helper import get_conn, execute_sql, close_conn
# # #
# # #
# # # def json_con(url):
# # #     """文章内容"""
# # #     header = {
# # #         "Connection":"keep-alive",
# # #         "Pragma":"no-cache",
# # #         "Cache-Control":"no-cache",
# # #         "Accept":"text/javascript, text/html, application/xml, text/xml, */*",
# # #         "X-Requested-With":"XMLHttpRequest",
# # #         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
# # #         "Content-Type":"application/x-www-form-urlencoded",
# # #         "Referer":"https://www.toutiao.com/c/user/5954781019/",
# # #         "Accept-Encoding":"gzip, deflate, br",
# # #         "Accept-Language":"zh-CN,zh;q=0.9",
# # #     }
# # #
# # #     res = requests.get(url,headers=header)
# # #     data = con(res.text)
# # #     save_result(data)
# # #     print(data)
# # #     print(data['max_behot_time'])
# # #     # global t
# # #     t = data['max_behot_time']
# # #     # save_result(data)
# # #     dic = get_cpas()
# # #     _sig = get_sign(t)
# # #     as1 = dic['as']
# # #     cp = dic['cp']
# # #     url = 'https://www.toutiao.com/c/user/article/?page_type=1&user_id=5954781019&max_behot_time=%s&count=20&as=%s&cp=%s&_signature=%s'%(data['max_behot_time'][0],as1,cp,_sig)
# # #     print(url)
# # #
# # #     while True:
# # #         try:
# # #             json_con(url=url)
# # #         except :
# # #             continue
# # #
# # #
# # #
# # #
# # # def transfer_time(t):
# # #     """时间戳转换成格式时间"""
# # #
# # #     timestamp = int(t)
# # #     #转换成localtime
# # #     time_local = time.localtime(timestamp)
# # #     #转换成新的时间格式(2017-09-16 11:28:54)
# # #     dtime= time.strftime("%Y-%m-%d %H:%M:%S",time_local)
# # #
# # #     return dtime
# # #
# # #
# # # # print(transfer_time(1571821475))
# # #
# # #
# # # def con(json_data):
# # #     """文章内容"""
# # #
# # #     patterns = re.compile('"max_behot_time": (.*?)}, "page_type":',re.S)
# # #     max_behot_time = patterns.findall(json_data)
# # #     # print(max_behot_time)
# # #
# # #     patterns = re.compile('"image_url": "(.*?)", "single_mode"',re.S)
# # #     img = patterns.findall(json_data) # 图片
# # #     # print(len(img))
# # #     # print(img)
# # #     patterns = re.compile('"title":(.*?)", "has_video"',re.S)
# # #     titles = patterns.findall(json_data)
# # #     titles_list = []  # 文章标题
# # #
# # #     for i in titles:
# # #         # print(type(i))
# # #         # print(i.encode('').decode("utf-8"))
# # #         title = i.encode().decode('unicode_escape')
# # #         titles_list.append(title)
# # #     # print(len(titles_list))
# # #     # print(titles_list)
# # #
# # #     patterns = re.compile('"go_detail_count":(.*?), "middle_mode":',re.S)
# # #     pageview = patterns.findall(json_data) # 阅读数
# # #     # print(len(pageview))
# # #     # print(pageview)
# # #     patterns = re.compile('"comments_count":(.*?), "composition":',re.S)
# # #     comments = patterns.findall(json_data) # 评论数
# # #     # print(len(comments))
# # #     # print(comments)
# # #     patterns = re.compile('"behot_time":(.*?), "has_gallery"',re.S)
# # #     times = patterns.findall(json_data)
# # #
# # #     time_list = [] # 发布时间
# # #     for item in times:
# # #         time = transfer_time(item)
# # #         time_list.append(time)
# # #     # print(len(time_list))
# # #     # print(time_list)
# # #     patterns = re.compile('"display_url":(.*?), "behot_time"',re.S)
# # #     url = patterns.findall(json_data) # url
# # #     # print(len(url))
# # #     # print(url)
# # #
# # #     data = {
# # #         "max_behot_time":max_behot_time,
# # #         # "img":img,
# # #         "titles":titles_list,
# # #         "pageview":pageview,
# # #         "comments":comments,
# # #         "time":time_list,
# # #         "url":url
# # #     }
# # #     # result.append(data)
# # #     # print(data)
# # #     return data
# # #
# # #
# # #
# # #
# # #
# # #
# # # def save_result(result):
# # #     """存储数据"""
# # #     for i,j,k,l,m in zip(result['titles'],result['pageview'],result['comments'],result['time'],result['url']):
# # #         data = {
# # #             # "img":h,
# # #             "titles":i,
# # #             "pageview":j,
# # #             "comments":k,
# # #             "time":l,
# # #             "url":m
# # #         }
# # #         # print(data)
# # #         try:
# # #             conn = get_conn()
# # #
# # #             sql = "insert into TouTiao " \
# # #                   "(titles,pageview,comments,time,url)" \
# # #                   "values ('%s','%s','%s'," \
# # #                   "'%s','%s')" % (data["titles"],data["pageview"], data["comments"],data["time"],data["url"])
# # #             # print(sql)
# # #             execute_sql(sql,conn)
# # #             close_conn(conn)
# # #         except Exception as e:
# # #             print(e)
# # #
# # #
# # #
# # #
# # #
# # #
# # # def get_cpas():
# # #     """cp as"""
# # #     with open('ascp.js','r') as f:
# # #         js = f.read()
# # #     ctx = execjs.compile(js)
# # #     return ctx.call('a')
# # #
# # #
# # #
# # # def get_sign(t):
# # #     """_signature"""
# # #     with open('sign.js','r') as f:
# # #         js = f.read()
# # #     ctx = execjs.compile(js)
# # #     return ctx.call('a',t)
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # url = 'https://www.toutiao.com/c/user/article/?page_type=1&user_id=50044041847&max_behot_time=0&count=20&as={}&cp={}&_signature={}'
# # #
# # # dic = get_cpas()
# # # as1 = dic['as']
# # # cp = dic['cp']
# # # t = '0'
# # # _signature = get_sign(t)
# # # url = url.format(as1,cp,_signature)
# # # print(url)
# # # while True:
# # #     try:
# # #         json_con(url=url)
# # #     except :
# # #         continue
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # # def get_as_cp():  # 该函数主要是为了获取as和cp参数，程序参考今日头条中的加密js文件：home_4abea46.js
# # # #     zz = {}
# # # #     now = round(time.time())
# # # #     # print(now) # 获取当前计算机时间
# # # #     e = hex(int(now)).upper()[2:] #hex()转换一个整数对象为16进制的字符串表示
# # # #     # print('e:', e)
# # # #     a = hashlib.md5()  #hashlib.md5().hexdigest()创建hash对象并返回16进制结果
# # # #     # print('a:', a)
# # # #     a.update(str(int(now)).encode('utf-8'))
# # # #     i = a.hexdigest().upper()
# # # #     # print('i:', i)
# # # #     if len(e)!=8:
# # # #         zz = {'as':'479BB4B7254C150',
# # # #               'cp':'7E0AC8874BB0985'}
# # # #         return zz
# # # #     n = i[:5]
# # # #     a = i[-5:]
# # # #     r = ''
# # # #     s = ''
# # # #     for i in range(5):
# # # #         s= s+n[i]+e[i]
# # # #     for j in range(5):
# # # #         r = r+e[j+3]+a[j]
# # # #     zz ={
# # # #         'as':'A1'+s+e[-3:],
# # # #         'cp':e[0:3]+r+'E1'
# # # #     }
# # # #     # print('zz:', zz)
# # # #     # print(zz)
# # # #     return zz
# # # #
# # # # print(get_as_cp())
# # #
# # #
# # # # json_con(url=url)
# # #
# # #
# # #
# # #
# # # # if __name__ == '__main__':
# # # #     main()
# # #
# # #
# # # # def get_as_cp():  # 该函数主要是为了获取as和cp参数，程序参考今日头条中的加密js文件：home_4abea46.js
# # # #     zz = {}
# # # #     now = round(time.time())
# # # #     # print(now) # 获取当前计算机时间
# # # #     e = hex(int(now)).upper()[2:] #hex()转换一个整数对象为16进制的字符串表示
# # # #     # print('e:', e)
# # # #     a = hashlib.md5()  #hashlib.md5().hexdigest()创建hash对象并返回16进制结果
# # # #     # print('a:', a)
# # # #     a.update(str(int(now)).encode('utf-8'))
# # # #     i = a.hexdigest().upper()
# # # #     # print('i:', i)
# # # #     if len(e)!=8:
# # # #         zz = {'as':'479BB4B7254C150',
# # # #               'cp':'7E0AC8874BB0985'}
# # # #         return zz
# # # #     n = i[:5]
# # # #     a = i[-5:]
# # # #     r = ''
# # # #     s = ''
# # # #     for i in range(5):
# # # #         s= s+n[i]+e[i]
# # # #     for j in range(5):
# # # #         r = r+e[j+3]+a[j]
# # # #     zz ={
# # # #         'as':'A1'+s+e[-3:],
# # # #         'cp':e[0:3]+r+'E1'
# # # #     }
# # # #     # print('zz:', zz)
# # # #     # print(zz)
# # # #     return zz
# # # #
# # # # print(get_as_cp())
# # #
# # #
# # # # json_con(url=url)
# # #
# # #
# # #
# # #
# # # # if __name__ == '__main__':
# # # #     main()
# # # import execjs
# # #
# # #
# # # def get_sign(t):
# # #     """_signature"""
# # #     with open('Toutiao.js','r') as f:
# # #         js = f.read()
# # #     ctx = execjs.compile(js)
# # #     return ctx.call('a',t)
# # # print(get_sign('5954781019+0'))
# #
# #
# # # 字符类型的时间
# # import time
# #
# # tss1 = '2013-10-10 23:42:00'
# # tss2 = '2013-10-10 23:41:00'
# # #
# # # # 转为时间数组
# # # timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
# # # # timeArra1 = time.strptime(tss2, "%Y-%m-%d %H:%M:%S")
# # #
# # # print(timeArray)
# # # # timeArray可以调用tm_year等
# # # # print(timeArray.tm_year)   # 2013
# # # # 转为时间戳
# # # timeStamp = int(time.mktime(timeArray))
# # # print(timeStamp)  # 1381419600
# #
# # # Y = 2013
# # # # m = 10
# # # # d = 10
# # # # H = 23
# # # # M = 40
# # # # S = 00
# # a = '05'
# # def timeStamp_(Y,m,d,H,M,S):
# #     tss = '%s-%s-%s %s:%s:%s'%(Y,m,d,H,M,S)
# #     timeArray = time.strptime(tss, "%Y-%m-%d %H:%M:%S")
# #     timeStamp = int(time.mktime(timeArray))
# #     return timeStamp
# # print(timeStamp_(2014,a,22,21,10,00))
# #
# #
# #
# # # 1400764200
# # import time
# #
# #
# # def transfer_time(t):
# #     """时间戳转换成格式时间"""
# #
# #     timestamp = int(t)
# #     #转换成localtime
# #     time_local = time.localtime(timestamp)
# # import re
# # import time
# # import requests
# # import threading
# # from lxml import etree
# # from bs4 import BeautifulSoup
# # from queue import Queue
# # from threading import Thread
# #
# #
#
#
# # def run(in_q, out_q):
# #     headers = {
# #         'Accept': '',
# #         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
# #         'Connection': 'keep-alive',
# #         'Cookie': '',
# #         'DNT': '1',
# #         'Host': 'www.g.com',
# #         'Referer': '',
# #         'Upgrade-Insecure-Requests': '1',
# #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
# #                       '(KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
# #     }
# #     while in_q.empty() is not True:
# #         print(in_q)
# #         nums = ['1546']
# #         for num in nums:
# #             num = re.findall('[0-9]', ''.join(num))
# #             real_num = int(''.join(num))
# #             out_q.put(str(threading.current_thread().getName()) + '-' + str(real_num))
# #         in_q.task_done()
# #
# #
# # if __name__ == '__main__':
# #     start = time.time()
# #     queue = Queue(2)
# #     result_queue = Queue()
# #     for i in range(1, 1001):
# #         queue.put('http://www.g.com?page='+str(i))
# #     print('queue 开始大小 %d' % queue.qsize())
# #
# #     for index in range(10):
# #         thread = Thread(target=run, args=(queue, result_queue, ))
# #         thread.daemon = True  # 随主线程退出而退出
# #         thread.start()
# #
# #     queue.join()  # 队列消费完 线程结束
# #     end = time.time()
# #     print('总耗时：%s' % (end - start))
# #     print('queue 结束大小 %d' % queue.qsize())
# #     print('result_queue 结束大小 %d' % result_queue.qsize())
#
#
# #
# # import re
# #
# # url  = 'https://music.163.com/#/album?id=64642342/1234123'
# # com_id = re.match(".*id=(\d+)", url)
# #
# # print(com_id.group(1))
#
#
#
#
# import json
# import random
#
# import requests
# import re
# from lxml import etree
# from bs4 import BeautifulSoup
# from save_wyy import formatData
# from wyy.wyy_function import is_Chinese, list_dict
#
#
#
#
# is_china = 0
#
# def get_total(id):
#     """ 获取评论数量 """
#     url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_{}'.format(id)
#     # print(url)
#     header = {
#         "Connection":"keep-alive",
#         "Pragma":"no-cache",
#         "Cache-Control":"no-cache",
#         "Accept":"text/javascript, text/html, application/xml, text/xml, */*",
#         "X-Requested-With":"XMLHttpRequest",
#         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
#                      "(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
#         "Content-Type":"application/x-www-form-urlencoded",
#         "Referer":"https://www.baidu.com/link?url=kl7W_qmAYRwjM_DK6s0yN5kMZ_f8OWS-7CeGK36oYly&wd=&eqid=be9ba1b30001d70d000000065db2a1e4",
#         "Accept-Encoding":"gzip, deflate, br",
#         "Accept-Language":"zh-CN,zh;q=0.9",
#     }
#     proxies = [
#         {'http':"http://117.169.78.54:16144"},{'http':"http://117.169.78.54:16038"},
#         {'http':"http://117.169.78.54:15164"},{'http':"http://117.169.78.54:17402"},
#         {'http':"http://114.239.249.87:46470"}, {'http':"http://124.132.212.178:25593"},
#         {'http':"http://171.80.152.56:43938"},{'http':"http://222.220.153.119:35973"},
#         {'http':"http://183.166.86.209:32342"}]
#     res = requests.get(url,headers=header)
#
#     # print(res.text)
#     json_res = json.loads(res.text)
#     return (json_res['total'])
#
#
#
#
#
#
#
#
#
# def get_intro(id):
#     """歌手简介"""
#     url = 'https://music.163.com/artist/desc?id={}'.format(id)
#     headers = {
#         "Connection":"keep-alive",
#         "Pragma":"no-cache",
#         "Cache-Control":"no-cache",
#         "Accept":"text/javascript, text/html, application/xml, text/xml, */*",
#         "X-Requested-With":"XMLHttpRequest",
#         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
#                      "(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
#         "Content-Type":"application/x-www-form-urlencoded",
#         "Referer":"https://music.163.com/",
#         "Accept-Encoding":"gzip, deflate, br",
#         "Accept-Language":"zh-CN,zh;q=0.9",
#     }
#     proxies = [
#         {'http':"http://117.94.183.226:"47312"},{'http':"http://115.223.125.187:29324"},
#         {'http':"http://183.7.171.16:45754"},{'http':"http://115.151.176.73:44622"},
#         {'http':"http://182.98.37.30:27432"},{'http':"http://117.169.78.54.178:17947"},
#         {'http':"http://117.169.78.54:14961"},{'http':"http://117.169.78.54.119:10822"},
#         {'http':"http://117.169.78.54:17127"}, {'http':"http://117.169.78.54:18230"}]


#     res = requests.get(url,headers=headers,proxies=random.choice(proxies))
#     tree = etree.HTML(res.text)
#     description = tree.xpath('//div[3]/div[1]/div/div/div[2]/div/p[1]/text()')
#     return description
#
#
#
# def get_homepage(id):
#     """主页信息"""
#     url = 'https://music.163.com/user/home?id={}'.format(id)
#     headers = {
#         "Connection":"keep-alive",
#         "Pragma":"no-cache",
#         "Cache-Control":"no-cache",
#         "Accept":"text/javascript, text/html, application/xml, text/xml, */*",
#         "X-Requested-With":"XMLHttpRequest",
#         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
#                      "(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
#         "Content-Type":"application/x-www-form-urlencoded",
#         "Referer":"https://music.163.com/",
#         "Accept-Encoding":"gzip, deflate, br",
#         "Accept-Language":"zh-CN,zh;q=0.9",
#     }
#     proxies = [
#         {'http':"http://117.169.78.54:16144"},{'http':"http://117.169.78.54:16038"},
#         {'http':"http://117.169.78.54:15164"},{'http':"http://117.169.78.54:17402"},
#         {'http':"http://114.239.249.87:46470"},{'http':"http://124.132.212.178:25593"},
#         {'http':"http://171.80.152.56:43938"},{'http':"http://222.220.153.119:35973"},
#         {'http':"http://183.166.86.209:32342"}]
#     res = requests.get(url,headers=headers,proxies=random.choice(proxies))
#     global is_china
#     tree = etree.HTML(res.text)
#     head_img = tree.xpath('//*[@id="ava"]/img/@src')  # 歌手图片
#
#     nickname = tree.xpath('//*[@id="j-name-wrap"]/span[1]/text()') # 歌手名字
#     print(nickname)
#     if is_Chinese(nickname[0]) == 1:
#         is_china = 1
#         print(is_china)
#     else:
#         is_china = 3
#         print(is_china)
#
#     tags = tree.xpath('//*[@id="head-box"]/dd/div[1]')  # 歌手标签
#     tag = ''
#     for item in tags[0][1:]:
#         tag += ((item.xpath('./text()')[1].strip()))
#
#     gender = tree.xpath('//*[@id="j-name-wrap"]/i/@class') # 歌手性别
#     gender = (re.findall(r'\d+',gender[0]))
#
#     dynamic_count = tree.xpath('//*[@id="event_count"]/text()') # 歌手动态数
#
#
#     follower_count = tree.xpath('//*[@id="follow_count"]/text()') # 歌手关注数
#
#
#     fans_count = tree.xpath('//*[@id="fan_count"]/text()') # 歌手粉丝数
#
#
#     region = tree.xpath('//*[@id="head-box"]/dd/div[3]/span/text()') # 歌手所在区域
#     if region == []:
#         region = ''
#     else:
#         region = region[0][5::]
#
#     introduce = tree.xpath('//*[@id="head-box"]/dd/div[2]/text()') # 歌手个人介绍
#     introduce = introduce[0][5::]
#
#     ul = tree.xpath('//*[@id="head-box"]/dd/div[4]/ul')
#     if ul == []:
#         other_contact = ''
#     else:
#         data_list = []
#         for item in ul[0]:
#             url = (item.xpath('./a/@href')[0])
#             name = (item.xpath('./a/@title')[0])
#             data = {
#                 name:url
#             }
#             data_list.append(data)
#         other_contact = list_dict(data_list)  # 歌手社交网络
#
#     return head_img,tag,gender,dynamic_count,follower_count,fans_count,region,nickname,introduce,other_contact,is_china

#
#
#
#
#
#
# def get_song(id,s_id):
#     """歌曲and专辑信息"""
#
#     url = 'https://music.163.com/album?id={}'.format(id)
#     headers = {
#         "Connection":"keep-alive",
#         "Pragma":"no-cache",
#         "Cache-Control":"no-cache",
#         "Accept":"text/javascript, text/html, application/xml, text/xml, */*",
#         "X-Requested-With":"XMLHttpRequest",
#         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
#                      "(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
#         "Content-Type":"application/x-www-form-urlencoded",
#         "Referer":"https://music.163.com/",
#         "Accept-Encoding":"gzip, deflate, br",
#         "Accept-Language":"zh-CN,zh;q=0.9",
#     }
#     proxies = [
#         {'http':"http://117.169.78.54:16144"},{'http':"http://117.169.78.54:16038"},
#         {'http':"http://117.169.78.54:15164"},{'http':"http://117.169.78.54:17402"},
#         {'http':"http://114.239.249.87:46470"},{'http':"http://124.132.212.178:25593"}
#         ,{'http':"http://171.80.152.56:43938"},{'http':"http://222.220.153.119:35973"},
#         {'http':"http://183.166.86.209:32342"}]
#     res = requests.get(url=url,headers=headers,proxies=random.choice(proxies))
#
#     album_id = id  # 专辑id
#     tree = etree.HTML(res.text)
#     artist_id = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[1]/span/a/@href') # 歌手id
#     artist_id = re.findall('\d+',artist_id[0])
#
#     '//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[1]'
#
#
#     album_name = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/h2/text()') # 专辑名
#
#     head_img = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[1]/img/@src') # 专辑url
#
#     singer =tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[1]/span/a/text()') # 专辑所属歌手
#
#     publish_time = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[2]/text()') # 专辑发行时间
#
#     publish_company = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[3]/text()') # 发行公司
#     if publish_company == []:
#         publish_company = ''
#     else:
#         publish_company = publish_company[0].strip()
#
#     share_count = tree.xpath('//*[@id="content-operation"]/a[4]/i/text()') # 专辑转发数
#     # print(share_count)
#     share_count_ = tree.xpath('//*[@id="content-operation"]/a[3]/i/text()')
#     # print(share_count_)
#
#     if is_Chinese(share_count) == 1:
#         share_count = 0
#
#     elif  share_count == ['下载']:
#         share_count = re.findall('\d+',share_count_[0])
#         share_count = share_count[0]
#     else:
#         share_count = re.findall('\d+',share_count[0])
#         share_count = share_count[0]
#
#     comment_count = tree.xpath('//*[@id="cnt_comment_count"]/text()') # 专辑评论数
#     if comment_count == ['评论']:
#         comment_count = 0
#     else:
#         comment_count = comment_count[0]
#     desc = tree.xpath('//*[@id="album-desc-more"]/p/text()') # 专辑说明
#     # print(desc)
#     data = {
#         'album_id':album_id,
#         'artist_id':artist_id[0],
#         'album_name':album_name[0],
#         'head_img':head_img[0],
#         'singer':singer[0],
#         'publish_time':publish_time[0],
#         'publish_company':publish_company,
#         'share_count':share_count,
#         'comment_count':comment_count,
#         'desc':formatData(str(desc)[1:-1:])}
#
#     print(data)
#     # save_result_album(data)
#
#     soup = BeautifulSoup(res.text, 'lxml')
#     textarea = (soup.find('textarea'))
#     textarea = textarea.text
#     if textarea.isspace() != True:
#         json_res = json.loads(textarea)
#         global is_china
#         for item in json_res:
#             if is_Chinese(item['name']) == True:
#                 is_china = 1
#
#             song_data = {
#                 'artist_id':item['artists'][0]['id'],
#                 'music_id':item['privilege']['id'],
#                 'mvid':item['mvid'],
#                 'name':item['name'],
#                 'comment_thread_id':item['commentThreadId'],
#                 'comment_count':get_total(item['privilege']['id']),
#                 'copyright_id':item['copyrightId'],
#                 'duration':item['duration'],
#                 'music_status':item['status'],
#                 'no':item['no'],
#                 'score':item['score'],
#                 'album_id':item['album']['id'],
#                 'album_name':item['album']['name'],
#                 'album_pic_url':item['album']['picUrl']
#             }
#             # save_result_song(song_data)
#         print(is_china)
#
#
#
#
#
#
# def album(s_id,n):
#     """专辑"""
#     url = 'https://music.163.com/artist/album?id=%d&limit=12&offset=%d'% (s_id,n)
#     headers = {
#         "Connection":"keep-alive",
#         "Pragma":"no-cache",
#         "Cache-Control":"no-cache",
#         "Accept":"text/javascript, text/html, application/xml, text/xml, */*",
#         "X-Requested-With":"XMLHttpRequest",
#         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
#                      "(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
#         "Content-Type":"application/x-www-form-urlencoded",
#         "Referer":"https://music.163.com/",
#         "Accept-Encoding":"gzip, deflate, br",
#         "Accept-Language":"zh-CN,zh;q=0.9",
#     }
#     proxies = [
#         {'http':"http://117.169.78.54:16144"},{'http':"http://117.169.78.54:16038"},
#         {'http':"http://117.169.78.54:15164"},{'http':"http://117.169.78.54:17402"},
#         {'http':"http://114.239.249.87:46470"},{'http':"http://124.132.212.178:25593"}
#         ,{'http':"http://171.80.152.56:43938"},{'http':"http://222.220.153.119:35973"},
#         {'http':"http://183.166.86.209:32342"}]
#     res = requests.get(url,headers=headers,proxies=random.choice(proxies))
#     soup = BeautifulSoup(res.text, 'lxml')
#     div = (soup.find_all(class_="m-cvrlst m-cvrlst-alb4 f-cb"))
#     if div == []:
#         return 'gg'
#     div = (str(div[0]))
#     soup = BeautifulSoup(div, 'lxml')
#     li = soup.find_all('li')
#     for item in li:
#         href = item.a['href']
#         id = re.findall('\d+',href)
#         id = id[0]
#         get_song(id,s_id)
#
#
#
#
# def get_introduce_user(id):
#     """user信息"""
#     url = 'https://music.163.com/artist?id={}'.format(id)
#     headers = {
#         "Connection":"keep-alive",
#         "Pragma":"no-cache",
#         "Cache-Control":"no-cache",
#         "Accept":"text/javascript, text/html, application/xml, text/xml, */*",
#         "X-Requested-With":"XMLHttpRequest",
#         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
#                      "(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
#         "Content-Type":"application/x-www-form-urlencoded",
#         "Referer":"https://music.163.com/",
#         "Accept-Encoding":"gzip, deflate, br",
#         "Accept-Language":"zh-CN,zh;q=0.9",
#     }
#     proxies = [
#         {'http':"http://117.169.78.54:16144"},{'http':"http://117.169.78.54:16038"},
#         {'http':"http://117.169.78.54:15164"},{'http':"http://117.169.78.54:17402"},
#         {'http':"http://114.239.249.87:46470"},{'http':"http://124.132.212.178:25593"}
#         ,{'http':"http://171.80.152.56:43938"},{'http':"http://222.220.153.119:35973"},
#         {'http':"http://183.166.86.209:32342"}]
#     res = requests.get(url,headers=headers,proxies=random.choice(proxies))
#     # print(res.text)
#     tree = etree.HTML(res.text)
#     # print(tree)
#     home_url = tree.xpath('//*[@id="artist-home"]/@href')
#
#     artist_id = id  # artist id
#     global user_id,is_china
#     if home_url == [] or home_url == None:
#
#         nickname = tree.xpath('//*[@id="artist-name"]/text()') # user 名字
#
#         if nickname ==  []:
#             return '没有相关歌手'
#         if is_Chinese(nickname[0]) == True:   # 是否中文名字
#             is_china = 1
#             print(is_china)
#         else:
#             is_china = 3
#             print(is_china)
#
#
#
#
#         description = get_intro(id) # user 简介
#         if description == []:
#             description = ''
#         else:
#             description = description[0]
#
#         page = 0
#         while True:
#             result = album(id,page)
#             if result == 'gg':
#                 break
#             page += 12
#
#         data = {
#             "artist_id":artist_id,
#             "nickname":nickname[0],
#             "description":description,
#             "is_china":is_china
#         }
#         print(data)
#         # save_result_user_to(data)
#


# a = tree.xpath('//*[@class="topblk"]')
# for i in a[0][1::2]:
#     artist_id = i.xpath('./span/a/@href')
#     artist_id = re.findall('\d+', (artist_id))
#     print(artist_id)
#
#
# artist_id = artist_id[0]
# print(artist_id[0],'=======================================',id,album_name)


#
#     # 有个人主页模块
#     else:
#         user_id = re.findall('\d+',home_url[0])  # user id
#
#         soup = BeautifulSoup(res.text, 'lxml')
#         name = soup.find('title')
#         # print(name.text)
#         head_img,tag,gender,dynamic_count,follower_count,fans_count,region,nickname,introduce,other_contact,is_china = \
#         get_homepage(user_id[0])
#
#         description = get_intro(id)
#         if description == []:
#             description = ''
#         else:
#             description = description[0]
#
#         page = 0
#         while True:
#             result = album(id,page)
#             if result == 'gg':
#                 break
#             page += 12
#
#
#
#
#         data = {
#             "artist_id":artist_id,
#             "user_id":user_id[0],
#             "nickname":nickname[0],
#             "description":formatData(description),
#             "home_url":home_url[0],
#             "head_img":str(head_img[0]),
#             "tag":str(tag),
#             "gender":str(gender[0])[1],
#             "dynamic_count":dynamic_count[0],
#             "follower_count":follower_count[0],
#             "fans_count":fans_count[0],
#             "region":str(region),
#             "other_contact":other_contact,
#             "introduce":introduce,
#             "is_china":is_china
#         }
#
#         print( data)
#         # save_result_user(data)
#
#
#
#
#
# get_introduce_user(14594)
#
# # music_id = 2294
# #
# #
# # while True:
# #     result = get_introduce_user(music_id)
# #     print(result,music_id)
# #     music_id+=1
#
#
#
# soup = BeautifulSoup(res.text, 'lxml')
# div = (soup.find_all(class_="topblk"))
# # print(div)
#
# if div == []:
#     return 'gg'
# div = (str(div[0]))
# # print(div)
# soup = BeautifulSoup(div, 'lxml')
# li = soup.find_all(class_="intr")
# print(li)
# for item in li:
#     # href = item.a['href']
#     # id = re.findall('\d+',href)
#     # id = id[0]
#     # # get_song(id,s_id)
#     #
#     # print(href,id)
#     print(item.text)
#
# def album(s_id,):
#     """专辑"""
#     headers = {
#         "Connection": "keep-alive",
#         "Pragma": "no-cache",
#         "Cache-Control": "no-cache",
#         "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
#         "X-Requested-With": "XMLHttpRequest",
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
#                       "(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Referer": "https://music.163.com/",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "zh-CN,zh;q=0.9",
#     }
#     while True:
#         ip = getProxy()
#         if verifyProxy(ip) == 200:
#             proxies =  {'https': ip}
#             # print(proxies)
#             break
#     page = 0
#     while True:
#         url = 'https://music.163.com/artist/album?id=%d&limit=12&offset=%d' % (s_id,page)
#         print(url)
#         res = requests.get(url=url, headers=headers, proxies=proxies)
#         soup = BeautifulSoup(res.text, 'lxml')
#         div = (soup.find_all(class_="m-cvrlst m-cvrlst-alb4 f-cb"))
#         if div == []:
#             return 'gg'
#         div = (str(div[0]))
#         soup = BeautifulSoup(div, 'lxml')
#         li = soup.find_all('li')
#         for item in li:
#             href = item.a['href']
#             id = re.findall('\d+', href)
#             id = id[0]
#
#             get_song(id,s_id)
#         if div == []:
#             break
#         page += 12
import json
import random

import pymysql
import requests
from fake_useragent import UserAgent

ua = UserAgent()


def get_total(id):
    """ 获取评论数量 """
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_{}'.format(id)
    # print(url)
    ua = UserAgent()
    header = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        'Accept': "*/*",
        "X-Requested-With": "XMLHttpRequest",
        # "User-Agent":ua.random,
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://music.163.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        # "Cookie":'_ntes_nuid=d23b1d0234a58749f15b03e3bfe800b4; mail_psc_fingerprint=0e5026d42e9dc4343ed55c4612ba7712; __gads=ID=1150016c9b65a074:T=1514275689:S=ALNI_MZ_ov9YC_Ox90BxIUGsqK4O8mI8Lw; vjuids=-20cd41793.16091dd6697.0.c246624090236; _ga=GA1.2.698481114.1514784364; nts_mail_user=shishi843694650@163.com:-1:1; __utma=187553192.698481114.1514784364.1540529010.1540804191.16; _ntes_nnid=d23b1d0234a58749f15b03e3bfe800b4,1547099471069; vjlast=1514275694.1549085249.21; P_INFO=shishi19910601@163.com|1550373835|0|ecard|00&99|sic&1550244254&xyq#sic&510100#10#0#0|&0|ecard&xyq_qrcode&xyq|shishi19910601@163.com; vinfo_n_f_l_n3=7fc96fbc3e916451.1.39.1514275694267.1561004832879.1561103748087; WM_TID=qKHLfIYIXi%2F4ECyHyn5P5LXGc6zqYatX; hb_MA-BFF5-63705950A31C_source=www.baidu.com; playerid=25512680; WM_NI=CGUjgkXbnY7X9uXntZTY4qfa%2FLk9xsPA7dcqZmLO6jz33WVGsYU2P7KOxxOREB0Yt%2B6xd1HZJ6XPC68J2nocnzvChcdHjSlRgTsa3PR30%2FgK2kaNVr4%2FXu%2FXuLWNLGwlYmw%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eebaf645ad8eafd5c64392bc8ab6c44b978b8b85f27f92ecfe84c141f7b8faa3ee2af0fea7c3b92a81999b8be6619cbea2bab654fbab988ff7529887fc92e56bed94a5dafb79949ff985e27b9ab384b0b562baedfdb8d54db1879bd3d33d8991b899ce5a879e00baf721f6a8acd2cb528aea98b1c23efc96fe8fee69aea6baa4eb69a898a6b4ef5aa58cbd82b25c92ed00d0e641f2b5afafd57af8f19896ae54b79499afcf4db5b4978ef637e2a3; _iuqxldmzr_=32; __remember_me=true; ntes_kaola_ad=1; MUSIC_U=79babd6bce35dd249f65fbdd2a6c596cd2a2e65844ec8b5d22c641508cb2e4b7f7ec07408b132b30bde5712085af36fd30b1b8726de9d20bdc74b1d4c93de86140696f5875abc324bf122d59fa1ed6a2; __csrf=fd4f2f7a7bc0364ef5672319d0ac9524; JSESSIONID-WYYY=UhhVhOUSEWi4upWw3gbuRsCmYeWpAx0upkgQbf9obGCPCD2Y%2Fiq3YEcwzX4qnw%2BopCsPaDsSDS0YC3gAS7sahyqssnBOFXX2pBYIB6bH6TwPTywhdU%2Fo1E2UTj0Ptn3t9qgJJey7o6cjGUz3qaHZ34rXJyN%2BgJBWbYNzYJqIEHiSeI1I%3A1572922843570'

    }
    # header = {
    # "Host": "music.163.com",
    # "Connection": "keep-alive",
    # "Cache-Control":"max-age=0",
    # "Upgrade-Insecure-Requests": "1",
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate",
    # "Accept-Language": "zh-CN,zh;q=0.9"
    #
    # }
    # print(header["User-Agent"])
    # while True:
    #     ip = getProxy()
    #     if verifyProxy(ip) == 200:
    #         proxies =  {'https': ip}
    #         # print(proxies)
    #         break


#     while True:
#         res = requests.get(url, headers=header)
#         print(res.text)
#         json_res = json.loads(res.text)
#         if ['code'] == 200:
#             break
#         print(id,json_res)
#     return (json_res['total'])
#
#
# get_total(565713207)
# # print(ua.random)
headers = {
    "Host": "cn.bykszb.com",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "content-type": "application/x-www-form-urlencoded",
    "Referer": "https://servicewechat.com/wxa54043f6082835a1/48/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br",

    # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat"
}


def get_info(id):
    con = {}
    url = 'https://cn.bykszb.com/app/index.php?i=2&t=0&v=1.8.37&from=wxapp&c=entry&a=wxapp&do=ApiGetTelInfo&state=we7sid-76d696100681f9a539366d8fd1d93257&sign=4a4ea61bef88e338a797a0aef02e0803&m=amouse_tel114&id={}'.format(
        id)
    print(url)
    proxies = [{'ip': '117.169.78.54', 'port': '18291'}, {'ip': '117.169.78.54', 'port': '15440'},
               {'ip': '117.169.78.54', 'port': '19798'}, {'ip': '117.169.78.54', 'port': '19997'},
               {'ip': '117.169.78.54', 'port': '10536'}, {'ip': '60.185.150.59', 'port': '41968'},
               {'ip': '114.227.161.2', 'port': '28363'}, {'ip': '27.191.65.80', 'port': '26926'},
               {'ip': '117.90.4.248', 'port': '45354'}, {'ip': '59.173.53.47', 'port': '28471'}]

    res = requests.get(url, headers=headers)
    # res = requests.get(url, headers=headers, proxies=random.choice(proxies))
    print(res.text)
    data = json.loads(res.text)
    data = data["data"]
    view = data["view"]
    if view == 1:
        return
    con["id"] = (data["id"])
    con["openid"] = data["openid"]
    con["title"] = data["title"]
    con["contact_name"] = data["contact_name"]
    con["info"] = data["info"]
    con["weixin"] = data["weixin"]
    con["logo"] = data["logo"]
    con["mobile"] = data["mobile"]
    con["place"] = data["place"]
    con["cate_title"] = data["cate_title"]
    print(con)


# res = requests.get('http://115.29.174.137:3333/xdn/proxies/get?count=10&type=0&all=0')
# proxies_list = json.loads(res.text)

# print(proxies)
# get_info(131802)


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



def formatData(data):
    """处理sql字符串引号"""
    if(data == None or data == ''):
        return  ""
    data=data.replace("'","\\\'")
    return  data.replace('"','\\\"')



def save_result_album(data):
    """储存专辑信息"""
    try:
        conn = get_conn()
        # print(item)
        # name 关键字 用`name
        # {'album_id': '80535308', 'artist_id': '1873', 'album_name': '火火的歌', 'head_img': 'http://p2.music.126.net/PAlBviJ_B9j3Hm91SDzhjw==/109951164236701524.jpg?param=177y177', 'singer': '阿宝', 'publish_time': '2019-07-21', 'publish_company': '\n墨枫文化\n', 'share_count': '', 'comment_count': '1', 'desc': ''}

        sql = f'insert ignore into  acq_kszb ' \
              f'(uid,open_id,title,contact_name,info,weixin,logo,mobile,place,cate_title)' \
              f'values ("{data["id"]}", "{data["openid"]}","{data["title"]}", "{data["contact_name"]}", ' \
              f'"{data["info"]}", "{data["weixin"]}", "{data["logo"]}", "{data["mobile"]}","{data["cate_title"]}",' \
              f' "{data["place"]}")'
        # print(sql)
        execute_sql(sql,conn)
        close_conn(conn)
    except Exception as e:
        print(e)


provinces = {
    '吉林省': [125.326800, 43.896160], '黑龙江省': [126.662850, 45.742080],
    '辽宁省': [123.429250, 41.835710], '内蒙古自治区': [111.765220, 40.817330],
    '新疆维吾尔自治区': [87.627100, 43.793430], '青海省': [101.780110, 36.620870],
    '北京市': [116.407170, 39.904690], '天津市': [117.199370, 39.085100],
    '上海市': [121.473700, 31.230370], '重庆市': [106.550730, 29.564710],
    '河北省': [114.469790, 38.035990], '河南省': [113.753220, 34.765710],
    '陕西省': [108.954240, 34.264860], '江苏省': [118.762950, 32.060710],
    '山东省': [117.020760, 36.668260], '山西省': [112.562720, 37.873430],
    '甘肃省': [103.826340, 36.059420], '宁夏回族自治区': [106.258670, 38.471170],
    '四川省': [104.075720, 30.650890], '西藏自治区': [91.117480, 29.647250],
    '安徽省': [117.285650, 31.861570], '浙江省': [120.153600, 30.265550],
    '湖北省': [114.342340, 30.545390], '湖南省': [112.983400, 28.112660],
    '福建省': [119.296590, 26.099820], '江西省': [115.910040, 28.674170],
    '贵州省': [106.707220, 26.598200], '云南省': [102.709730, 25.045300],
    '广东省': [113.266270, 23.131710], '广西壮族自治区': [108.327540, 22.815210],
    '香港': [114.165460, 22.275340], '澳门': [113.549130, 22.198750],
    '海南省': [110.348630, 20.019970], '台湾省': [121.520076, 25.030724],
}






def get_data(x,y,page):
    # url = 'https://cn.bykszb.com/app/index.php?i=2&t=0&v=1.8.37&from=wxapp&c=entry&a=wxapp&do=ApiQueryTelList&state=we7sid-76d696100681f9a539366d8fd1d93257&sign=09f5b2c28596d9953bac6c6d9ddeaa99&type=1&lat={}&lng={}&m=amouse_tel114&pageIndex={}'.format(x,y,page)
    url = 'https://cn.bykszb.com/app/index.php?i=2&t=0&v=1.8.37&from=wxapp&c=entry&a=wxapp&do=ApiGetTelInfo&state=we7sid-bf42856f4bcd80270266b3f7aa701250&sign=43f725eafdc0d0805972c5b7b60881e5&m=amouse_tel114&id={}'.format(page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat"
    }
    res = requests.get(url, headers=headers)
    print(res.text)
    data = json.loads(res.text)
    lists = data["data"]["list"]
    if lists == []:
        return '0'
    data = {}
    for item in lists:
        data["id"] = (item["id"])
        data["openid"] = item["openid"]
        data["title"] = item["title"]
        data["contact_name"] = item["contact_name"]
        data["info"] = item["info"]
        data["weixin"] = item["weixin"]
        data["logo"] = item["logo"]
        data["mobile"] = item["mobile"]
        data["place"] = item["place"]
        data["cate_title"] = item["cate_title"]
        # save_result_album(data)


def get_con(value):
    for item in range(100):
        print(item)
        a = get_data(item,value[1],value[0])
        if a == "0":
            break

# for key,value in provinces.items():
#     get_con(value)
#     print(key,value)

get_data(10000,32,6354)

