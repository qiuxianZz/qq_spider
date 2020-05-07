import json
import re
import time

import execjs
import requests


def get_sign(id, t):
    """_signature"""
    print(id, t)
    with open('sign.js', 'r') as f:
        js = f.read()
    ctx = execjs.compile(js)
    return ctx.call('a', id, t)


a = get_sign(111572755092, 0)
print(a)

uid_list = [51138452718, 102227680616, 1393804440774765, 5776431832, 5931633599, 2027123749436456, 3522478669571448,
            5855187792, 111572755092, 4428429842721358, 5905715301]

max_behot_time = 0


def get_content(uid, max_time):
    url = 'https://www.toutiao.com/c/user/article/?page_type=1&user_id={}&max_behot_time={}&count=20&as=A1252EB0B1DB52F&cp=5E01FBC5522F9E1'.format(
        uid, max_time)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Referer": "https://www.toutiao.com/c/user/",
        "Cookie": 'uuid="w:912057c54847457eb48b69d637117cdc"; _ga=GA1.2.750742914.1512468789; tt_webid=6496003991339943438; WEATHER_CITY=%E5%8C%97%E4%BA%AC; csrftoken=5d5451cff324d51738a43be755409d3f; tt_webid=6496003991339943438; UM_distinctid=16bd0953213a12-08ca4cb1e5e02e-b781636-1fa400-16bd0953214703; CNZZDATA1259612802=1368380591-1512950320-https%253A%252F%252Fwww.newrank.cn%252F%7C1571894378; tt_track_id=5b300642d21cf37a5b867ab978f257c5; __tasessionId=q91xdrcwm1577348600504'
    }
    print(url)
    res = requests.get(url, headers=header)
    json_res = json.loads(res.text)
    global max_behot_time
    try:
        max_behot_time = json_res["next"]['max_behot_time']
        print(max_behot_time)
    except:
        return "stop"
    data = json_res["data"]
    for i in data:
        print(i)
        # print(i["item_id"])
        # get_toutiao_content(i["item_id"])

    if len(data) < 20:
        return True
    else:
        return False


#
def get_toutiao_content(id):
    url = "https://www.toutiao.com/group/{}/".format(id)
    # url = "https://www.toutiao.com/a6773807279578808840/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Referer": "https://www.toutiao.com/c/user/",
        "Cookie": 'uuid="w:912057c54847457eb48b69d637117cdc"; _ga=GA1.2.750742914.1512468789; tt_webid=6496003991339943438; WEATHER_CITY=%E5%8C%97%E4%BA%AC; csrftoken=5d5451cff324d51738a43be755409d3f; tt_webid=6496003991339943438; UM_distinctid=16bd0953213a12-08ca4cb1e5e02e-b781636-1fa400-16bd0953214703; CNZZDATA1259612802=1368380591-1512950320-https%253A%252F%252Fwww.newrank.cn%252F%7C1571894378; tt_track_id=5b300642d21cf37a5b867ab978f257c5; __tasessionId=q91xdrcwm1577348600504'
    }
    print(url)
    res = requests.get(url, headers=header)
    patterns = re.compile('content: (.*?);\'.slice', re.S)
    con = patterns.findall(res.text)
    # str = re.sub("[u03CpstrongE2FbqdivclaxDmhefw\!\%\[\]\,\\\\'\&\;\#\-\_:.. ]", "", con[0])
    print(con[0])


while True:
    con = get_content(53335521365, max_behot_time)
    if con == True:
        break
    elif con == "stop":
        time.sleep(60)
