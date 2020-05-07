# album_id = id
# # print(id)
#
#
#
# tree = etree.HTML(res.text)
# name = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/h2/text()')
# # print(name)
#
# song_name = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[1]/span/@title')
# print(song_name)
#
#
# img = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[1]/img/@src')
# # print(img)
# time = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[2]/text()')
# # print(time)
#
# company = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[3]/text()')
# # print(company)
#
# share = tree.xpath('//*[@id="content-operation"]/a[4]/i/text()')
# # print(share)
#
# comment = tree.xpath('//*[@id="cnt_comment_count"]/text()')
# # print(comment)
#
#
# desc = tree.xpath('//*[@id="album-desc-more"]/p/text()')
# print(album_id,s_id,name,song_name,img,time,company,share,comment,desc)
#
#
# data = {
#     'album_id':album_id,
#     'artist_id':artist_id[0],
#     'album_name':album_name[0],
#     'head_img':head_img[0],
#     'singer':singer[0],
#     'publish_time':publish_time[0],
#     'publish_company':publish_company[0],
#     'share_count':share_count[0],
#     'comment_count':comment_count[0],
#     'desc':desc[0]
#
# }



def get_album(id):
    """专辑"""
    url = 'https://music.163.com/album?id={}'.format(id)
    headers = {
        "Connection":"keep-alive",
        "Pragma":"no-cache",
        "Cache-Control":"no-cache",
        "Accept":"text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With":"XMLHttpRequest",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                     "(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded",
        "Referer":"https://music.163.com/",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.9",
    }
    proxies = [
        {'http':"http://117.169.78.54:16144"}, {'http':"http://117.169.78.54:16038"},
        {'http':"http://117.169.78.54:15164"},{'http':"http://117.169.78.54:17402"},
        {'http':"http://114.239.249.87:46470"}, {'http':"http://124.132.212.178:25593"},
        {'http':"http://171.80.152.56:43938"},{'http':"http://222.220.153.119:35973"},
        {'http':"http://183.166.86.209:32342"}]
    res = requests.get(url=url,headers=headers,proxies=random.choice(proxies))
    # print(res.text)
    album_id = id
    tree = etree.HTML(res.text)
    artist_id = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[1]/span/a/@href')
    artist_id = re.findall('\d+',artist_id[0])
    # print(artist_id)
    album_name = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/h2/text()')
    # print(album_name)
    head_img = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[1]/img/@src')
    # print(head_img)
    singer =tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[1]/span/a/text()')
    # print(singer)
    publish_time = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[2]/text()')
    # print(publish_time)
    publish_company = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[3]/text()')
    # if publish_company != None or publish_company != []:
    # publish_company = re.findall(u"[\u4e00-\u9fa5]+",publish_company[0])
    # print(publish_company)
    share_count = tree.xpath('//*[@id="content-operation"]/a[4]/i/text()')
    share_count = re.findall('\d+',share_count[0])
    # print(share_count)
    comment_count = tree.xpath('//*[@id="cnt_comment_count"]/text()')
    # print(comment_count)
    desc = tree.xpath('//*[@id="album-desc-dot"]/p/text()')
    # print(desc)
    data = {
        'album_id':album_id,
        'artist_id':artist_id[0],
        'album_name':album_name[0],
        'head_img':head_img[0],
        'singer':singer[0],
        'publish_time':publish_time[0],
        'publish_company':publish_company[0],
        'share_count':share_count[0],
        'comment_count':comment_count[0],
        'desc':desc[0]

    }
    print(data)
    return data



def  get_music_data(id):
    """歌曲内容"""

    url = 'https://music.163.com/song?id={}'.format(id)
    header = {
        "Connection":"keep-alive",
        "Pragma":"no-cache",
        "Cache-Control":"no-cache",
        "Accept":"text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With":"XMLHttpRequest",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                     "(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded",
        "Referer":"https://www.baidu.com/link?url=kl7W_qmAYRwjM_DK6s0yN5kMZ_f8OWS-7CeGK36oYly&wd=&eqid=be9ba1b30001d70d000000065db2a1e4",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.9",
    }

    proxies = [
        {'http':"http://117.169.78.54:16144"},
        {'http':"http://117.169.78.54:16038"},
        {'http':"http://117.169.78.54:15164"},
        {'http':"http://117.169.78.54:17402"},
        {'http':"http://114.239.249.87:46470"},
        {'http':"http://124.132.212.178:25593"},
        {'http':"http://171.80.152.56:43938"},
        {'http':"http://222.220.153.119:35973"},
        {'http':"http://183.166.86.209:32342"}]
    res = requests.get(url,headers=header,proxies=random.choice(proxies))

    # res.encoding = 'utf-8'
    # print(res.text)
    tree = etree.HTML(res.text)
    # print(tree)

    music_name = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div/em/text()')
    # print(music_name) # 歌曲名

    name = tree.xpath('//p/span/a/text()')
    # print(name) # 歌手名

    album = tree.xpath('//div[1]/div[2]/p[2]/a/text()')
    # print(album) # 专辑名


    homepage_str = tree.xpath('//p/span/a/@href') # 歌手主页id
    # print(homepage_str)

    homepage = re.findall(r'\d+', homepage_str[0])
    # print(homepage)



    total = get_total(id)  # 评论数量
    print(music_name,name,album,homepage,total)

