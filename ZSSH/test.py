import json
import requests

url = 'https://mlife.cmbchina.com/ContentPublisher/queryMiniProgDetailPage.json'


def getCon(i):
    headers = {
        "Host": "mlife.cmbchina.com",
        "Connection": "keep-alive",
        "Content-Length": "16",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "content-type": "application/x-www-form-urlencoded",
        "Referer": "https://servicewechat.com/wxf225cb5ecb7acdd2/12/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br",

    }
    # data = "contentId=709521"
    data = "contentId={}".format(i)
    # 707194
    # 704646
    #
    #
    #
    # 707858
    # 709521
    res = requests.post(url, headers=headers, data=data)
    print(res.text)


getCon(404614)
#
#
# i = 300000
# while True:
#     print(i)
#     getCon(i)
#     i += 1

url = 'https://mlife.cmbchina.com/AtpCore/comment/querySelectedCommentsAndReplyByPage.json'

'https://mlife.cmbchina.com/ContentPublisher/queryCmpContentSec.json'

"https://res.cc.cmbimg.com/fsp/File/G20200419G1740334539G31312D32313931382D5C345C355C.DAT"
"https://res.cc.cmbimg.com/fsp/File/G20200421G1760977742G31312D32313931382D5C385C345C.DAT"

"https://res.cc.cmbimg.com/fsp/File/G20200423G1783826620G31312D32313931382D5C375C395C.DAT"
"https://res.cc.cmbimg.com/fsp/File/G20200421G1760652299G31312D32313931382D5C375C345C.DAT"

"https://res.cc.cmbimg.com/fsp/File/AtpResource/4f4d213faa6e3db1a7bd2a4b6aafe98c/968ffa232eef4e3481ed8ff00c424b42.html"
"https://res.cc.cmbimg.com/fsp/File/AtpResource/4f4d213faa6e3db1a7bd2a4b6aafe98c/60dfb728a3074404ab125078d043700e.html"

# url = 'https://mlife.cmbchina.com/ContentPublisher/queryCmpContentSec.json'
# headers = {
#     "Accept": "*/*",
#     "Accept-Language": "zh-CN",
#     "Charset": "UTF-8",
#     "Connection": "Keep-Alive",
#     "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; TAS-AN00 Build/LMY48Z);(cmblife 8.0.10/106)",
#     "Content-Type": "text/plain;charset=utf-8",
#     "Content-Length": "731",
#     "Host": "mlife.cmbchina.com",
#     "Accept-Encoding": "gzip"
#
# }
# data = 'v10004IsO1tCMXd3z8EwVpZO2U8QZTXUFoB1TM24mPNDff1OEEL8yy3bNBv0+L4u48/HvfBp80XY2lNKUehnXUMU9g9wFMO2ueSrP2XnSjOAs=|nbisFhbfspi0b7dhFCanpTCCYNaZE6f9pnZPNslKNSru7hD8oK0hOFuiTl/DmJZvTVDZugV0lV1X73NKIMtJyC2vvNHgq1E0C2DN+5o7jJjteCV3Kd0pms9zp1dmX7qxKZ5lVUtH6jThe3SW8TuQvLjidhPKed5oYlUMjmlVs6vTXHNcd0oUrLSFqv3963zD5gMltiwQu+Mm8HK9+RMN1O/Fucnkt2LNH+q+mlsNe13DpyMPAqPr0pKMOPhPO47cptX87STHTzOVax4X06Fwoob3B90J+xqvCbEblvjjZy12MBsVMHRScXeoy8dw9cp+IDlZnG0fluRSN24EoKe+kbg/4u4RKOIUW+ZUbnr51VJ2vDvjYMxX0gdShMnkhvRDyyKaqesuNAbQt80PJwsqL96tIAU3B8yX7qUb4JmlgGW+Lsqpw89l5Ds+a82Pbpb94hyYOKxdmsLVX2fnY779uZIRQ38Se+RjTYfxzv7i89mjTpDGWyu/br/xPE9zDntrBmvXJxlcZPFSU40B0cSNshHgUNm3LkzZVk7wzWW6NalbQ7r098vHxMpUsQEd/FRfw6hYa5RsKSFDQU+NxRhDMSqrEuM8sFi2oWJWFz3sHLg='
#
# res = requests.post(url, headers=headers, data=data)
# print(res.text)

url = 'https://res.cc.cmbimg.com/fsp/File/G20200426G1807487604G31312D32313931382D5C325C365C.DATHost: res.cc.cmbimg.com'
headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; TAS-AN00 Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Safari/537.36 ergate-android;(cmblife 8.0.10/106 v2)",
    "Accept": "image/webp,image/*,*/*;q=0.8",
    "Referer": "https://res.cc.cmbimg.com/fsp/File/AtpResource/998c896a61f2311d9fcd5d5e9434f93d/701092d8ef09415a926cd110cf3f33c3.html?tabId=1001",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,en-US;q=0.8",
    "Cookie": "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22171a9e7bd1a3d-02d10c0055ded-6c331c75-640200-171a9e7bd1bf3%22%2C%22%24device_id%22%3A%22171a9e7bd1a3d-02d10c0055ded-6c331c75-640200-171a9e7bd1bf3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%8",

}

# res = requests.get(url,headers=headers)
# print(res.text)

