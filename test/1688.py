import re

import requests
#
url = 'https://s.1688.com/selloffer/offer_search.htm?keywords=%D2%C2%B7%FE&n=y&netType=1%2C11&encode=utf-8&spm=a260k.dacugeneral.search.0'
url = 'https://s.1688.com/selloffer/offer_search.htm?keywords=%D2%C2%B7%FE&n=y&netType=16&encode=utf-8&spm=a260k.dacugeneral.search.0&beginPage={}'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "cookie": '__wpkreporterwid_=5faea648-cc71-4295-b670-da7cefe6a501; cna=9S+uEoBdokcCAdpYG4whEJSq; ali_apache_id=10.147.120.49.1521527284800.284585.2; ali_ab=110.184.133.49.1573193857518.1; cookie2=18191d2a918761c7dbe84ed5ccbf4bad; hng=CN%7Czh-CN%7CCNY%7C156; t=d3282b1a5e0c9e602ed4cadfd2ee0d47; _tb_token_=ef7ebee51e511; UM_distinctid=171a57899fe972-02d81c25649d7d-b781636-1fa400-171a57899ff9a8; taklid=d224768f68c04738837e9ee70238d5c6; ali_beacon_id=110.184.181.213.1587619413788.493320.0; lid=%E8%87%AA%E7%94%B1%E5%A6%82%E5%BE%AE%E9%A3%8E; __cn_logon__=true; __cn_logon_id__=%E8%87%AA%E7%94%B1%E5%A6%82%E5%BE%AE%E9%A3%8E; ali_apache_track=c_mid=b2b-2813310569a188b|c_lid=%E8%87%AA%E7%94%B1%E5%A6%82%E5%BE%AE%E9%A3%8E|c_ms=1; ali_apache_tracktmp=c_w_signed=Y; last_mid=b2b-2813310569a188b; __rn_alert__=false; ctoken=xltnYFwysi097twdD1jspineneedle; _m_h5_tk=5a80e29d10f127477103aab035c1cc3d_1587631184969; _m_h5_tk_enc=95697d75941e1de275946313762f58ef; alisw=swIs1200%3D1%7C; cookie1=BxZjekYL89gPIyASGOV8xrvZw%2BUxnCZY60UzhXmxEXo%3D; cookie17=UUBZEjjYtBwjgw%3D%3D; sg=%E9%A3%8E90; csg=712ef369; unb=2813310569; uc4=nk4=0%40ti1AJsV93bxYt54vCkiuO2GoA0dX&id4=0%40U2LLEaOVDysVWUqbXuTQrEMkCNDZ; _nk_=%5Cu81EA%5Cu7531%5Cu5982%5Cu5FAE%5Cu98CE; _csrf_token=1587627519011; _is_show_loginId_change_block_=b2b-2813310569a188b_false; _show_force_unbind_div_=b2b-2813310569a188b_false; _show_sys_unbind_div_=b2b-2813310569a188b_false; _show_user_unbind_div_=b2b-2813310569a188b_false; alicnweb=touch_tb_at%3D1587627567123%7Clastlogonid%3D%25E8%2587%25AA%25E7%2594%25B1%25E5%25A6%2582%25E5%25BE%25AE%25E9%25A3%258E; ad_prefer="2020/04/23 15:41:30"; h_keys="%u8863%u670d#%u6c7d%u8f66%u7528%u54c1#%u664b%u6c5f%u5947%u8ff9%u978b%u4e1a#%u88e4%u5b50"; isg=BHd3AGsq5e9TomWUdqFqkUffBmvBPEueLfUqhckkp8ateJa60w9E72pZXtgmkCMW; l=eBxD8COqvwC9iCB-BOfZourza779JIRfguPzaNbMiT5POfXW5qbGWZjXqkxXCnGVnsgX-3z5HU79BoLZ5y4F7xv9-e9bhfrIEdLh.'
}

# res = requests.get(url,headers=headers)
# print(res.text)
# #
# &lastLoginMemberId=b2b-2813310569a188b&needUserInfo

