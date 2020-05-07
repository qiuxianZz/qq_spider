import random

import requests

import json

url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzI2MzE2NDczMw==&f=json&offset=65&count=10&is_ok=1&scene=124&uin=MTk2NjU4NjExNQ%3D%3D&key=818087460639ae49b601d56fddd2ee628d5c0a635384d914f2244e1909c4b670d42c5ff24d186f3c7d47d5b44ac5d1074ff20de1c44b8b6d379393a091b591710a49d860de864d75fd0b4e0b997f3685&pass_ticket=DO87H6ckGVLIlqKdfbfDspa266VK4C0rYUe8WX+PfXsSePh3Xcs6vm4yS9H3HES7&wxtoken=&appmsg_token=1054_Dhxb959N%252BlysRQOwAf6q5QpnKdnr9JVzFuvXQg~~&x5=0&f=json'
# url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzI2MzE2NDczMw==&f=json&offset=78&count=10&is_ok=1&scene=124&uin=MTk2NjU4NjExNQ%3D%3D&key=861420a46a8ac7f7b70f23b547641b8b843b3c7d8e8d060357f84c2acc5c54f70ebcb3dbfc86ff7b4c10a4a20766e637758d3e6860ad5ead35ca147ba9dd3a974dbdd4aa9449e8763bf26996c035e48e&pass_ticket=6mCeSkEWVRedXWTjDkFVF5R5X7NyAfemlYMw5stQMS1hqBe%2Bwx8IpJ%2BVRwrvIqS4&wxtoken=&appmsg_token=1054_Dhxb959N%252BlysRQOwAf6q5QpnKdnr9JVzFuvXQg~~&x5=0&f=json'
# url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzI2MzE2NDczMw==&f=json&offset=93&count=10&is_ok=1&scene=124&uin=MTk2NjU4NjExNQ%3D%3D&key=861420a46a8ac7f7b70f23b547641b8b843b3c7d8e8d060357f84c2acc5c54f70ebcb3dbfc86ff7b4c10a4a20766e637758d3e6860ad5ead35ca147ba9dd3a974dbdd4aa9449e8763bf26996c035e48e&pass_ticket=6mCeSkEWVRedXWTjDkFVF5R5X7NyAfemlYMw5stQMS1hqBe%2Bwx8IpJ%2BVRwrvIqS4&wxtoken=&appmsg_token=1054_Dhxb959N%252BlysRQOwAf6q5QpnKdnr9JVzFuvXQg~~&x5=0&f=json'
# url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzI2MzE2NDczMw==&f=json&offset=106&count=10&is_ok=1&scene=124&uin=MTk2NjU4NjExNQ%3D%3D&key=861420a46a8ac7f7b70f23b547641b8b843b3c7d8e8d060357f84c2acc5c54f70ebcb3dbfc86ff7b4c10a4a20766e637758d3e6860ad5ead35ca147ba9dd3a974dbdd4aa9449e8763bf26996c035e48e&pass_ticket=6mCeSkEWVRedXWTjDkFVF5R5X7NyAfemlYMw5stQMS1hqBe%2Bwx8IpJ%2BVRwrvIqS4&wxtoken=&appmsg_token=1054_Dhxb959N%252BlysRQOwAf6q5QpnKdnr9JVzFuvXQg~~&x5=0&f=json'
# url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzI2MzE2NDczMw==&f=json&offset=119&count=10&is_ok=1&scene=124&uin=MTk2NjU4NjExNQ%3D%3D&key=e2ae4c71ebea1245e4baf7f27d2d3ae788ede8cc5536bab67fe0827c7ca7f0bf5c5fe2545e55991e80cafd6bc6a90deb1d8938254a3cc12ec82f145c55902df8231ba23773879c5bbb22e8815b469f5f&pass_ticket=DO87H6ckGVLIlqKdfbfDspa266VK4C0rYUe8WX%2BPfXsSePh3Xcs6vm4yS9H3HES7&wxtoken=&appmsg_token=1054_mJB77k01fVmRSPb0aObOYIPJ0noWxXnO346jtg~~&x5=0&f=json'
# url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzI2MzE2NDczMw==&f=json&offset=44&count=10&is_ok=1&scene=124&uin=MTk2NjU4NjExNQ%3D%3D&key=861420a46a8ac7f752fae2d5d95781a095d4479c2e3adca20375dd8b78091539732d1b85fcdb3c6302f3a112b74cc45da4f9d1efad387e0663d9acd01b99ab7285bf8533e119d6287610ca271df8f21c&pass_ticket=DO87H6ckGVLIlqKdfbfDspa266VK4C0rYUe8WX%2BPfXsSePh3Xcs6vm4yS9H3HES7&wxtoken=&appmsg_token=1054_uI2CQGtCaqerrjdxI0v9y7pvwepmN4laonJZbQ~~&x5=0&f=json'
# url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzI2MzE2NDczMw==&f=json&offset=0&count=10&is_ok=1&scene=124&uin=MTk2NjU4NjExNQ%3D%3D&key= e2ae4c71ebea1245c0f7b0d4d39d36618cf192cb75efd99c4ce2070ffcdbbf80962c1f3ab99030a1d60543e1c417a7f436e72394ae3831d00f8d3d03a82fa876cbc817b213a303b9c91824ca15342195&pass_ticket=DO87H6ckGVLIlqKdfbfDspa266VK4C0rYUe8WX%2BPfXsSePh3Xcs6vm4yS9H3HES7&wxtoken=&appmsg_token=1054_R1UOcIHN2ecewE2GkkkP7hnKSD-Sds7A2cO0_g~~&x5=0&f=json'
# url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MjM5NjAxOTU4MA==&f=json&offset=10&count=10&is_ok=1&scene=124&uin=MTk2NjU4NjExNQ%3D%3D&key=861420a46a8ac7f737306f1fd2ae2b35fea95b7dba38118fa4e7629eb800d1d5a80bc5d246fb3fa9042fc9b4284c5319dae3b15eb871a6c0010fea0598f1b7b4b796ae861131ebed8cea336ffb1a8a6e&pass_ticket=DO87H6ckGVLIlqKdfbfDspa266VK4C0rYUe8WX%2BPfXsSePh3Xcs6vm4yS9H3HES7&wxtoken=&appmsg_token=1054_xtsiHpxA5BHj6bznyz2Ao5XWiCENJASuQ5LA4Q~~&x5=0&f=json'
# url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MjM5NjAxOTU4MA==&f=json&offset=10&count=10&is_ok=1&scene=124&uin=MTk2NjU4NjExNQ%3D%3D&key=861420a46a8ac7f752fae2d5d95781a095d4479c2e3adca20375dd8b78091539732d1b85fcdb3c6302f3a112b74cc45da4f9d1efad387e0663d9acd01b99ab7285bf8533e119d6287610ca271df8f21c&pass_ticket=DO87H6ckGVLIlqKdfbfDspa266VK4C0rYUe8WX%2BPfXsSePh3Xcs6vm4yS9H3HES7&wxtoken=&appmsg_token=1054_xtsiHpxA5BHj6bznyz2Ao5XWiCENJASuQ5LA4Q~~&x5=0&f=json'

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
# }
#
# proxies = {'http': "http://119.146.249.160:23343"}
# res = requests.get(url, headers=headers, proxies=proxies)
# data = json.loads(res.text)
# next_offset = data["next_offset"]
# print(next_offset)
# data = (data["general_msg_list"])
# print(data)
# data = json.loads(data)
#
# data = (data["list"])
# for item in data:
#     print(item)
#
# url = 'https://mp.weixin.qq.com/mp/homepage?__biz=MzI2MzE2NDczMw==&hid=1&sn=82535620c0eac83006257862b2d9ebd8&scene=18&uin=MTk2NjU4NjExNQ%3D%3D&key=818087460639ae497360473aeaa56f36715e8b2e5c8746ae99bcda960c059e3bf69bb3c0b5ef3cea3773077e6923e24f624a0a41539968f6710d2b5e29bbfa8a35be71012d4288822065f9669b9ad5ed&devicetype=Windows+10&version=62080079&lang=zh_CN&ascene=7&pass_ticket=cgvQSnYbLLmxkLtIbV4XDmnxqr1rOu%2BTqmW6dqoVNx8o7%2BQ38jylRmWtlm3yT5Xs&winzoom=1&cid=0&begin=21&count=5&action=appmsg_list&f=json&r=0.7315866082017313&appmsg_token=1054_nKuiASNzIJWdFL6UrGlkDJLHAuAgiJAqoR6Uhg~~'
#
# headers = {
#     "Host": "mp.weixin.qq.com",
#     "Connection": "keep-alive",
#     "Content-Length": "0",
#     "Accept": "application/json",
#     "Origin": "https://mp.weixin.qq.com",
#     "X-Requested-With": "XMLHttpRequest",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1295.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat",
#     "Referer": "https://mp.weixin.qq.com/mp/homepage?__biz=MzI2MzE2NDczMw==&hid=1&sn=82535620c0eac83006257862b2d9ebd8&scene=18&uin=MTk2NjU4NjExNQ%3D%3D&key=818087460639ae497360473aeaa56f36715e8b2e5c8746ae99bcda960c059e3bf69bb3c0b5ef3cea3773077e6923e24f624a0a41539968f6710d2b5e29bbfa8a35be71012d4288822065f9669b9ad5ed&devicetype=Windows+10&version=62080079&lang=zh_CN&ascene=7&pass_ticket=cgvQSnYbLLmxkLtIbV4XDmnxqr1rOu%2BTqmW6dqoVNx8o7%2BQ38jylRmWtlm3yT5Xs&winzoom=1",
#     "Accept-Encoding": "gzip, deflate",
#     "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4",
#     "Cookie": "rewardsn=; wxtokenkey=777; wxuin=1966586115; devicetype=Windows10; version=62080079; lang=zh_CN; pass_ticket=cgvQSnYbLLmxkLtIbV4XDmnxqr1rOu+TqmW6dqoVNx8o7+Q38jylRmWtlm3yT5Xs; wap_sid2=CIPy3qkHElw4VGZBYVlQcDhSUTNnNEVvTlRNWmR1OXZ6cnlEZmlma0RsaDJRZWI2c0VJVFM3V1RVRmpOaWdyelU4d2VZczhKOUk3NzROQ2ZHQTJSbXZ4aHZNaUxMaDRFQUFBfjCCtYr0BTgMQJRO",
#
# }
# res = requests.post(url, headers=headers)
# print(res.text)

