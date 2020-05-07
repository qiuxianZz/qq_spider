import json
import signal
import time
import datetime

import requests

from queue import Queue, LifoQueue, PriorityQueue


# q = Queue(maxsize=0)
# ipQueue = Queue(maxsize=0)
#
#
# def verify_ip(ips: dict):
#     """
#     :param ips: 代理列表
#     :return:
#     """
#     try:
#         proxy = {
#             'http': 'http://' + ips["ip"] + ':' + ips["port"],
#             'https': 'https://' + ips["ip"] + ':' + ips["port"]
#         }
#         head = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
#             'Connection': 'keep-alive'}
#         '''http://icanhazip.com会返回当前的IP地址'''
#         p = requests.get('http://icanhazip.com', headers=head, proxies=proxy)
#         if p.status_code == 200:
#             return ips
#         else:
#             return None
#
#     except Exception as e:
#         print(e)
#
#
# def getProxy():
#     res = requests.get('http://115.29.174.137:3333/xdn/proxies/get?count=10&type=0&all=0')
#     proxies_list = json.loads(res.text)
#     proxies = (proxies_list['RESULT'])
#     for p in proxies:
#         q.put(p)
#
#
# def valid_ip():
#     while True:
#         ip = verify_ip(q.get())
#         if ip == None:
#             continue
#         else:
#             return ip
#
#
# def ip():
#     while True:
#         if q.qsize() < 10:
#             getProxy()
#         ip = valid_ip()
#         ipQueue.put(ip)
#         print(ipQueue.get())
#
#
# ip()
#


def verify_ip():
    res = requests.get('http://115.29.174.137:3333/xdn/proxies/get?count=10&type=0&all=0')
    proxies_list = json.loads(res.text)
    proxies = (proxies_list['RESULT'])
    for p in proxies:
        try:
            proxy = {
                'http': 'http://' + p["ip"] + ':' + p["port"],
            }
            head = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                'Connection': 'keep-alive'}
            res = requests.get('http://icanhazip.com', headers=head, proxies=proxy)

            if res.status_code == 200:
                return p
            else:
                continue
        except Exception as e:
            print(e)
            continue
verify_ip()
#
# class Get_ip:
#     q = Queue(maxsize=0)
#     ipQueue = Queue(maxsize=0)
#
#     # def __init__(self, ipQueue, q):
#     #     self.ipQueue = ipQueue
#     #     self.q = q
#
#     def verify_ip(self):
#         ip = self.q.get()
#         try:
#             proxy = {
#                 'http': 'http://' + ip["ip"] + ':' + ip["port"],
#                 'https': 'https://' + ip["ip"] + ':' + ip["port"]
#             }
#             head = {
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
#                 'Connection': 'keep-alive'}
#             '''http://icanhazip.com会返回当前的IP地址'''
#             res = requests.get('http://icanhazip.com', headers=head, proxies=proxy)
#             if res.status_code == 200:
#                 return ip
#             else:
#                 return None
#
#         except Exception as e:
#             print(e)
#
#     def getProxy(self):
#         res = requests.get('http://115.29.174.137:3333/xdn/proxies/get?count=10&type=0&all=0')
#         proxies_list = json.loads(res.text)
#         proxies = (proxies_list['RESULT'])
#         for p in proxies:
#             self.q.put(p)
#
#     def valid_ip(self):
#         while True:
#             ip = self.verify_ip()
#             if ip == None:
#                 continue
#             else:
#                 return ip
#
#     def ip(self):
#         while True:
#             if self.q.qsize() < 10:
#                 self.getProxy()
#             ip = self.valid_ip()
#             self.ipQueue.put(ip)
#             # print(self.ipQueue.get())
#
#
#
# i = Get_ip()
# i.ip()
# print(i.ipQueue.qsize())