url = 'https://mlife.cmbchina.com/ContentPublisher/queryCmpContentSec.json'

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN",
    "Charset": "UTF-8",
    "Connection": "Keep-Alive",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; TAS-AN00 Build/LMY48Z);(cmblife 8.0.10/106)",
    "Content-Type": "text/plain;charset=utf-8",
    "Content-Length": "731",
    "Host": "mlife.cmbchina.com",
    "Accept-Encoding": "gzip"

}
data = 'v10003xQfND94abSR1X/m8RxGu+XTms8KyzXm2YKVgReajCNVn+ZaXRM3wKcuPKNEXlkIr9SKCWf2NxS9h1rGCbqryhZd7I7YmD5msxqEsODY=|TwRnzGmvJqVZPNMW1YmbBbLCl+DeBoITKUxARm2DlPpDjwyeIt3iimROx+PW++sqSvuV3qM7zUHpmJ5Vdg5tJB0Gf5axOKWEka837qFEDKcgBSqjPQnHW+NeqyBXZze8+OkIDAUToomEhhgBiL//t6XL/etvBdoLJa2lLwCfghhmkHezco4YtxYY9Zy9V1/jCJWzMh7UM6feuj09jMG0Zv7REBCmixbgPOQWM49pOwjOWIQKZ7xYxQQAafQ8dJP4rl1gSLJ0gUTBiVMq6uU/cAb4Tjudo+QUYu0Imn+EShVSWpl1l1CwCzR/JyubzSn9goGIWsRFZ+xegPOmE/oMNoCJWq+2ScQN5hRdKl4Z3XFaxso+pSNDimk95mxBhX+VuGidlsnFpE2A7UFPP+Ph8a8RjGFYM3Dv4us3VSxPnz4Ihb4xYLSd4IvxCTKcLe8lgNyD42NrpdpjcTH85rOenD0SIN4TqMrDtrj7Q5a55vBdQB3/0I1GL/IwRQsBRjL4aPWQuiKTS+7odAJQbangv+Y7hOHUP0+eAH+i9IJVAEEzvk7vnMyf0nFeJYpN2j9iVH5NV59OcHSlX4VLn9AXnSb2cBvygp8YW9rlByUbg74='

# res = requests.post(url,headers=headers,data=data)
# print(res.text)

'v10003xQfND94abSR1X/m8RxGu+XTms8KyzXm2YKVgReajCNVn+ZaXRM3wKcuPKNEXlkIr9SKCWf2NxS9h1rGCbqryhZd7I7YmfJD4Y+weOnI=|yauk9iUygvmbNMgTTa0k5axkRXU1eOg1oXIvSWf55tUmODn5Sm9NL/WvdVcAVCJMtXQHuFUNu+HEts0U4BQUYIyyHarP382Blz6xf1YAaQVMy/czojjgvoF7QEeARj6Q/qphx4J50USZuBa5zN/biTNX3u289CFPgHFPSI2Lhin+gdOXd8pVrPy3QZXaiv0E8QRgIPyWNADu71Cpntq9SxyMrEgFGar8bVGwSB0YztPwzS5dL6+KPUl8F99Ze7q3LDcm2LnBh3tvic5z5gA0U3jChvZdt8X43sbEvPGUHuYaPnA6dlzZYafX2oA8UcymDTHGaqXDJ42D+z1w5f5+W0G6LytBRs2Qrp00yksCZtQfy5/Ey6Mpd9VhqZ1+/kpsdSDCLy0YE0qnNj95eTzAtwsO65TEeaEPBKy3+vDYu3I/whNng8dove/ak6QIuxGgT5VGljWWtx0kTNPDv8sLZVeKzXcUnAwPNtl/i26D89ddSfcbLXq6Io/8VLmP3b6bQhkNIitn7aYz0m5mCfLsOQNbbWjVJYfk3MuCk93PLSnham2BgYUr7aSoLQAp91a15Z+H40IlF3o54rSRH1MVTyNcmKh863wIcY7pno0h/EU='
'v10003xQfND94abSR1X/m8RxGu+XTms8KyzXm2YKVgReajCNVn+ZaXRM3wKcuPKNEXlkIr9SKCWf2NxS9h1rGCbqryhZd7I7YmkooWWSJHXkg=|oHd+IOVl+iWzmD1LBzB7uThBH0qc5MSWWKz0WSxgPrleWqTfPlLEol+xoBaROP7JB5u44q0tuk1XjiPm4tODwvjgkoGY66AisWDE41Y+gOu8lktlQGKC81qyRv8TOIMLOA7QFZLS/6k/j15Of0rp46D9Qm+KWFeRKYoklimO9kwmjo2xx9d6FqMgQhYFVPyefx+BvsWjvY4Ig/d+EUO5MPJ/ILSuxq1fuCd7F9tFXZWhwuKBUW5Ei1xYrwz7J8N8iuhBUWfzMhBhoW9MaJzXhDKwkiPeTDBka1ITzfjCTHAzU40seKkDLI5PkIgsqpm0pwasbBJL/XlO9Y6jLaP+HwTZGPYhZVVCmhoICkt8p8Jd6qau2AY3SEEYBK8ZBE6BpIK7htheX5I59V4f+LKPLKQuH+9ftQ1HsLiFcUp2zWT6U1O1MQcLWwvziVJ7pM9N5T+7gY0Q7JVLPRgZfYueDdoS6Ng6+GH3llJv5TbKYz9awX6rcq9HoggZ9zaUnMbDuVr1xRh0Ym3mBud2LTTEXgAqxxTsPyev6kLyzw8zFyhYNQRvJd14if9D+y1CFv8L3QDiN3u+WedERTQi4mMlTUoBVsaINm/CFM1bIttvTGc='