url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzI2MzE2NDczMw==&f=json&offset=0&count=10&is_ok=1&scene=124&uin=NjEyOTcyMDI4&key=48ac1fe873eb07259d800afc90f16356f4c1f74f6eab7d980af7ce4b62c9b769b17f0a761f3a355b5a23cbafb15fe8e73131c8914582c12ddef568f2a0090af9fbb1471f52b58d80b0e2dd9790bfebb3&pass_ticket=hpvx1RdJ7JcKxtCYs3dT%2FZhdeX1wJtZD0lBD%2BVF%2FLexAoru5DALpX%2BGULxIa5NXm&wxtoken=&appmsg_token=1054_58vnUYRzIYBCrrBRneI6Fpz2oAUKL1WuU1blng~~&x5=0&f=json'
URL = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MjM5NjAxOTU4MA==&f=json&offset=30&count=10&is_ok=1&scene=124&uin=NjEyOTcyMDI4&key=5ca46d607212cc7703871be35b193a973e9223c042c7e481d00ae1313ab6de509d11f96a5093c886eb6d8e586ab75a4b381db170016b258a7c40fbf284c5a231dd4eeb175fd67bf11ac2339a89433fb7&pass_ticket=hpvx1RdJ7JcKxtCYs3dT%2FZhdeX1wJtZD0lBD%2BVF%2FLexAoru5DALpX%2BGULxIa5NXm&wxtoken=&appmsg_token=1054_WXsMOJJbxNnKdA%252FamPPP9T6gnrFon91MT0zPdQ~~&x5=0&f=json'

