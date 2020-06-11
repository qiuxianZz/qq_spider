# # import json
# # import re
# #
# # import requests
# # from lxml import etree
# # #
# # # for _ in range(1):
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
#     # 'cookie': 'cna=9S+uEoBdokcCAdpYG4whEJSq; ali_apache_id=10.147.120.49.1521527284800.284585.2; ali_ab=110.184.133.49.1573193857518.1; UM_distinctid=171a57899fe972-02d81c25649d7d-b781636-1fa400-171a57899ff9a8; taklid=d224768f68c04738837e9ee70238d5c6; ali_beacon_id=110.184.181.213.1587619413788.493320.0; lid=%E8%87%AA%E7%94%B1%E5%A6%82%E5%BE%AE%E9%A3%8E; ali_apache_track=c_mid=b2b-2813310569a188b|c_lid=%E8%87%AA%E7%94%B1%E5%A6%82%E5%BE%AE%E9%A3%8E|c_ms=1; h_keys="%u8863%u670d#%u8863%u670d%u77f3%u72ee%u5e02%u5e38%u9752%u5885%u670d%u88c5%u5382#%u6c7d%u8f66%u7528%u54c1#%u664b%u6c5f%u5947%u8ff9%u978b%u4e1a#%u88e4%u5b50"; ad_prefer="2020/04/23 17:00:29"; cookie2=1d345f2c941aee66f4eb8dc2203bafbf; hng=CN%7Czh-CN%7CCNY%7C156; t=d9fc0269f45fef3a31596e1105a1beb6; _tb_token_=fe3bd645dee3e; __cn_logon__=true; __cn_logon_id__=%E8%87%AA%E7%94%B1%E5%A6%82%E5%BE%AE%E9%A3%8E; ali_apache_tracktmp=c_w_signed=Y; cookie1=BxZjekYL89gPIyASGOV8xrvZw%2BUxnCZY60UzhXmxEXo%3D; cookie17=UUBZEjjYtBwjgw%3D%3D; sg=%E9%A3%8E90; csg=d0ed9245; unb=2813310569; uc4=id4=0%40U2LLEaOVDysVWUqbXuWPyR8V4Nbu&nk4=0%40ti1AJsV93bxYt54vCknE786HU0a6; _nk_=%5Cu81EA%5Cu7531%5Cu5982%5Cu5FAE%5Cu98CE; last_mid=b2b-2813310569a188b; _csrf_token=1591704545470; _is_show_loginId_change_block_=b2b-2813310569a188b_false; _show_force_unbind_div_=b2b-2813310569a188b_false; _show_sys_unbind_div_=b2b-2813310569a188b_false; _show_user_unbind_div_=b2b-2813310569a188b_false; __rn_alert__=false; alicnweb=touch_tb_at%3D1591704551319%7Clastlogonid%3D%25E8%2587%25AA%25E7%2594%25B1%25E5%25A6%2582%25E5%25BE%25AE%25E9%25A3%258E%7Cshow_inter_tips%3Dfalse; l=eBxD8COqvwC9iiaXBOfwourza77OSIRAguPzaNbMiOCP_JC65WvAWZvhDZ8BC3GVh6-JR3z5HU7TBeYBqI2qOlGuT6b6mnDmn; isg=BB0dLEOyH2O0If_GgGcgQ8kxLPkXOlGMU4tQ99_iWXSjlj3Ip4phXOsAwIqQVmlE'
# }
# # #     # url = 'https://jsgongyi.1688.com/page/contactinfo.htm'
# # #     # url = 'https://shop2764083652742.1688.com/page/contactinfo.htm'
# # #     url = 'https://zyyyfs.1688.com/page/contactinfo.htm'
# # #     res = requests.get(url, headers=headers)
# # #     tree = etree.HTML(res.text)
# # #     # tel = tree.xpath('//*[@id="site_content"]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/dl[2]/dd/text()')
# # #     tel = tree.xpath('//*[@id="site_content"]/div[1]/div/div/div/div[2]')
# # #     con = tel[0].xpath('string(.)').strip()
# # #     print(con)
# # #
# #
# #
# # def getcon(url):
# #     headers = {
# #         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
# #         'cookie': 'cna=9S+uEoBdokcCAdpYG4whEJSq; ali_apache_id=10.147.120.49.1521527284800.284585.2; ali_ab=110.184.133.49.1573193857518.1; UM_distinctid=171a57899fe972-02d81c25649d7d-b781636-1fa400-171a57899ff9a8; taklid=d224768f68c04738837e9ee70238d5c6; ali_beacon_id=110.184.181.213.1587619413788.493320.0; lid=%E8%87%AA%E7%94%B1%E5%A6%82%E5%BE%AE%E9%A3%8E; ali_apache_track=c_mid=b2b-2813310569a188b|c_lid=%E8%87%AA%E7%94%B1%E5%A6%82%E5%BE%AE%E9%A3%8E|c_ms=1; h_keys="%u8863%u670d#%u8863%u670d%u77f3%u72ee%u5e02%u5e38%u9752%u5885%u670d%u88c5%u5382#%u6c7d%u8f66%u7528%u54c1#%u664b%u6c5f%u5947%u8ff9%u978b%u4e1a#%u88e4%u5b50"; ad_prefer="2020/04/23 17:00:29"; cookie2=1d345f2c941aee66f4eb8dc2203bafbf; hng=CN%7Czh-CN%7CCNY%7C156; t=d9fc0269f45fef3a31596e1105a1beb6; _tb_token_=fe3bd645dee3e; __cn_logon__=true; __cn_logon_id__=%E8%87%AA%E7%94%B1%E5%A6%82%E5%BE%AE%E9%A3%8E; ali_apache_tracktmp=c_w_signed=Y; cookie1=BxZjekYL89gPIyASGOV8xrvZw%2BUxnCZY60UzhXmxEXo%3D; cookie17=UUBZEjjYtBwjgw%3D%3D; sg=%E9%A3%8E90; csg=d0ed9245; unb=2813310569; uc4=id4=0%40U2LLEaOVDysVWUqbXuWPyR8V4Nbu&nk4=0%40ti1AJsV93bxYt54vCknE786HU0a6; _nk_=%5Cu81EA%5Cu7531%5Cu5982%5Cu5FAE%5Cu98CE; last_mid=b2b-2813310569a188b; _csrf_token=1591704545470; _is_show_loginId_change_block_=b2b-2813310569a188b_false; _show_force_unbind_div_=b2b-2813310569a188b_false; _show_sys_unbind_div_=b2b-2813310569a188b_false; _show_user_unbind_div_=b2b-2813310569a188b_false; __rn_alert__=false; alicnweb=touch_tb_at%3D1591704551319%7Clastlogonid%3D%25E8%2587%25AA%25E7%2594%25B1%25E5%25A6%2582%25E5%25BE%25AE%25E9%25A3%258E%7Cshow_inter_tips%3Dfalse; l=eBxD8COqvwC9iiaXBOfwourza77OSIRAguPzaNbMiOCP_JC65WvAWZvhDZ8BC3GVh6-JR3z5HU7TBeYBqI2qOlGuT6b6mnDmn; isg=BB0dLEOyH2O0If_GgGcgQ8kxLPkXOlGMU4tQ99_iWXSjlj3Ip4phXOsAwIqQVmlE'
# #     }
# #     # url = 'https://jsgongyi.1688.com/page/contactinfo.htm'
# #     url = url + '/page/contactinfo.htm'
# #     print(url)
# #     res = requests.get(url, headers=headers)
# #     tree = etree.HTML(res.text)
# #     # tel = tree.xpath('//*[@id="site_content"]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/dl[2]/dd/text()')
# #     tel = tree.xpath('//*[@id="site_content"]/div[1]/div/div/div/div[2]')
# #     con = tel[0].xpath('string(.)').strip()
# #     print(con)
# #
# # def geturl(page):
# #     url = 'https://s.1688.com/selloffer/offer_search.htm?keywords=%C4%B8%D3%A4&n=y&netType=16&encode=utf-8&spm=a260k.dacugeneral.search.0&beginPage={}#sm-filtbar'.format(page)
# #     res = requests.get(url,headers =headers )
# #     u = re.findall('successDataCheck\((.*?)\);',res.text,re.S)
# #     # u = re.findall('memberCreditUrl":"(.*?)","province"',res.text,re.S)
# #     # for item in u:
# #     #     # a = re.findall('"url":(.*?)"memberCreditUrl"',item,re.S)
# #     #     # for i in a:
# #     #     print(item)
# #     #     # data = json.loads(item)
# #     #     # offerList = data["data"]["offerList"]
# #     #     # print(offerList)
# #     data = json.loads(u[1])
# #     offerList = data["data"]["offerList"]
# #     for item in offerList:
# #         url = (item["company"]["url"])
# #         getcon(url)
# #
# # for i in range(1,51):
# #     geturl(i)
# #
# #
#
# import  requests
# data = 'taskType=6&params=%7B%22mid%22%3A626%2C%22bvid%22%3A%22BV16b411M7Wz%22%7D&taskId=0'
# res = requests.post('http://127.0.0.1:3701/bili/output/task/add',data = data,headers=headers)
# print(res.text)