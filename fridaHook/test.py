# -*- coding: utf-8 -*-

# @Create   : 2017/11/29 11:10
# @Author   : Anxidn
# @EMail    : xiangcaidong@newrank.cn
# @File     : test1.py


import frida
import sys
import json

import os

def cmd_row(input):
    p = os.popen(input)
    print(p)

def on_message(message, data):
    print(json.dumps(message))

# cmd_row("adb forward tcp:21503 tcp:21503")
# cmd_row("adb forward tcp:21503 tcp:21503")
cmd_row("adb -s 04879f7e25229ed0 forward tcp:21503 tcp:21503")
cmd_row("adb -s 04879f7e25229ed0 forward tcp:21503 tcp:21503")

# rdev = frida.get_remote_device()
rdev = frida.get_usb_device()
# front_app = rdev.get_frontmost_application()
# print(front_app)
# session = rdev.attach("com.xunmeng.pinduoduo")
# processes = rdev.enumerate_processes()
# session = rdev.attach("com.tencent.mm")r
# session = rdev.attach("com.tencent.weread")

# session = rdev.attach("com.tencent.reading")
# session = rdev.attach("com.xingin.xhs")
# session = rdev.attach("com.ss.android.ugc.aweme")
# session = rdev.attach("com.artist.wxmanager:upload")
# session =  rdev.attach("com.smile.gifmaker")
# session =  rdev.attach("com.jifen.qukan")
# session = rdev.attach("com.smile.gifmaker")
# session = rdev.attach("com.dahua.bluetoothunlock")
session = rdev.attach("com.cmbchina.ccd.pluto.cmbActivity")
file_object = open('./ks7.4.js')
# file_object = open('./douyin/douyin1010.js')
# script = session.create_script(unicode(file_object.read(), "utf-8"))
script = session.create_script(file_object.read())
file_object.close()
script.on('message',on_message)
script.load()
sys.stdin.read()