headers = {
    # "Host": "mp.weixin.qq.com",
    # "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1295.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat",
    # "X-Requested-With": "XMLHttpRequest",
    # "Accept": "*/*",
    # "Referer": "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5NjAxOTU4MA==&scene=124&uin=NjEyOTcyMDI4&key=5ca46d607212cc7703871be35b193a973e9223c042c7e481d00ae1313ab6de509d11f96a5093c886eb6d8e586ab75a4b381db170016b258a7c40fbf284c5a231dd4eeb175fd67bf11ac2339a89433fb7&devicetype=Windows+10&version=62080079&lang=zh_CN&a8scene=7&pass_ticket=hpvx1RdJ7JcKxtCYs3dT%2FZhdeX1wJtZD0lBD%2BVF%2FLexAoru5DALpX%2BGULxIa5NXm&winzoom=1",
    # "Referer": "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI2MzE2NDczMw==&scene=124&uin=NjEyOTcyMDI4&key=b68e89182d72fe2f585529dd3d49b59ed346846f9e2327d9b0b9e38047ca66d582d79a19456b9c7cc67e7a673a1c20537f042e52e1a6dd620d544818ef580b3d1085cac44177267ed2ae65ca957dd2b9&devicetype=Windows+10&version=62080079&lang=zh_CN&a8scene=7&pass_ticket=hpvx1RdJ7JcKxtCYs3dT%2FZhdeX1wJtZD0lBD%2BVF%2FLexAoru5DALpX%2BGULxIa5NXm&winzoom=1",
    # "Accept-Encoding": "gzip, deflate",
    # "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4",
    # "Cookie": "rewardsn=; wxtokenkey=777; wxuin=612972028; devicetype=iPhoneiOS13.3.1; version=17000c26; lang=zh_CN; pass_ticket=hpvx1RdJ7JcKxtCYs3dT/ZhdeX1wJtZD0lBDVF/LexAoru5DALpXGULxIa5NXm; wap_sid2=CPzrpKQCElxyYVBaNVg2ZWVTcjN6RkZYa3VoMVNQRlFmUGMwY2NLcnJSSzZVNE5PYjhXdHQ1WEpjaGhuSjlqemNJcFJBSG9pa05EbHhJdlBsRElMTUdOSmtFTXJPeDRFQUFBfjCexor0BTgNQJVO",
    # "Cookie": "rewardsn=; wxtokenkey=777; wxuin=612972028; devicetype=iPhoneiOS13.3.1; version=17000c26; lang=zh_CN; pass_ticket=hpvx1RdJ7JcKxtCYs3dT/ZhdeX1wJtZD0lBDVF/LexAoru5DALpXGULxIa5NXm; wap_sid2=CPzrpKQCElxtNWg3UXRWS19CbDFIRi1CaF96c2dDZVVXdTBLT1NUbmprZng1Q01udlNlbTI5SFpJMnVsaWI2Y2NZX3VIaHBQZy1UaENKUHBWaTBwYW9WYkcxa294QjRFQUFBfjC7/Yr0BTgNQJVO"
    "Cookie": "rewardsn=; wxtokenkey=777; wxuin=612972028; devicetype=iPhoneiOS13.3.1; version=17000c26; lang=zh_CN; pass_ticket=hpvx1RdJ7JcKxtCYs3dT/ZhdeX1wJtZD0lBDVF/LexAoru5DALpXGULxIa5NXm; wap_sid2=CPzrpKQCElxtNWg3UXRWS19CbDFIRi1CaF96c2dDZVVXdTBLT1NUbmprZng1Q01udlNlbTI5SFpJMnVsaWI2Y2NZX3VIaHBQZy1UaENKUHBWaTBwYW9WYkcxa294QjRFQUFBfjC7/Yr0BTgNQJVO"


}

res = requests.get(url, headers=headers)
print(res.text)
# data = json.loads(res.text)
# print(data["next_offset"])




















