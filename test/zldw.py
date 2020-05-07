import json

import requests

url = "https://coop.incopat.com/appservice/patentBazaar/detail.json"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "65",
    "Host": "coop.incopat.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.12.0",

}

# #
data = {"token=&secretKey=pZzYZNc6JiWFaWgXzJJ5JQ==&patentBazaarId=9996"}
data = {
    "token":"",
    "secretKey":"",
    "patentBazaarId":"9994"
}
res = requests.post(url,headers=headers,data=data)
print(res.text)
# #
#
# def zl(id):
#     data = {
#         "token": "",
#         "secretKey": "",
#         "patentBazaarId": id
#     }
#     res = requests.post(url, headers=headers, data=data)
#     res = json.loads(res.text)
#     print(res)
#     res = res["data"]
#     print(res)
#     # return res
# zl(1)

for item in range(9994,10004):
    data = {
        "token": "",
        "secretKey": "",
        "patentBazaarId": item
    }
    print(item)

    res = requests.post(url, headers=headers, data=data)
    res = json.loads(res.text)
    # print(res)
    con = res["data"]
    # print(res)
    # data = json.loads(data)
    # print(data)
    # data = data["data"]
    number = con["number"]
    description = con["description"]
    imageUrl = con["imageUrl"]
    ti = con["ti"]
    tits = con["tits"]
    pt = con["pt"]
    ptName = con["ptName"]
    ipcCategory = con["ipcCategory"]
    ipcCategoryName =con["ipcCategoryName"]
    mobile = con["mobile"]
    shopName = con["shopName"]
    pn = con["pn"]
    an = con["an"]
    apOr = con["apOr"]
    priceStr = con["priceStr"]
    promotionName = con["promotionName"]
    print(number,description,imageUrl,ti,tits,pt,ptName,ipcCategory,ipcCategoryName,mobile,shopName,pn,an,apOr,priceStr,promotionName)
    print("")

