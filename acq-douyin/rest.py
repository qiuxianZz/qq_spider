import requests
from lxml import etree

url = 'https://detail.vip.com/detail-1710618238-6918209495798829662.html'
def get_vip_brandStoreName(url):
    headers = {
        # "Connection": "keep-alive",
        # "Pragma": "no-cache",
        # "Cache-Control": "no-cache",
        # "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        # "X-Requested-With": "XMLHttpRequest",
        # "Content-Type": "application/x-www-form-urlencoded",
        # "Referer": "https://music.163.com/",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Accept-Language": "zh-CN,zh;q=0.9",
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    res = requests.get(url,headers=headers)

    # print(res.text)
    tree = etree.HTML(res.text)

    name = tree.xpath('/html/body/div[5]/div[1]/div/div[3]/div[1]/div[1]/div/a/text()')
    print(name)


# get_vip_brandStoreName('https://m.vip.com/public/go.html?pid=2161772874&brandid=3725885')


