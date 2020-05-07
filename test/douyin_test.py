import requests
import json
import csv

# lists=[]
# headers={
#     "Accept-Encoding":"gzip",
#     "Cache-Control":"max-stale=0",
#     "Host":"api.amemv.com",
#     "Connection":"Keep-Alive",
#     "Cookie":"odin_tt=82a949aa8ae1b872fa4df2f60c4d33fec8f334b767602b8b60ef9f507d93b15d5e8647968ff313460faa0076256aaace",
#     "User-Agent":"okhttp/3.8.1",
# }
# headers1={
#     "Accept-Encoding":"gzip",
#     "Cache-Control":"max-stale=0",
#     "Host":"aweme.snssdk.com",
#     "Connection":"Keep-Alive",
#     "Cookie":"odin_tt=82a949aa8ae1b872fa4df2f60c4d33fec8f334b767602b8b60ef9f507d93b15d5e8647968ff313460faa0076256aaace; qh[360]=1; install_id=40848822342; ttreq=1$e8c1f361efcda12544370f7a494603a452732861",
#     "User-Agent":"okhttp/3.8.1",
# }
# for i in range(8):
#     url="https://api.amemv.com/aweme/v1/music/aweme/?music_id=6572842239368628996&cursor=%d&count=20&type=6&retry_type=no_retry&iid=40848822342&device_id=56150513062&ac=wifi&channel=wap_aweme_homepage&aid=1128&app_name=aweme&version_code=176&version_name=1.7.6&device_platform=android&ssmix=a&device_type=MI+6+&device_brand=Xiaomi&language=zh&os_api=19&os_version=4.4.2&uuid=863254010282712&openudid=1c1b0d1f9c475224&manifest_version_code=176&resolution=1280*720&dpi=240&update_version_code=1762&_rticket=1541749638586&ts=1541749638&as=a155933e1658fb5b354703&cp=3484b8526759e7bee1mqpf&mas=0079976b3ffd723983ff617d6724ae8a12cc0cec2caccc46ac4666 HTTP/1.1"%(i*20)
#     # url="https://api.amemv.com/aweme/v1/user/?user_id=59595424956"
#     # url="https://api.amemv.com/aweme/v1/user/?user_id=71628104519&retry_type=no_retry&iid=40848822342&device_id=56150513062&ac=wifi&channel=wap_aweme_homepage&aid=1128&app_name=aweme&version_code=176&version_name=1.7.6&device_platform=android&ssmix=a&device_type=MI+6+&device_brand=Xiaomi&language=zh&os_api=19&os_version=4.4.2&uuid=863254010282712&openudid=1c1b0d1f9c475224&manifest_version_code=176&resolution=1280*720&dpi=240&update_version_code=1762&_rticket=1541747089699&ts=1541747089&as=a105439ea1691b01651063&cp=3792b7561e5eef1be1lifq&mas=00642bcd2ff19ec2ce0ca1f2836e1fff62cc6c0c8cac6c8c0c468c HTTP/1.1"
#
#     html=requests.get(url,headers=headers).text
#     b=json.loads(html)
#     for n in range(15):
#         new_url="https://api.amemv.com/aweme/v1/user/?user_id=%s&retry_type=no_retry&iid=40848822342&device_id=56150513062&ac=wifi&channel=wap_aweme_homepage&aid=1128&app_name=aweme&version_code=176&version_name=1.7.6&device_platform=android&ssmix=a&device_type=MI+6+&device_brand=Xiaomi&language=zh&os_api=19&os_version=4.4.2&uuid=863254010282712&openudid=1c1b0d1f9c475224&manifest_version_code=176&resolution=1280*720&dpi=240&update_version_code=1762&_rticket=1541774858486&ts=1541774856&as=a1e5d9ee08905bce154337&cp=9303b5538b57eaede1kjmt&mas=0045c1713eb5e0589ef116f3d71fecf90aeccccc2cac8ca6c646ac HTTP/1.1"%(b['aweme_list'][n]['author_user_id'])
#         new_html=requests.get(new_url,headers=headers1).text
#         c=json.loads(new_html)
#         print(c)
#         nickname=c["user"]["nickname"]
#         number=c["user"]["short_id"]
#         signature=c["user"]["signature"]
#         birthday=c["user"]["birthday"]
#         total_favorited=c["user"]["total_favorited"]
#         city=c["user"]["city"]
#         fans_count=c["user"]["followers_detail"][0]["fans_count"]
#         print(type(fans_count))
#         # l=["抖音昵称："+nickname,"抖音ID:"+str(number),"生日:"+birthday,"个人简介:"+signature,"获赞数:"+str(total_favorited),"粉丝数:"+str(fans_count)]
#         l=[nickname,str(number),city,birthday,signature,str(total_favorited),str(fans_count)]
#         print(l)
#         lists.append(l)
#
# with open("douyin.csv", "w", encoding="utf-8",newline="") as f:
#     k = csv.writer(f, dialect="excel")
#     k.writerow(["抖音昵称", "抖音ID","城市" ,"生日", "个人简介", "获赞数", "粉丝数"])
#
#     for list in lists:
#         k.writerow(list)
#



url = 'http://data.gdcic.net/Dop/Open/EnterpriseList.aspx'
url = 'http://jg.hbcic.net.cn/web/QyManage/QyList.aspx'
# data = {"__VIEWSTATE": "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"}
data = {"__VIEWSTATE":"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"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

res = requests.post(url,data=data,headers=headers)
print(res.text)