import  requests
from bs4 import BeautifulSoup
from lxml import etree


def get_content(page):
    url = 'http://www.dianping.com/chengdu/ch10/g110p{}?cpt=1906736093'.format(page)
    print(url)
    header = {
        "Host": "www.dianping.com",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Cookie": "cy=8; cye=chengdu; _lxsdk_cuid=16f22511ba5c8-0fd95f208c34e-b781636-1fa400-16f22511ba6c8; _lxsdk=16f22511ba5c8-0fd95f208c34e-b781636-1fa400-16f22511ba6c8; _hc.v=4a5256a0-9d3d-36a2-eb2a-219caa16dc2d.1576828739; s_ViewType=10; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=16f5b080b81-ed1-af-d88%7C%7C266"
    }
    res = requests.get(url,headers=header)
    # print(res.text)
    tree = etree.HTML(res.text)
    ul = tree.xpath('//*[@id="shop-all-list"]/ul')
    print(len(ul[0]))
    for li in ul[0]:
        data = {}
        url = li.xpath('./div[1]/a/@href')
        data["url"] = url[0]

        img_src = li.xpath('./div[1]/a/img/@src')
        data["img_src"] =img_src[0]
        shop_name = li.xpath('./div[2]/div[1]/a[1]/h4/text()')
        data["shop_name"] = shop_name[0]
        level = li.xpath('./div[2]/div[2]/span/@title')
        data["level"] = level[0]
        group = li.xpath('./div[3]/a/@title')
        data["group"] = group[0]
        feature1 = li.xpath('./div[2]/div[4]/a[1]/text()')
        feature2 = li.xpath('./div[2]/div[4]/a[2]/text()')
        feature3 = li.xpath('./div[2]/div[4]/a[3]/text()')
        data["feature"] = [feature1[0],feature2[0],feature3[0]]
        print(data)
        # a = li.xpath('./div[3]/a[2]/@data-address')
        # b = li.xpath('./div[4]/a[2]/@data-address')
        #
        # print(a)
        # print(b)
        #

for i in range(1,51):
    get_content(i)


# def parse_con(con):
#     tree = etree.HTML(con)
