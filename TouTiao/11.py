import requests

headers1 = {
    'Host': 'sale.gongji58.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type': 'application/json',
    'token': '3b70e44b43623a5da291c352b8d4766dffeaf4c266d5d08f7e4dd0a704f335dc',
    'Referer': 'https://servicewechat.com/wx886fad111cc18e75/102/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br',

}
# url3="https://rate.taobao.com/detailCommon.htm?auctionNumId=40781988852&callback=jsonp"
# print(requests.get(url3,headers=headers1).text)
session = requests.session()
res = session.get('https://sale.gongji58.com/v1/car?id=9744',headers=headers1)
print(res.text)