def getUd(page):
    res = requests.get(url,headers=headers)
    # print(res.text)
    # data = re.findall("&lastLoginMemberId=(.*?)&needUserInfo", res.text, re.S)
    # "memberCreditUrl":"https:\/\/girlskids.1688.com\/page\/creditdetail.htm
    # "loginId":"girlskids","loginIdOfUtf8"
    # data = re.findall( '"loginId":"(.*?)","loginIdOfUtf8"', res.text, re.S)
    # a = 'tpCreditUrl":"https:\\/\\/(.*?).1688.com.*?page.*?creditdetail.htm'
    # data = re.findall( 'tpCreditUrl":"https:.*?(.*?).1688.com.*?page.*?creditdetail.htm', res.text, re.S)
    # "memberid":"b2b-2914651533b80ba","is_vip"
    data = re.findall( '"memberid":"(.*?)","is_vip":', res.text, re.S)
    print(data)
    for item in data:
        print(item)

# getUd(2)

# for item in range(1,11):
#     getUd(item)

#
# url = 'https://renders.1688.com/winport/page/archive.html?memberId=b2b-400305141307b29'
# res = requests.get(url,headers=headers)
# print(res.text)



# import time

# millis = int(round(time.time() * 1000))
# headers = {
#     "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; TAS-AN00 Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Safari/537.36 MMWEBID/9379 MicroMessenger/7.0.13.1640(0x27000D34) Process/appbrand2 NetType/WIFI Language/zh_CN ABI/arm32 WeChat/arm32 miniProgram",
#     "Cookie": "ali_apache_id=11.11.52.71.1587623347692.347843.2; _m_h5_tk=dbbc23250f500937c4d2f4028ba2d9a6_1587631268742; _m_h5_tk_enc=b6b019cc96861a5ffa60c9412e1bc824; cna=tCMoFxM9dXQCAW64h+adXlWR; UM_distinctid=171a5ba26ce49-0c51fb9c4d8096-33d2f4a-9c4c8-171a5ba26cf2ea; isg=BPv7iJeJIaPMex0X6FxQ1gLugdZlUA9S8r3Sg-24z_qQTBAudSEhoRyKYuoC7GdK"
# }
# # url = 'mtopjsonp8'
# url = 'https://h5api.m.1688.com/h5/mtop.1688.offerservice.getoffers/1.0/?jsv=2.4.11&appKey=12574478&t=1587623885782&sign=1cb761f69955d7c948e844520a588789&api=mtop.1688.offerService.getOffers&v=1.0&type=jsonp&dataType=jsonp&callback=mtopjsonp8&data=%7B%22sortType%22%3A%22pop%22%2C%22keywords%22%3A%22%E8%A1%A3%E6%9C%8D%20%E5%A5%B3%22%2C%22filtId%22%3A%22%22%2C%22p4pCount%22%3A%224%22%2C%22appName%22%3A%22wap%22%2C%22beginPage%22%3A7%2C%22pageSize%22%3A20%7D'
# # url = 'https://h5api.m.1688.com/h5/mtop.1688.offerservice.getoffers/1.0/?jsv=2.4.11&appKey=12574478&t=1587623887120&sign=1cb761f69955d7c948e844520a588789&api=mtop.1688.offerService.getOffers&v=1.0&type=jsonp&dataType=jsonp&callback=mtopjsonp9&data=%7B%22sortType%22%3A%22pop%22%2C%22keywords%22%3A%22%E8%A1%A3%E6%9C%8D%20%E5%A5%B3%22%2C%22filtId%22%3A%22%22%2C%22p4pCount%22%3A%224%22%2C%22appName%22%3A%22wap%22%2C%22beginPage%22%3A7%2C%22pageSize%22%3A20%7D'
# url = 'https://h5api.m.1688.com/h5/mtop.1688.offerservice.getoffers/1.0/?jsv=2.4.11&appKey=12574478&t=1587623885782&sign=1cb761f69955d7c948e844520a588789&api=mtop.1688.offerService.getOffers&v=1.0&type=jsonp&dataType=jsonp&callback=mtopjsonp8&data={"sortType":"pop","keywords":"衣服 女","filtId":"","p4pCount":"4","appName":"wap","beginPage":7,"pageSize":20}'
# url = 'https://h5api.m.1688.com/h5/mtop.1688.offerservice.getoffers/1.0/?jsv=2.4.11&appKey=12574478&t=1587624768681&sign=b9c04a664b03fadf3ae37aff330f5320&api=mtop.1688.offerService.getOffers&v=1.0&type=jsonp&dataType=jsonp&callback=mtopjsonp12&data=%7B%22sortType%22%3A%22pop%22%2C%22keywords%22%3A%22%E8%A1%A3%E6%9C%8D%20%E5%A5%B3%22%2C%22filtId%22%3A%22%22%2C%22p4pCount%22%3A%224%22%2C%22appName%22%3A%22wap%22%2C%22beginPage%22%3A11%2C%22pageSize%22%3A20%7D'
#
# res = requests.get(url,headers=headers)
# print(res.text)

