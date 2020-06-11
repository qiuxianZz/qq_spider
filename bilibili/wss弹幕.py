# import numpy as np
# from websocket import create_connection
# import requests
# import re
# import struct
# import json
#
#
#
# # url="https://api.live.bilibili.com/room/v1/Danmu/getConf?room_id=64213&platform=pc&player=web"
# # headers={
# # 'Accept-Encoding': 'gzip, deflate',
# # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
# # }
# # res=requests.get(url,headers=headers,verify = False)
# # key=json.loads(res.text)["data"]["token"]
#
#
#
#
# # print(ws)
# # data="................"+{"uid":"403495084","roomid":"21715657","platfrom":"web","clientver":"1.11.1","type":"2","key":key}
# # data={"uid":403495084,"roomid":21715657,"protover":2,"platform":"web","clientver":"1.11.1","type":2,"key":"ZfGn1-rlgDgda4gpTf_oJ5POmmdug6wR4tE3v4GrmQLqM3a09KXd910fj5rPotZXgwlA29q8txg9zdhwnE-f68TkTnIzFQTfIW--_WwI8LmrZ3gUPqEUa_M="}
# #
# #
# # bt = [0x00, 0x00,0x00, 0xF0, 0x00, 0x10, 0x00, 0x01, 0x00, 0x00, 0x00, 0x07, 0x00, 0x00, 0x00, 0x01]
# # for x in str(data):
# #
# #     bt.append(str_to_hex(x))
# # print(bt)
# # data = {"uid":"403495084","roomid":"21715657","platfrom":"web","clientver":"1.11.1","type":"2","key":key}
# # data=np.array([],dtype='uint8')
# # print(data.tostring().decode("utf-8"))
# data = json.dumps({"uid":0,"roomid":64213,"protover":2,"platfrom":"web","clientver":"1.11.1","type":2,"key":'P-iy8FK9pR1UEF1NMuENHZtHL2bVIb4kfE82ZmHjvT-6BNjNpts3jf_bUN8uoN52DWnzzJi9uWmaMAJ2HYNAYfBUryZR2ylQsAHNQlxpfIVVRF1R'}, separators=(',', ':'))
# def _pack_socket_data(data_length, data):
#     _data = data.encode('utf-8')
#     _send_bytes = struct.pack('>IHHII', data_length, 16,1,7,1)
#     return _send_bytes + _data
#
# total_length = 16 + len(data)
# data1 = _pack_socket_data(total_length, data)
# print(data1)
#
#
#
# import time
# wss="wss://tx-sh-live-comet-02.chat.bilibili.com/sub"
# #wss="wss://tx-gz-live-comet-02.chat.bilibili.com/sub"
#
# ws = create_connection(wss)
#
#
# # data=np.array(bt)
# # print(data)
# # print(data.tostring().decode("utf-8"))
# ws.send(data1)
# #
# result = ws.recv()
# # print(result.decode("utf-8"))
#
# # result = ws.recv()
#
# import zlib
# result = ws.recv()
# # x=result.dencode('hex')
# print(result)
# # print(x)
# # x=str(result, encoding = "utf8")
# # print(x)
# # result = ws.recv()
# # # x=result.dencode('hex')
# # print(result)
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : liyongbin


#import websockets
import json
import asyncio
import logging
import re

import requests
import struct
from datetime import datetime
from aiowebsocket.converses import AioWebSocket

url="https://api.live.bilibili.com/room/v1/Danmu/getConf?room_id=64213&platform=pc&player=web"
headers={
'Accept-Encoding': 'gzip, deflate',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
}
res=requests.get(url,headers=headers,verify = False)
key=json.loads(res.text)["data"]["token"]

header_dict = {
    "uid": 0,
    "roomid":64213,
    "protove":2,
    "platform":"web",
    "clientver":"1.11.0",
    "type":2,
    "key":key
}


def _pack_socket_data(data_length, data):
    _data = data.encode('utf-8')
    _send_bytes = struct.pack('>IHHII', data_length, 16,1,7,1)
    return _send_bytes + _data

total_length = 16 + len(json.dumps(header_dict))
data1 = _pack_socket_data(total_length, json.dumps(header_dict))

async def startup(uri):
    async with AioWebSocket(uri) as aws:
        converse = aws.manipulator
        # 客户端给服务端发送消息
        await converse.send(data1)
        while True:
            mes = await converse.receive()
            try:
                print(str(mes,"utf-8"))
            except:
                print(mes)
            # print('{time}-Client receive: {rec}'
            #       .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes))
if __name__ == '__main__':

    remote = 'wss://tx-sh-live-comet-02.chat.bilibili.com/sub'
    try:
        asyncio.get_event_loop().run_until_complete(startup(remote))
    except KeyboardInterrupt as exc:
        print('Quit.')


