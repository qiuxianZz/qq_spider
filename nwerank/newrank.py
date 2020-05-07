import threading
import time

import requests
import execjs
import re


def newrank(id):
    """内容"""
    url = 'https://edit.newrank.cn/xdnphb/editor/article/getEditorArticleById'

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    nonce,xyz = nonce_xyz(id)
    # print(nonce,xyz)
    data = {
        "article_uuid": id,
        "nonce": nonce,
        "xyz": xyz
    }

    response = requests.post(url=url, data=data, headers=headers)

    result = response.text

    return result




def nonce_xyz(uuid):
    # 读取js文件
    with open('newrank.js', encoding='utf-8') as f:
        js = f.read()
    # 通过compile命令转成一个js对象
    docjs = execjs.compile(js)
    res = docjs.call('nonce')
    xyz = docjs.call('xyz','/xdnphb/editor/article/getEditorArticleById?AppKey=joker&article_uuid=%s&nonce=%s'% (uuid,res))
    return res,xyz







def new_rank(num,nonce,xyz):
    """id"""
    url = 'https://www.newrank.cn/xdnphb/index/getMedia'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    data= {
    "keyword":'',
    "pageNumber": num,
    "pageSize": 10,
    "nonce":nonce ,
    "xyz": xyz
    }
    r = requests.post(url=url,headers=headers,data=data)
    patterns = re.compile('"article_uuid":"(.*?)","author"',re.S)
    result = patterns.findall(r.text)
    return result

# uuids = new_rank()

# result = newrank(id='0735DFFACAF9AE27B1B9D7A2D612FA3B')
# print(result)

# for item in range(len(new_rank())):
#     print(newrank(new_rank()[item]))


def uuid_f(num):
    """所有文章id"""
    # 调用本地js
    with open('newrank.js', encoding='utf-8') as f:
        js = f.read()
    # 通过compile命令转成一个js对象
    docjs = execjs.compile(js)
    # 调用function方法
    r = docjs.call('h')
    # print(r)
    res = docjs.call('bxyz','/xdnphb/index/getMedia?AppKey=joker&keyword=&pageNumber=%d&pageSize=10&nonce=%s'%(num,r))
    # print(res)
    return r,res


def f():
    for item in range(1,1102):
        nonce,xyz = uuid_f(item)
        uuid = new_rank(item,nonce,xyz)
        for item in range(len(uuid)):
            result = newrank(uuid[item])
            print(result)


f()


# def a():
#     for item in range(100000):
#         print(item)

# def main():
#     threads = [threading.Thread(target=a) for _ in range(2)]
#     for thread in threads:
#         thread.start()
#
#     for thread in threads:
#         thread.join()



# if __name__ == '__main__':
#     main()