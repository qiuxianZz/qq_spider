import re
import telnetlib
import time

from lxml import etree
import requests

xici_ip = "https://www.xicidaili.com/nn//"

iphai_ip = ['http://www.iphai.com/free/ng', 'http://www.iphai.com/free/wg']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',

}


def check_proxy(ip, port):
    print(ip,port)
    """第二种："""
    try:
        # 设置重连次数
        requests.adapters.DEFAULT_RETRIES = 3
        # IP = random.choice(IPAgents)
        proxy = f"http://{ip}:{port}"
        # thisIP = "".join(IP.split(":")[0:1])
        # print(thisIP)
        res = requests.get(url="http://icanhazip.com/", timeout=2, proxies={"http": proxy})
        proxyIP = res.text
        print(proxyIP)
        if (proxyIP == proxy):
            print("代理IP:'" + proxyIP + "'有效！")
            return True
        else:
            print("2代理IP无效！")
            return False
    except:
        print("1代理IP无效！")
        return False



def get_xici_ip(url):
    res = requests.get(url, headers=headers)
    tree = etree.HTML(res.text)
    tb = tree.xpath('//*[@id="ip_list"]')
    print(len(tb[0]))
    for item in tb[0]:
        ip = item.xpath('./td[2]/text()')
        port = item.xpath('./td[3]/text()')
        if ip == [] and port == []:
            continue
        check_proxy(ip[0],port[0])




def get_iphai_ip(url):
    for item in url:
        res = requests.get(item,headers)
        tree = etree.HTML(res.text)
        tb = tree.xpath('/html/body/div[2]/div[2]/table/tbody')
        print(tb)



def get_ip():
    res = requests.get(url='http://p.ashtwo.cn/',headers=headers)
    tree = etree.HTML(res.text)
    proxy = tree.xpath('/html/body/p/text()')
    a = (proxy[0].split(":"))
    check_proxy(a[0],a[1])



# get_iphai_ip(iphai_ip)/
# 47.101.134.187:8888
check_proxy('117.169.78.54',17982)
# while True:
#     get_ip()
#     time.sleep(2)