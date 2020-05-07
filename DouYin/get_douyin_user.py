import queue
import threading

import requests

# url = 'https://api.weibo.cn/2/profile?networktype=wifi&user_domain=6036995098'
# url = 'https://m.weibo.cn/profile/6099970126'

# res = requests.get(url,headers=header)
# # print(res.text)
#
# url = 'https://www.iesdouyin.com/share/user/70013225676'
#
# header = {
#     "User-Agent": "com.ss.android.ugc.aweme/911 (Linux; U; Android 5.1.1; zh_CN; OPPO R11; Build/NMF26X; Cronet/TTNetVersion:4df3ca9d 2019-11-25)"
#
# }
#
# res = requests.get(url, headers=header)
# print(res.text)

import re
import requests
from lxml import etree

'''
                         抖音用户基本信息 -> 请求share来获取数据
'''


def handle_decode(input_data):
    # 匹配icon font
    regex_list = [
        {'name': [' &#xe603; ', ' &#xe60d; ', ' &#xe616; '], 'value': 0},
        {'name': [' &#xe602; ', ' &#xe60e; ', ' &#xe618; '], 'value': 1},
        {'name': [' &#xe605; ', ' &#xe610; ', ' &#xe617; '], 'value': 2},
        {'name': [' &#xe604; ', ' &#xe611; ', ' &#xe61a; '], 'value': 3},
        {'name': [' &#xe606; ', ' &#xe60c; ', ' &#xe619; '], 'value': 4},
        {'name': [' &#xe607; ', ' &#xe60f; ', ' &#xe61b; '], 'value': 5},
        {'name': [' &#xe608; ', ' &#xe612; ', ' &#xe61f; '], 'value': 6},
        {'name': [' &#xe60a; ', ' &#xe613; ', ' &#xe61c; '], 'value': 7},
        {'name': [' &#xe60b; ', ' &#xe614; ', ' &#xe61d; '], 'value': 8},
        {'name': [' &#xe609; ', ' &#xe615; ', ' &#xe61e; '], 'value': 9},
    ]

    for i1 in regex_list:
        for i2 in i1['name']:
            input_data = re.sub(i2, str(i1['value']), input_data)  # 把正确value替换到自定义字体上
    html = etree.HTML(input_data)
    douyin_info = {}
    # 获取昵称
    try:
        douyin_info['nick_name'] = \
            html.xpath("//div[@class='personal-card']/div[@class='info1']//p[@class='nickname']/text()")[0]
        # 获取抖音ID
        douyin_id = html.xpath("//div[@class='personal-card']/div[@class='info1']/p[@class='shortid']//text()")
        douyin_info['douyin_id'] = ''.join(douyin_id).replace('抖音ID：', '').replace(' ', '')

        # 职位类型
        try:
            douyin_info['job'] = html.xpath(
                "//div[@class='personal-card']/div[@class='info2']/div[@class='verify-info']/span[@class='info']/text()")[
                0].strip()
        except:
            pass
        # 描述
        douyin_info['describe'] = \
            html.xpath("//div[@class='personal-card']/div[@class='info2']/p[@class='signature']/text()")[0].replace('\n',
                                                                                                                    ',')
        # 关注
        douyin_info['follow_count'] = html.xpath(
            "//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='focus block']//i[@class='icon iconfont follow-num']/text()")[
            0].strip()
        # 粉丝
        fans_value = ''.join(html.xpath(
            "//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='follower block']//i[@class='icon iconfont follow-num']/text()"))
        unit = html.xpath(
            "//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='follower block']/span[@class='num']/text()")
    except:
        return
    if unit[-1].strip() == 'w':
        douyin_info['fans'] = str(float(fans_value) / 10) + 'w'
    else:
        douyin_info['fans'] = fans_value
    # 点赞
    like = ''.join(html.xpath(
        "//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='liked-num block']//i[@class='icon iconfont follow-num']/text()"))
    unit = html.xpath(
        "//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='liked-num block']/span[@class='num']/text()")
    if unit[-1].strip() == 'w':
        douyin_info['like'] = str(float(like) / 10) + 'w'
    else:
        douyin_info['like'] = like

    return douyin_info


def handle_douyin_info(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    response = requests.get(url=url, headers=header)
    # print(response.text)
    data =  handle_decode(response.text)
    if data != None:
        file_handle=open('1.txt',mode='a')
        file_handle.write(url)
        file_handle.write('\r\n')




q = queue.Queue()


def Producer():
    id = 6000025256
    while True:
        url = 'https://www.iesdouyin.com/share/user/{}'.format(id)
        q.put(url)
        id += 1


def Consumer():
    '''消费者'''
    while True:
        i = q.get()  # 从队列中取数据
        print(i)
        print(handle_douyin_info(i))
        # time.sleep(1)


def main():
    p = threading.Thread(target=Producer)
    threads = [threading.Thread(target=Consumer) for _ in range(30)]
    for thread in threads:
        thread.start()
    p.start()
    for thread in threads:
        thread.join()

    #
    # id = 70013225676
    #
    # while True:
    #     url = 'https://www.iesdouyin.com/share/user/{}'.format(id)
    #     id+=1
    #     print(handle_douyin_info(url))
if __name__ == '__main__':
    main()
    # id = 70013225676
    # url = 'https://www.iesdouyin.com/share/user/{}'.format(id)
    # print(url)
    # print(handle_douyin_info(url))