# get_data(483671599)

# import json
# import random
# import threading
#
# import requests
# import re
# from lxml import etree
# from bs4 import BeautifulSoup
# from save_wyy import save_result_user, save_result_song, save_result_album, formatData, save_result_user_to
# from wyy_function import is_Chinese, list_dict
#
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
#         {'http':"http://117.169.78.54:16144"},{'http':"http://117.169.78.54:16038"},
#         {'http':"http://117.169.78.54:15164"},{'http':"http://117.169.78.54:17402"},
#         {'http':"http://114.239.249.87:46470"},{'http':"http://124.132.212.178:25593"},
#         {'http':"http://171.80.152.56:43938"},{'http':"http://222.220.153.119:35973"},
#         {'http':"http://183.166.86.209:32342"}]
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
#     nickname = tree.xpath('//*[@id="j-name-wrap"]/span[1]/text()') # 歌手名字
#     if is_Chinese(nickname) == 1:
#         is_china = 1
#     else:
#         is_china = 3
#     tags = tree.xpath('//*[@id="head-box"]/dd/div[1]')  # 歌手标签
#     tag = ''
#     for item in tags[0][1:]:
#         tag += ((item.xpath('./text()')[1].strip()))
#
#     gender = tree.xpath('//*[@id="j-name-wrap"]/i/@class') # 歌手性别
#
#     gender = (re.findall(r'\d+',gender[0]))
#
#     dynamic_count = tree.xpath('//*[@id="event_count"]/text()')
#
#
#     follower_count = tree.xpath('//*[@id="follow_count"]/text()')
#
#
#     fans_count = tree.xpath('//*[@id="fan_count"]/text()')
#
#
#     region = tree.xpath('//*[@id="head-box"]/dd/div[3]/span/text()')
#     if region == []:
#         region = ''
#     else:
#         region = region[0][5::]
#
#     introduce = tree.xpath('//*[@id="head-box"]/dd/div[2]/text()')
#     introduce = introduce[0][5::]
#
#     ul = tree.xpath('//*[@id="head-box"]/dd/div[4]/ul')
#
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
#         other_contact = list_dict(data_list)
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
#     album_id = id
#     tree = etree.HTML(res.text)
#     artist_id = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[1]/span/a/@href')
#     artist_id = re.findall('\d+',artist_id[0])
#
#     album_name = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/h2/text()')
#
#     head_img = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[1]/img/@src')
#
#     singer =tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[1]/span/a/text()')
#
#     publish_time = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[2]/text()')
#
#     publish_company = tree.xpath('//div[3]/div[1]/div/div/div[1]/div[2]/div/div[1]/p[3]/text()')
#     if publish_company == []:
#         publish_company = ''
#     else:
#         publish_company = publish_company[0].strip()
#
#     share_count = tree.xpath('//*[@id="content-operation"]/a[4]/i/text()')
#     share_count_ = tree.xpath('//*[@id="content-operation"]/a[3]/i/text()')
#
#     # print(share_count)
#     if share_count == ['分享'] or share_count == []:
#         share_count = 0
#     elif  share_count == ['下载']:
#         share_count = re.findall('\d+',share_count_[0])
#         # print(share_count)
#         share_count = share_count[0]
#
#     else:
#         share_count = re.findall('\d+',share_count[0])
#         # print(share_count)
#         share_count = share_count[0]
#         # print(share_count)
#     # print(share_count)
#     comment_count = tree.xpath('//*[@id="cnt_comment_count"]/text()')
#     if comment_count == ['评论']:
#         comment_count = 0
#     else:
#         comment_count = comment_count[0]
#     desc = tree.xpath('//*[@id="album-desc-more"]/p/text()')
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
#         'desc':formatData(str(desc)[1:-1:])
#
#     }
#     print(data)
#     save_result_album(data)
#
#
#     soup = BeautifulSoup(res.text, 'lxml')
#     textarea = (soup.find('textarea'))
#     textarea = textarea.text
#     # print(textarea)
#     json_res = json.loads(textarea)
#     # print(json_res)
#     global is_china
#     for item in json_res:
#         if is_Chinese(item['name']) == 1:
#             is_china = 1
#         song_data = {
#             'artist_id':item['artists'][0]['id'],
#             'music_id':item['privilege']['id'],
#             'mvid':item['mvid'],
#             'name':item['name'],
#             'comment_thread_id':item['commentThreadId'],
#             'comment_count':get_total(item['privilege']['id']),
#             'copyright_id':item['copyrightId'],
#             'duration':item['duration'],
#             'music_status':item['status'],
#             'no':item['no'],
#             'score':item['score'],
#             'album_id':item['album']['id'],
#             'album_name':item['album']['name'],
#             'album_pic_url':item['album']['picUrl']
#         }
#         save_result_song(song_data)
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
#     # print(res.text)
#
#     tree = etree.HTML(res.text)
#
#
#     soup = BeautifulSoup(res.text, 'lxml')
#     # print(soup.find_all(class_="u-cover u-cover-alb3"))
#     div = (soup.find_all(class_="m-cvrlst m-cvrlst-alb4 f-cb"))
#     if div == []:
#         return 'gg'
#     # print(div)
#     div = (str(div[0]))
#     # print(type(div))
#     soup = BeautifulSoup(div, 'lxml')
#     li = soup.find_all('li')
#     # print(li)
#     for item in li:
#         img = item.img['src']
#         href = item.a['href']
#         title = item.div['title']
#         time = soup.find('span')
#         time = (time.string)
#         id = re.findall('\d+',href)
#         id = id[0]
#
#         data = {
#             'img':img,
#             'id':id,
#             'href':href,
#             'title':title,
#             'time':time
#         }
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
#     global user_id
#     if home_url == [] or home_url == None:
#         nickname = tree.xpath('//*[@id="artist-name"]/text()') # user 名字
#         if is_Chinese(nickname) == 1:   # 是否中文名字
#             is_china = 1
#         else:
#             is_china = 3
#         if nickname ==  []:
#             return '没有相关歌手'
#         description = get_intro(id) # user 简介
#         if description == []:
#             description = ''
#         else:
#             description = description[0]
#
#         n = 0
#         while True:
#             try:
#                 result = album(id,n)
#                 if result == 'gg':
#                     break
#                 n+=12
#             except EOFError as  e:
#                 print(e)
#                 break
#
#
#         data = {
#             "artist_id":artist_id,
#             "nickname":nickname[0],
#             "description":description,
#             "is_china":is_china
#         }
#         print(data)
#         save_result_user_to(data)
#
#
#
#     # 有个人主页模块
#     else:
#         user_id = re.findall('\d+',home_url[0])  # user id
#
#         soup = BeautifulSoup(res.text, 'lxml')
#         name = soup.find('title')
#         # print(name.text)
#         head_img,tag,gender,dynamic_count,follower_count,fans_count,region,nickname,introduce,other_contact,is_china = \
#             get_homepage(user_id[0])
#
#         description = get_intro(id)
#         if description == []:
#             description = ''
#         else:
#             description = description[0]
#
#         n = 0
#         while True:
#             try:
#                 result = album(id,n)
#                 if result == 'gg':
#                     break
#                 n+=12
#             except EOFError as  e:
#                 print(e)
#                 break
#         data = {
#             "artist_id":artist_id,
#             "user_id":user_id[0],
#             "nickname":nickname[0],
#             "description":description,
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
#         save_result_user(data)
#
#
#
# music_id = 85388
#
# while True:
#     result = get_introduce_user(music_id)
#     print(result,music_id)
#     music_id+=1
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # def f():
# #     for i in range(1877,999999999):
# #         result = get_introduce_user(i)
# #         print(result,i)
#
#
#
#
#
#
#
#
#
# #
# # result = get_introduce_user(1876)
#
#
#
#
# # def main():
# #     threads = [threading.Thread(target=f) for _ in range(8)]
# #
# #     for thread in threads:
# #         thread.start()
# #
# #     for thread in threads:
# #         thread.join()
#
#
# # t_1 = threading.Thread(target=f())
# # t_1.start()
# # t_1.join()
# # t_2 = threading.Thread(target=f())
# # t_2.start()
# # t_2.join()
# # t_3 = threading.Thread(target=f())
# # t_3.start()
# # t_3.join()
# # t_4 = threading.Thread(target=f())
# # t_4.start()
# # t_4.join()
# # t_5 = threading.Thread(target=f())
# # t_5.start()
# # t_5.join()
#
#
#
#
#
# #
# # if __name__ == '__main__':
# #     main()
# #














