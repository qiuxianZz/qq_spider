import json

import requests
from lxml import etree

url = 'https://www.moretickets.com/list/1101-concerts/hottest/p1'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"

}


# def getprice(u):
#     url = "https://www.moretickets.com"
#     res = requests.get(url +u,headers=headers)
#     print(res.text)
#     tree = etree.HTML(res.text)
#     data = tree.xpath('//*[@id="sessionPar-container"]/ul')
#     print(data)
#     for item in data[0]:
#         price1 = item.xpath('./li[1]/div/span[1]')
#         print(price1)
#
#
#
# getprice("/content/5dd797a2d3521e483210585c")

# res = requests.get(url, headers=headers)
# # print(res.text)
# tree = etree.HTML(res.text)
# data = tree.xpath("/html/body/div[3]/div[1]/div/div[3]")
#
# print(data)
# for item in data[0]:
#     name = (item.xpath('./div/div[1]/div[2]/div[1]/@title'))
#     time = (item.xpath('./div/div[1]/div[2]/div[4]/div[1]/text()'))
#     site = (item.xpath('./div/div[1]/div[2]/div[4]/div[2]/text()'))
#     href = item.xpath('./@href')
#     print(name, time, site, href)
#     getprice(href[0])


def getprice(uid):
    url = "https://appapi.moretickets.com/showapi/pub/v1_2/show/{}/sessionone?src=android&ver=5.8.1&isSupportSession=true&bizCode=MTL&refreshTime=1583908753437&locationCityOID=5101".format(
        uid)
    res = requests.get(url, headers=headers)
    data = json.loads(res.text)
    result = data["result"]
    data = result["data"]
    seatplans = data[0]["seatplans"]
    list = []
    for item in seatplans:
        con = {}
        con["票价"] = item["originalPrice"]
        list.append(con)
    return list
# url = "https://appapi.moretickets.com/showapi/pub/site/58a2bb1d0cf273b891c85e8f/active_show?siteCityOID=5101&offset=0&length=10&src=android&ver=5.8.1&isSupportSession=true&bizCode=MTL&refreshTime=1583906901595&locationCityOID=5101&type=1&sorting=weight&seq=desc&"
# url = "https://appapi.moretickets.com/showapi/pub/site/58a2bb1d0cf273b891c85e8f/active_show?siteCityOID=1101&offset=20&length=10&src=android&ver=5.8.1&isSupportSession=true&bizCode=MTL&refreshTime=1583907188402&locationCityOID=5101&type=1&sorting=weight&seq=desc&"
# url = "https://appapi.moretickets.com/showapi/pub/site/58a2bb1d0cf273b891c85e8f/active_show?siteCityOID=5301&offset=120&length=10&src=android&ver=5.8.1&isSupportSession=true&bizCode=MTL&refreshTime=1583908289414&locationCityOID=5101&sorting=discount&seq=asc&"
url = "https://appapi.moretickets.com/showapi/pub/site/58a2bb1d0cf273b891c85e8f/active_show?siteCityOID=5101&offset=10&length=10&src=android&ver=5.8.1&isSupportSession=true&bizCode=MTL&refreshTime=1583908517315&locationCityOID=5101&sorting=discount&seq=asc&"

# url = "https://appapi.moretickets.com/showapi/pub/v1_2/show/5df0d1d6a81bd02e608781ef/sessionone?src=android&ver=5.8.1&isSupportSession=true&bizCode=MTL&refreshTime=1583908753437&locationCityOID=5101"
# url = "https://appapi.moretickets.com/showapi/pub/v1_2/show/5dce2142e24c3a59033de921/sessionone?src=android&ver=5.8.1&isSupportSession=true&bizCode=MTL&refreshTime=1583908832813&locationCityOID=5101"
res = requests.get(url, headers=headers)
data = json.loads(res.text)
result = data["result"]
data = result["data"]
con = {}
for item in data:
    showOID = item["showOID"]
    con = getprice(showOID)
    showName = item["showName"]
    venueName = item["venueName"]
    latestShowTime = item["latestShowTime"]
    print(showOID, showName, venueName, latestShowTime, con)
