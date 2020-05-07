import time
from time import sleep

import requests
import  json
url = "https://api3-normal-c-lf.snssdk.com/api/feed/profile/v1/?category=profile_all&visited_uid={}&stream_api_version=88&count=20&offset={}&client_extra_params=%7B%22playparam%22%3A%22codec_type%3A0%22%7D&iid=110986401453&device_id=71425677262&ac=wifi&mac_address=1C%3A1B%3A0D%3AA3%3AD0%3AE1&channel=xiaomi&aid=13&app_name=news_article&version_code=767&version_name=7.6.7&device_platform=android&ab_version=1419046%2C668775%2C1529251%2C1556060%2C1190522%2C1157750%2C1157634%2C1419597%2C1439625%2C1469498%2C1592803%2C1484967%2C1576656%2C1590978%2C1593455%2C668779%2C1417596%2C662099%2C668774%2C1546040%2C1396152%2C857803%2C660830%2C1526645%2C662176%2C1555753%2C1553980%2C1609889&ab_feature=102749%2C94563&ssmix=a&device_type=OPPO+R17&device_brand=OPPO&language=zh&os_api=22&os_version=5.1.1&uuid=866174504020823&openudid=1c1b0da3d0e14991&manifest_version_code=7670&resolution=900*1600&dpi=320&update_version_code=76711&_rticket=1586314948201&plugin=0&tma_jssdk_version=1.58.0.3&pos=5r_-9Onkv6e_eDMBewU4eCUfv7G_8fLz-vTp6Pn4v6esrKizqKulqKylq6qurKWppKWxv_H86fTp6Pn4v6evqrOkpKqlraiqqKukqqyvqauxv_zw_O3e9Onkv6e_eDMBewU4eCUfv7G__PD87dHy8_r06ej5-L-nrKyos6irpaispauqrqylqaSlsb_88Pzt0fzp9Ono-fi_p6-qs6SkqqWtqKqoq6SqrK-pq-A%3D&rom_version=coloros__r17-user+5.1.1+nmf26x+500200323+release-keys&cdid=45c8963a-357e-48ca-be01-fcf73a1b2c7c"
# url = 'https://is.snssdk.com/api/feed/profile/v1/?category=profile_all&visited_uid={}&stream_api_version=88&count=20&offset={}&client_extra_params=%7B%22playparam%22%3A%22codec_type%3A1%22%7D&iid=108985447641&device_id=71237989952&ac=wifi&mac_address=dc%3A68%3Ad4%3A78%3A95%3A65&channel=baidu_0411&aid=13&app_name=news_article&version_code=755&version_name=7.5.5&device_platform=android&ab_version=1629316%2C1612012%2C1419041%2C668775%2C1630876%2C1469462%2C1529246%2C1190525%2C1157750%2C1419598%2C1439625%2C1629530%2C1628175%2C1469498%2C1484964%2C1576656%2C1629326%2C668779%2C662099%2C1613263%2C668774%2C857804%2C1624276%2C660830%2C1479497%2C1598769%2C1587644%2C662176%2C1555753&ab_group=100167&ab_feature=102749%2C94563&ssmix=a&device_type=OPPO+R11+Plus&device_brand=OPPO&language=zh&os_api=22&os_version=5.1.1&uuid=861143247784164&openudid=0425eebe3326b9c2&manifest_version_code=7550&resolution=720*1280&dpi=192&update_version_code=75515&_rticket=1586917609788&plugin=18762&tma_jssdk_version=1.46.0.12&rom_version=coloros__oppo-user+5.1.1+20171130.276299+release-keys&cdid=45355aa4-4a66-4624-a266-7660a8ce22e9'
header = {
    "User-Agent": "com.ss.android.article.news/7670 (Linux; U; Android 5.1.1; zh_CN; OPPO R17; Build/NMF26X; Cronet/TTNetVersion:3154e555 2020-03-04 QuicVersion:8fc8a2f3 2020-03-02"
    # "User-Agent": "ttnet okhttp/3.10.0.2"

}


def get_tt_list(uid, offset):

    res = requests.get(url.format(uid, offset), headers=header)
    print(res.text)
    data = json.loads(res.text)
    offset = data["offset"]
    return offset


offset = "0"
while True:
    offset = get_tt_list('6029241157',offset)
    time.sleep(3)