headers = {
    "user-agent": "MTOPSDK%2F3.1.1.7+%28Android%3B5.1.1%3BHUAWEI%3BTAS-AN00%29",
    # "Cookie": "unb=2813310569; sn=; uc3=id2=UUBZEjjYtBwjgw%3D%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D&vt3=F8dBxGR1SJfuDYf5Mlk%3D&nk2=tMvPb7%2B7DOczeQ%3D%3D; uc1=cookie21=UIHiLt3xThH8t7YQoFNq&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&cookie14=UoTUPcqeQbtx3g%3D%3D; csg=dabbe421; lgc=%5Cu81EA%5Cu7531%5Cu5982%5Cu5FAE%5Cu98CE;t=efffdbf694b3b80ff4cb2be21433880d; cookie17=UUBZEjjYtBwjgw%3D%3D; dnk=%5Cu81EA%5Cu7531%5Cu5982%5Cu5FAE%5Cu98CE; skt=6a277afa08b9aec8; munb=2813310569; cookie2=71d2bea55020d9c2c378af300dd95e8f; uc4=id4=0%40U2LLEaOVDysVWUqbXuTQrEMmJR%2B6&nk4=0%40ti1AJsV93bxYt54vCkiuO2GqqWa6; tracknick=%5Cu81EA%5Cu7531%5Cu5982%5Cu5FAE%5Cu98CE; _cc_=WqG3DMC9EA%3D%3D; ti=10000470%40alibaba_android_8.23.2.0; sg=%E9%A3%8E90;_l_g_=Ug%3D%3D; _nk_=%5Cu81EA%5Cu7531%5Cu5982%5Cu5FAE%5Cu98CE; cookie1=BxZjekYL89gPIyASGOV8xrvZw%2BUxnCZY60UzhXmxEXo%3D; _tb_token_=e353345b7740e; imewweoriw=2ZLqrvoql2fHdQgzJBger9QCW9%2F4bOaDGZ2jRFof7Kg%3D; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BtOUrJKv7HNKTlS0XrNmTbos%3D; _w_tb_nick=%E8%87%AA%E7%94%B1%E5%A6%82%E5%BE%AE%E9%A3%8E; ockeqeudmj=p5hzmHw%3D; sgcookie=Y6lnpCTjBAYMlIZ1XGyRjec6LwbVTtEQ8V63XqTXPDp0kcG%2F9MXcn3gRskMuoceCHzk%3D; unb=2813310569; sn=;uc3=id2=UUBZEjjYtBwjgw%3D%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D&vt3=F8dBxGR1SJfuDYf5Mlk%3D&nk2=tMvPb7%2B7DOczeQ%3D%3D; uc1=cookie21=UIHiLt3xThH8t7YQoFNq&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&cookie14=UoTUPcqeQbtx3g%3D%3D; csg=dabbe421; lgc=%5Cu81EA%5Cu7531%5Cu5982%5Cu5FAE%5Cu98CE; t=efffdbf694b3b80ff4cb2be21433880d; cookie17=UUBZEjjYtBwjgw%3D%3D; dnk=%5Cu81EA%5Cu7531%5Cu5982%5Cu5FAE%5Cu98CE; skt=6a277afa08b9aec8; munb=2813310569;cookie2=71d2bea55020d9c2c378af300dd95e8f; uc4=id4=0%40U2LLEaOVDysVWUqbXuTQrEMmJR%2B6&nk4=0%40ti1AJsV93bxYt54vCkiuO2GqqWa6; tracknick=%5Cu81EA%5Cu7531%5Cu5982%5Cu5FAE%5Cu98CE; _cc_=WqG3DMC9EA%3D%3D; ti=10000470%40alibaba_android_8.23.2.0; sg=%E9%A3%8E90; _l_g_=Ug%3D%3D; _nk_=%5Cu81EA%5Cu7531%5Cu5982%5Cu5FAE%5Cu98CE; cookie1=BxZjekYL89gPIyASGOV8xrvZw%2BUxnCZY60UzhXmxEXo%3D; _tb_token_=e353345b7740e;imewweoriw=2ZLqrvoql2fHdQgzJBger9QCW9%2F4bOaDGZ2jRFof7Kg%3D; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BtOUrJKv7HNKTlS0XrNmTbos%3D; _w_tb_nick=%E8%87%AA%E7%94%B1%E5%A6%82%E5%BE%AE%E9%A3%8E; ockeqeudmj=p5hzmHw%3D; sgcookie=Y6lnpCTjBAYMlIZ1XGyRjec6LwbVTtEQ8V63XqTXPDp0kcG%2F9MXcn3gRskMuoceCHzk%3D"
    "Cookie": 'cna=84bvFhzbVksCAbaKhkM/hmYZ; taklid=9c8ad257f8ef4a47a4c5a012ca2f42a5; UM_distinctid=171a593ca48707-0aaee6011d09ef-11077430-1fa400-171a593ca495a3; ali_apache_id=11.23.109.12.1587620857557.376674.9; tbcp=f=UUjZel89AUtIFZo0KocPdSyI72Y%3D; uc3=vt3=F8dBxGR1S2lbshC1%2Fwk%3D&lg2=UtASsssmOIJ0bQ%3D%3D&id2=UUBZEjjYtBwjgw%3D%3D&nk2=tMvPb7%2B7DOczeQ%3D%3D; uc1=cookie14=UoTUPcqfHyYcgw%3D%3D&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&existShop=false&cookie15=VFC%2FuZ9ayeYq2g%3D%3D; csg=b52c4445; lgc=%5Cu81EA%5Cu7531%5Cu5982%5Cu5FAE%5Cu98CE; ntm=0; t=f7695c2d4b63cf78d0797c898e5e6788; dnk=%5Cu81EA%5Cu7531%5Cu5982%5Cu5FAE%5Cu98CE; skt=a12fa19d9ffd9f71; uc4=nk4=0%40ti1AJsV93bxYt54vCkiuO2BEKQ6R&id4=0%40U2LLEaOVDysVWUqbXuTQrEKzC7tM; tracknick=%5Cu81EA%5Cu7531%5Cu5982%5Cu5FAE%5Cu98CE; _cc_=Vq8l%2BKCLiw%3D%3D; lid=%E8%87%AA%E7%94%B1%E5%A6%82%E5%BE%AE%E9%A3%8E; _l_g_=Ug%3D%3D; sg=%E9%A3%8E90; _nk_=%5Cu81EA%5Cu7531%5Cu5982%5Cu5FAE%5Cu98CE; cookie1=BxZjekYL89gPIyASGOV8xrvZw%2BUxnCZY60UzhXmxEXo%3D; _tb_token_=e5695177d0764; __waplatid__=289bea442abe41fd874c71e002d39080; cookie17=UUBZEjjYtBwjgw%3D%3D; _m_h5_tk=7fcb481ca5f0c7fc1aba6b2d4ff8d6d5_1587643256986; _m_h5_tk_enc=756e5a6d3dcdce6d4de2a763c8e31637; ctoken=C0s4pNw88x0hYMtHM8Ycwing-web; webp=1; cn_tmp=Z28mC+GqtZ2fJadwi/kqrvUdQVUgNPbDy4tVdcZucrsIyOS2uR82kyv2quPW1rl4QGl+bFvAYnXj9ThF2KDMByJ1dpKkVgZTdRNjb7xhSLYdMfGAXbtHmWzUs0XusHE9; cn_tmp.sig=V3vAuBmbiKz6H0uBP_VL53Rj5zv1izdx9atY3OanhPE; cn_m_s=r1cWhCU4DZKn7wGUcE/2y1N6b6qzLM/moBaz+NU/0KJ0aRAviHaErigJ3og34Y01sSUDDXKASTY=; cn_m_s.sig=WBq8XIeumYXmnErP61XZCNNkoItzYWcwncLc35yTRsI; ali_apache_track="c_mid=b2b-2813310569a188b|c_lid=%E8%87%AA%E7%94%B1%E5%A6%82%E5%BE%AE%E9%A3%8E"; ali_apache_track.sig=Jc8TOKDl_39Hl72njN6A06sX6KdXByCvUahzPW5GrI0; cookie2=71dbdeaa13bfad5b9005b4dbecace2e6; cookie2.sig=3Wqhn4yY3BayBOoPoacoLVH6VOFt4vSg6X2CVqyoBb8; tbsnid=9lMMQp+C00e9mzK0XjP1r/DCCIwajUAYMLyObNLEPyA6sOlEpJKl9g==; tbsnid.sig=PHwmBPyClF3QQhkfe9NyUBJJP9a_ttvL0gO6ZO6oBNE; __cn_logon__=true; __cn_logon__.sig=_ajkY7FU0uQvAF-ntvenQBFbCtNdfk148wQYAOovzG0; unb=2813310569; unb.sig=57TkDegzm2rYSErq6ibiSHW7u9HkIZNlzJLFsogBhOU; __cn_logon_id__=%E8%87%AA%E7%94%B1%E5%A6%82%E5%BE%AE%E9%A3%8E; __cn_logon_id__.sig=SLqKcCTarCE2MWp2hPW0tnyGApcRLHbPE4QrIbyCrIk; ali-ss=eyJtZW1iZXJJZCI6ImIyYi0yODEzMzEwNTY5YTE4OGIiLCJ1c2VySWQiOiIyODEzMzEwNTY5IiwibG9naW5JZCI6IuiHqueUseWmguW+rumjjiIsInNpZCI6IjcxZGJkZWFhMTNiZmFkNWI5MDA1YjRkYmVjYWNlMmU2IiwiZWNvZGUiOiJTd25MSiIsImxvZ2luU3RhdHVzUmV0TXNnIjpudWxsLCJsb2dpbk1lc3NhZ2VFcnJvciI6bnVsbCwibG9naW5FcnJvclVzZXJOYW1lIjpudWxsLCJjaGVja2NvZGUiOm51bGwsInNlY3JldCI6IjNQTlo5MTc0OTZ2Y2lubHZIbUdGOWVvWSIsImtvYS1mbGFzaCI6e30sIl9leHBpcmUiOjE1ODc3MjAzNTcxODcsIl9tYXhBZ2UiOjg2NDAwMDAwfQ==; ali-ss.sig=FMb-wERrUG4R6cpykFPBo1HfKJFcQlqUS46rFMPm2vY; l=eBjqpxQmQ2H8bJIQBOfanurza77OSCOYYuPzaNbMiT5P_01B57W1WZjX8gT6C3GNhsteR3P95yXMBeYBq7Vonxv94AK85PMmn; isg=BIuL3KArUfNWVo2nxl-4N41mES91IJ-iLIU_Lv2IS0pjHKt-hfD088A68hTyPPea'
}
# url = 'http://h5api.m.1688.com/gw/mtop.1688.companyservice.getcompanys/1.0/?data=%7B%22deviceId%22%3A%22Aiv57zGSPgQ0tdh1THMTLap1DgkPZq0CSjgxzEF2tyRq%22%2C%22pageId%22%3A%22Aiv57zGSPgQ0tdh1THMTLap1DgkPZq0CSjgxzEF2tyRq1587626066004%22%2C%22categoryId%22%3A%220%22%2C%22beginPage%22%3A%2212%22%2C%22pageSize%22%3A%2220%22%2C%22lastLoginMemberId%22%3A%22b2b-2813310569a188b%22%2C%22sortType%22%3A%22pop%22%2C%22bizType%22%3A%220%22%2C%22local_utdid%22%3A%22XnmHVpqd%2FxoDACOMGtQ0eSIz%22%2C%22userAgent%22%3A%22android%22%2C%22keywords%22%3A%22%E4%BC%91%E9%97%B2%E8%A3%A4%22%7D'
# url = 'https://dj.1688.com/gw/mtop.1688.companyservice.getcompanys/1.0/?data=%7B%22deviceId%22%3A%22Aiv57zGSPgQ0tdh1THMTLap1DgkPZq0CSjgxzEF2tyRq%22%2C%22pageId%22%3A%22Aiv57zGSPgQ0tdh1THMTLap1DgkPZq0CSjgxzEF2tyRq1587627500163%22%2C%22categoryId%22%3A%220%22%2C%22beginPage%22%3A%225%22%2C%22pageSize%22%3A%2220%22%2C%22lastLoginMemberId%22%3A%22b2b-2813310569a188b%22%2C%22sortType%22%3A%22pop%22%2C%22bizType%22%3A%220%22%2C%22local_utdid%22%3A%22XnmHVpqd%2FxoDACOMGtQ0eSIz%22%2C%22userAgent%22%3A%22android%22%2C%22keywords%22%3A%22%E4%BC%91%E9%97%B2%E8%A3%A4%E7%94%B7%E7%AB%A5%22%7D'
# res = requests.get(url, headers=headers)
# print(res.text)

