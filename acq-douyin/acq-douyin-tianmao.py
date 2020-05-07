# import requests
#
#
#
#
# requests.session()
#
#
# def get_tianmao_shopname(url):
#     headers = {
#         # "Connection": "keep-alive",
#         # "Pragma": "no-cache",
#         # "Cache-Control": "no-cache",
#         # "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
#         # "X-Requested-With": "XMLHttpRequest",
#         # "Content-Type": "application/x-www-form-urlencoded",
#         # "Referer": "https://music.163.com/",
#         # "Accept-Encoding": "gzip, deflate, br",
#         # "Accept-Language": "zh-CN,zh;q=0.9",
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
#     }
#
#
#
#
#     headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
#     "Cookie": "_ga=GA1.2.1855430798.1461857641; _octo=GH1.1.783519559.1525492869; tz=Asia%2FShanghai; logged_in=no; _gat=1; _gh_sess=TTZZNnVPOTRwTlI2YW1UOWFqTUZwa1JHVENFOVpjYWxoekJLbS9GTGFQQkR4ODZVSTIrV1NTWUFQS0dETUhURmg4YVR3bGxjV1hJT2dMZ2NIOEptZlREUUxrOXV0eG1EcG5kUi9adUZQamFpWmxmMHVhY04vckJVWkxXbkNVa3ZHNCtjekF2WEVnMGVzaElqMnBpVUIvVGVSNzJmdjNQMFFxYWpONE1HMks2eDhpVzZ0Wk9ZQUZLMVJOOTRsYXJWUjV6VUNmRFhyaHlYczUzdUozSWR5M210akh3dkcvaXRhY2ZmanRNRC9IbElUMm5OSmkzVDhtbEwvSEdGWFMvd0xySWIxcFRrbGZ0RDQwQit5eGUvaGZKdWp5U1dYSnZ0VzRRb1FqUThZZXlreTBNU1RicUhheGJGQjFRcDlnN1N2b2RXRXRsT21lRFB5Q3RFSHQ3V1FpR05QSlo2TVBic2o3R0hDaUZOSmhST0l2ZXdabHVzVEdBcGdMRWpiS2lXME5jOWV2WTFJckFGUXI2WHpjeTZ5ZXpXMUJvSXlpdmRpZWNONUhFejFUMD0tLVhyaTZJdlZBMUdNWnBNU0QrWDFFQ1E9PQ%3D%3D--ab7943f35d872df42bb86b8086b5cec50d3ef0ce"
#     }
#     post_data = {
#     "commit": "Sign in",
#     "utf8": "✓",
#     "authenticity_token": "ookie: cna=9S+uEoBdokcCAdpYG4whEJSq; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; lid=%E4%B8%80%E5%A4%9C1%E6%89%81%E8%88%9F; x=__ll%3D-1%26_ato%3D0; cq=ccp%3D1; hng=CN%7Czh-CN%7CCNY%7C156; enc=VrJIBrOw54wqQ%2FVSyQ36Gj65%2Fqgi26hllFrc9rr%2BlczZLdI4kAaoo4rL3OMOQJnl538B4cRZBOuAxIGBeTcXHA%3D%3D; t=8762ee6844e4c99f1ea67c5ae4d7185a; tracknick=%5Cu4E00%5Cu591C1%5Cu6241%5Cu821F; _tb_token_=f43dbbeb3b031; cookie2=1079049a26c693631f50a9d86926292b; _m_h5_tk=ccac32e899cdfcffdef8153b0f28de9d_1573204259386; _m_h5_tk_enc=ab12674cf748679fc66bb724a0b603a7; pnm_cku822=098%23E1hv%2FpvUvbpvUvCkvvvvvjiPRsMUQjDPn2M9sjthPmP90jDvnL5Ztj3nn25wtj1UiQhvCvvvpZpPvpvhvv2MMQyCvhQm%2Fd7ljaAfV1Oqb64B9Cka%2BfvsxI2hVC6t%2BFBCAfyp%2Bu64jomxfBuKDBh%2BoIkQrEgfVjxV%2Bnezr2UpwhKn3feAhE31oGexRdItn0vHKphv8vvvphvvvvvvvvCj1Qvv9xZvvhNjvvvmjvvvBGwvvvUUvvCj1Qvvv9kivpvUvvCCbAeGGlTEvpvVvpCmpYshvphvC9mvphvvv2yCvvpvvhCv; l=dBPuTEUVv_ElgaC9BOCgCuI8UN_O7IRfguPRwdfMi_5dq18_SfQOkQt3oeJ6cjWcGOYB4z6vzNeTmeUQ-yJ_XMJA-9cdvdHDBef..; isg=BMPDPZu7mu-rAlF2IB1piUThUoetkFV3mSl-OfWgDyKZtOLWfQh7y7ouLgRfFK9y",
#     # "login": "czwspider",
#     # "password": "qwer1234"
#     }
#
#
#     session = requests.session()
# #    2. 发送请求获取响应
#     response = session.get(url,headers=headers)
#     response.encoding = 'gbk'
#     print(response.text)
#     # res = requests.get(url,headers=headers)
#     # res.encoding = 'gbk'
#     # print(res.text)
#
# #
# #
# get_tianmao_shopname('https://s.click.taobao.com/t?e=m%3D2%26s%3DQCxeO3rjJC9w4vFB6t2Z2ueEDrYVVa64yK8Cckff7TVRAdhuF14FMVKbWjSHff6A1aH1Hk3GeOjCLbnHYgDO7RXvAaHY+k4sE1p8UKWvOoOYHHoEKDSsVB8X7G7Q37BaEHESUfc7ygHrmWdQF0imwYwe6/tGg2/RSyiL934V8t7Ny6VfD8aHxJ6P/jo9mSm0fWsUjZoD5RCiPjN8FPKfVoLiglfzF7Nrm/AqrVg3iolmYKmPQjlXgib4FRL6yn47QLQtqj2NQCM7Qq3IsVviSLpPcC+jxcBwIYULNg46oBA%3D&amp;union_lens=lensId:0b0fc0d4_0c42_16e38989d39_2d47&amp;xId=HfEnx5soKtEOSU6xpxHyXf5L2yvJ5eyqro75Yu86HVvwAc6nBXSnV71dtNhBUvNRcTRx2Z74G3KFfywtwOixkM&amp;union_lens=lensId:0b1b5435_0cca_16e38989d3b_d834&amp;utm_campaign=client_share&amp;app=aweme&amp;utm_medium=ios&amp;tt_from=copy&amp;utm_source=copy&amp;ref=&amp;et=trFa2PhmCJKS%2FG53hCfeuDhoOyNq6XyZ')
# # get_tianmao_shopname('https://detail.tmall.com/item.htm?id=596670968366&ali_trackid=2:mm_26846744_880750142_109471300057:1573194009_171_694674820&ak=24698276')
#
#
# import execjs
#
# # 读取js文件
# with open('douyin.js', encoding='utf-8') as f:
#     js = f.read()
# #
# # 通过compile命令转成一个js对象
# docjs = execjs.compile(js)
#
# # 调用function方法
# res = docjs.call('bol')
# print(res)

