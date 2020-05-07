import json

import requests

header = {
    "User-Agent": "ttnet okhttp/3.10.0.2",
}

url = 'https://api-service.chanmama.com/v1/home/author/info?author_id=2365744590893533'
res = requests.get(url, headers=header)
print(res.text)

import queue
import threading

import re
import requests
from lxml import etree


def handle_douyin_info(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    response = requests.get(url=url, headers=header)
    print(response.text)
    data = json.loads(response.text)
    if data["errCode"] != 50000:
        file_handle = open('1.txt', mode='a')
        file_handle.write(url)
        file_handle.write('\r\n')


q = queue.Queue()


def Producer():
    id = 6000025256
    while True:
        url = 'https://api-service.chanmama.com/v1/home/author/info?author_id={}'.format(id)
        q.put(url)
        id += 1


def Consumer():
    '''消费者'''
    while True:
        i = q.get()  # 从队列中取数据
        print(i)
        handle_douyin_info(i)


def main():
    p = threading.Thread(target=Producer)
    threads = [threading.Thread(target=Consumer) for _ in range(30)]
    for thread in threads:
        thread.start()
    p.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