#
# res = requests.get("https://szgoogou.1688.com/page/contactinfo.htm?spm=a261y.7663282.autotrace-topNav.9.62994838R1mgLd",headers=headers)
# print(res.text)
# url = 'https://h5api.m.1688.com/h5/mtop.1688.offerservice.getoffers/1.0/?jsv=2.4.11&appKey=12574478&t=1587633970032&sign=52df28264c2ec187edece2f68b1eb4d6&api=mtop.1688.offerService.getOffers&v=1.0&type=jsonp&dataType=jsonp&callback=mtopjsonp2&data=%7B%22spm%22%3A%22a26g8.7710019.0.0%22%2C%22keywords%22%3A%22%E6%A9%A1%E5%A1%91%E6%B0%B4%E5%B8%A6%22%2C%22appName%22%3A%22wap%22%2C%22beginPage%22%3A3%2C%22pageSize%22%3A20%7D'
# url = 'https://h5api.m.1688.com/h5/mtop.1688.offerservice.getoffers/1.0/?jsv=2.4.11&appKey=12574478&t=1587634471142&sign=84368cd38e517ec775d1dd9618ec1ee9&api=mtop.1688.offerService.getOffers&v=1.0&type=jsonp&dataType=jsonp&callback=mtopjsonp4&data=%7B%22spm%22%3A%22a26g8.7710019.0.0%22%2C%22keywords%22%3A%22%E6%A9%A1%E5%A1%91%E6%B0%B4%E5%B8%A6%22%2C%22appName%22%3A%22wap%22%2C%22beginPage%22%3A5%2C%22pageSize%22%3A20%7D'
# res = requests.get(url,headers=headers)
# print(res.text)


url = 'https://api.amoeba-inc.com/v4?access_token=b60f4275854a11ea8097422f85317929&goms_action=17.api.shop.detail&id=657'

headers = {
    "User-Agent": "okhttp/3.12.1"

}
res = requests.get(url,headers=headers)
print(res.text)