# 调用变量方法
# res = docjs.eval('asd')
# print(res)


import requests
#
#
def get_redirect_url():
    # 重定向前的链接
    # url = 'https://s.click.taobao.com/t?e=m%3D2%26s%3DQCxeO3rjJC9w4vFB6t2Z2ueEDrYVVa64yK8Cckff7TVRAdhuF14FMVKbWjSHff6A1aH1Hk3GeOjCLbnHYgDO7RXvAaHY+k4sE1p8UKWvOoOYHHoEKDSsVB8X7G7Q37BaEHESUfc7ygHrmWdQF0imwYwe6/tGg2/RSyiL934V8t7Ny6VfD8aHxJ6P/jo9mSm0fWsUjZoD5RCiPjN8FPKfVoLiglfzF7Nrm/AqrVg3iolmYKmPQjlXgib4FRL6yn47QLQtqj2NQCM7Qq3IsVviSLpPcC+jxcBwIYULNg46oBA%3D&amp;union_lens=lensId:0b0fc0d4_0c42_16e38989d39_2d47&amp;xId=HfEnx5soKtEOSU6xpxHyXf5L2yvJ5eyqro75Yu86HVvwAc6nBXSnV71dtNhBUvNRcTRx2Z74G3KFfywtwOixkM&amp;union_lens=lensId:0b1b5435_0cca_16e38989d3b_d834&amp;utm_campaign=client_share&amp;app=aweme&amp;utm_medium=ios&amp;tt_from=copy&amp;utm_source=copy&amp;ref=&amp;et=trFa2PhmCJKS%2FG53hCfeuDhoOyNq6XyZ'
    # url = 'https://detail.tmall.com/item.htm?id=596670968366&ali_trackid=2:mm_26846744_880750142_109471300057:1577778123_194_1551527756&ak=24698276'
    url = 'https://uland.taobao.com/coupon/edetail?e=quHuTU1UBUwE%2BdAb1JoOOj3JlHUoEyKqR6h47zF5ZCrqa9POAQ9x7D%2BNIklD12%2FSPxx%2FqKUBx9LWZ9Q3CD37tKtxutraZgdS%2FnNA6NfsJbiBA9I59CpFie%2FDpAZTKJqwnED0eMMe7%2B7Z7tLp0IPlxrmykeWYbo0f%2B9AVZ6pYAmKVygApNPKk7Odth9k8bqqSHKTgBzHkoM7XTQC0vfau6E%2F9Zk7cDx8UHWt32Au%2FrGK%2FFWQpcIiqmHui%2Fn%2FQ7Z5VWyeDUYYQMsaz%2BEEIX1kmAg%3D%3D&traceId=0b0b7c4615773535823886517e&union_lens=lensId:0b014932_720e_16f4199976a_6fc5&xId=z5LIs1XkEjH7cahaBrNDIsh8ShBe9jDU4G42vCpe1GA3ieCAUxSt6rL2adPv8hmc2o5bHQbHI1reuBPOsBMmf6&union_lens=lensId:0b0f8444_1366_16f4199976c_ea0e'
    # 请求头，这里我设置了浏览器代理
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Cookie': 'cna=9S+uEoBdokcCAdpYG4whEJSq; miid=579824039327804150; enc=VrJIBrOw54wqQ%2FVSyQ36Gj65%2Fqgi26hllFrc9rr%2BlczZLdI4kAaoo4rL3OMOQJnl538B4cRZBOuAxIGBeTcXHA%3D%3D; tracknick=%5Cu4E00%5Cu591C1%5Cu6241%5Cu821F; tg=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; _cc_=WqG3DMC9EA%3D%3D; cookie2=1079049a26c693631f50a9d86926292b; t=8762ee6844e4c99f1ea67c5ae4d7185a; _tb_token_=f43dbbeb3b031; v=0; uc1=cookie14=UoTbnrlxzH%2FlyQ%3D%3D; mt=ci=-1_0; _m_h5_tk=b6d2ac486626d2c4571841598455e2a5_1573203958198; _m_h5_tk_enc=a2b9b23a839ffe848775f2802baf5c96; _fbp=fb.1.1573193883254.1556323589; isg=BIuLzXv0UpckW4kuKCUUvypdGi-1iJ2vEdGGwf2ILko0HKt-hPAv8in98hzyPPea; l=dBQBFrzIv_ElpP5TBOCg5uI8UN_TtIRAguPRwdfMi_5Zi_-dBn7OkQtOuEJ6cjWft3Tp4z6vzNe9-etlwKrNApDgcGAwsxDc.'
    }
    # 请求网页
    response = requests.get(url, headers=headers)
    print(response.text)
    history_list = response.history
    print(history_list)
    # print(response.status_code)  # 打印响应的状态码
    print(response.url)  # 打印重定向后的网址
    # 返回重定向后的网址
    return response.url


if __name__ == '__main__':

    url = get_redirect_url()
    # res = requests.get(url)
    # print(res.text)