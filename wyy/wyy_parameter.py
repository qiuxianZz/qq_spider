import urllib.request
import http.cookiejar
import urllib.parse
import json
import time
import codecs

import requests
from Crypto.Cipher import  AES
import base64
import os



def get_encSecKey():
    #获取encSecKey
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey



def get_params(page):
    #获取encText，也就是params\

    second_param = "010001"
    #第三个参数
    third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
    #第四个参数
    forth_param = "0CoJUm6Qyw8W8jud"



    iv = "0102030405060708"
    first_key = forth_param
    second_key = 'F' * 16
    if page == 0:
        first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
    else:
        offset = str((page - 1) * 20)
        first_param = '{rid:"", offset:"%s", total:"%s", limit:"20", csrf_token:""}' % (offset, 'false')
    encText = AES_encrypt(first_param, first_key, iv)
    encText = AES_encrypt(encText.decode('utf-8'), second_key, iv)
    return encText

def AES_encrypt( text, key, iv):
    #AES加密
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    encrypt_text = encryptor.encrypt(text.encode('utf-8'))
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text



def get_json(id):
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_{}'.format(id)
    data = {
        'params': get_params(1),
        'encSecKey': get_encSecKey(),
    }
    # print(data)
    Headers = {
        'Accept': "*/*",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Connection': "keep-alive",
        'Host': "music.163.com",
        'User-Agent':"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"

    }
    # print(data)
    res = requests.post(url,data=data,headers=Headers)
    # print(res.text)
    json_res = json.loads(res.text)
    # print(id,json_res)
    return (json_res['total'])







# def get_json( url):
#     # post所含的参数
#     data = {
#         'params': get_params(1),
#         'encSecKey': get_encSecKey(),
#     }
#     Headers = {
#         'Accept': "*/*",
#         'Accept-Language': "zh-CN,zh;q=0.9",
#         'Connection': "keep-alive",
#         'Host': "music.163.com",
#         'User-Agent':"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
#
#     }
#     # 对post编码转换
#     postData = urllib.parse.urlencode(data).encode('utf8')
#     try:
#         #发出一个请求
#         request = urllib.request.Request(url,postData,Headers)
#     except urllib.error.HTTPError as e:
#         print(e.code)
#         print(e.read().decode("utf8"))
#     #得到响应
#     response = urllib.request.urlopen(request)
#     #需要将响应中的内容用read读取出来获得网页代码，网页编码为utf-8
#     content = response.read().decode("utf8")
#     #返回获得的网页内容
#     # print(content)
#     return content










# print(get_json(327419))