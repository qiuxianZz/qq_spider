import json
import random
import time

import requests
from fake_useragent import UserAgent

min_time = 1578844800
max_time = 1579363200
num = 0
sleep = [0, ]


def test():
    url = 'https://is-lq.snssdk.com/api/feed/profile/v1/?category=profile_all&visited_uid=3200725091&stream_api_version=47&count=20&offset=0&channel=lite2_tengxun&aid=35&app_name=news_article_lite&version_code=728&device_platform=android&device_type=MI+6&os_version=5.1.1'
          # 'https://is-lq.snssdk.com/api/feed/profile/v1/?category=profile_all&visited_uid=5954781019&stream_api_version=47&count=20&offset=1579135528915&client_extra_params=%7B%7D&iid=99543603066&device_id=69809116561&ac=wifi&mac_address=1C%3A1B%3A0D%3AA3%3AD0%3AE1&channel=lite_xiaomi&aid=35&app_name=news_article_lite&version_code=730&version_name=7.3.0&device_platform=android&ab_version=668905%2C668907%2C808414%2C668908%2C668904%2C668906%2C1427333%2C668903%2C1259058%2C928942%2C1322036%2C1335187%2C1355485%2C1355391&ab_client=a1%2Cc2%2Ce1%2Cf2%2Cg2%2Cf7&ab_feature=z1&abflag=3&ssmix=a&device_type=MI+6&device_brand=Xiaomi&language=zh&os_api=22&os_version=5.1.1&uuid=863254010282712&openudid=1c1b0da3d0e14487&manifest_version_code=730&resolution=900*1600&dpi=320&update_version_code=73005&_rticket=1579138074520&sa_enable=0&tma_jssdk_version=1.49.0.4&lite_qi_enable=1&rom_version=22&plugin_state=2412994591&cdid=47750a50-6f32-417c-9812-d6972dd920fb'
    header = {
        # 'Accept': 'image/webp,image/*;q=0.8',
        'User-Agent': 'News/6.9.8.36 CFNetwork/975.0.3 Darwin/18.2.0',
        # "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; MI 6 Build/NMF26X) NewsArticle/7.2.8 cronet/TTNetVersion:4df3ca9d 2019-11-25",
        # 'Accept-Language': 'zh-cn'

    }
    res = requests.get(url, headers=header)
    data = json.loads(res.text)
    if data["message"] != "sorry, unkown error":
        return 'yes'


def get_toutiao_app_data(uid, offset):
    # url = 'https://is-lq.snssdk.com/api/feed/profile/v1/?category=profile_all&visited_uid={}&stream_api_version=47&count=20&offset={}&channel=lite2_tengxun&aid=35&app_name=news_article_lite&version_code=728&device_platform=android&device_type=MI+6&os_version=5.1.1'.format(
    #     uid, offset)
    # url = 'https://lf-hl.snssdk.com/api/feed/profile/v1/?category=profile_all&visited_uid={}&stream_api_version=47&count=20&offset={}&client_extra_params=%7B%7D&iid=99612913034&device_id=70481541210&ac=wifi&mac_address=1C%3A1B%3A0D%3AA3%3AD0%3AE1&channel=lite_xiaomi&aid=35&app_name=news_article_lite&version_code=730&version_name=7.3.0&device_platform=android&ab_version=668906%2C1404962%2C1445060%2C668903%2C668905%2C668907%2C808414%2C772542%2C1445269%2C1378618%2C1446839%2C668908%2C668904%2C928942%2C1322036%2C1335187%2C1355485%2C1355391&ab_client=a1%2Cc2%2Ce1%2Cf2%2Cg2%2Cf7&ab_feature=z1&abflag=3&ssmix=a&device_type=MI+9&device_brand=Xiaomi&language=zh&os_api=22&os_version=5.1.1&uuid=863254881120827&openudid=1c1b0da3d0e18717&manifest_version_code=730&resolution=900*1600&dpi=320&update_version_code=73005&_rticket=1579418362689&sa_enable=0&tma_jssdk_version=1.49.0.6&lite_qi_enable=1&rom_version=22&plugin_state=2412994591&cdid=0016cd39-0bb9-4e5e-90cb-27e63156ff29'.format(uid,offset)
    url = 'https://lf-hl.snssdk.com/api/feed/profile/v1/?category=profile_all&visited_uid={}&stream_api_version=47&count=20&offset={}&client_extra_params=%7B%7D&iid=99612913034&device_id=70481541210&ac=wifi&mac_address=1C%3A1B%3A0D%3AA3%3AD0%3AE1&channel=lite_xiaomi&aid=35&app_name=news_article_lite&version_code=730&version_name=7.3.0&device_platform=android&ab_version=668905%2C668907%2C808414%2C772542%2C1445269%2C1378618%2C1446839%2C668908%2C668904%2C668906%2C1404962%2C1445063%2C668903%2C928942%2C1322036%2C1335187%2C1355485%2C1355391&ab_client=a1%2Cc2%2Ce1%2Cf2%2Cg2%2Cf7&ab_feature=z1&abflag=3&ssmix=a&device_type=MI+9&device_brand=Xiaomi&language=zh&os_api=22&os_version=5.1.1&uuid=863254881120827&openudid=1c1b0da3d0e18717&manifest_version_code=730&resolution=900*1600&dpi=320&update_version_code=73005&_rticket=1579418877218&https://lf-hl.snssdk.com/api/feed/profile/v1/?category=profile_all&visited_uid=5954781019&stream_api_version=47&count=20&offset=1579417744029&client_extra_params=%7B%7D&iid=99612913034&device_id=70481541210&ac=wifi&mac_address=1C%3A1B%3A0D%3AA3%3AD0%3AE1&channel=lite_xiaomi&aid=35&app_name=news_article_lite&version_code=730&version_name=7.3.0&device_platform=android&ab_version=668905%2C668907%2C808414%2C772542%2C1445269%2C1378618%2C1446839%2C668908%2C668904%2C668906%2C1404962%2C1445063%2C668903%2C928942%2C1322036%2C1335187%2C1355485%2C1355391&ab_client=a1%2Cc2%2Ce1%2Cf2%2Cg2%2Cf7&ab_feature=z1&abflag=3&ssmix=a&device_type=MI+9&device_brand=Xiaomi&language=zh&os_api=22&os_version=5.1.1&uuid=863254881120827&openudid=1c1b0da3d0e18717&manifest_version_code=730&resolution=900*1600&dpi=320&update_version_code=73005&_rticket=1579418877218&plugin_state=2227314707&sa_enable=0&lite_qi_enable=1&rom_version=22&cdid=db90942a-c1d7-4859-b3ac-36386aa30bb7=2227314707&sa_enable=0&lite_qi_enable=1&rom_version=22&cdid=db90942a-c1d7-4859-b3ac-36386aa30bb7'.format(uid,offset)


    ua = UserAgent()
    header = {
        # "Host": "is-lq.snssdk.com",
        # "Connection": "keep-alive",
        # "Cookie": "install_id=97744175209; ttreq=1$e18e6b32c8eecb12055a39314bccdb00780674e8; odin_tt=764d713373776b67353378566c78395acda96fceeb00c6b395df96b3fb04721b60eb4fdf30a22cab0d0e828b974d7513d3af95e36873c5aa6530849d0d85afdf",
        # "X-SS-REQ-TICKET": "1578022377291",
        # "passport-sdk-version": "9",
        # "sdk-version": "2",
        # "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; MI 6 Build/NMF26X) NewsArticle/7.2.8 cronet/TTNetVersion:4df3ca9d 2019-11-25",
        # "User-Agent":"Mozilla/5.0 (Linux;u;Android 4.2.2;zh-cn;) AppleWebKit/534.46 (KHTML,likeGecko) Version/5.1 Mobile Safari/10600.6.3"
        # 'User-Agent':ua.random,
        # "x-tt-trace-id": "00-697698df0a1040f29591d34d0ad60023-697698df0a1040f2-01",
        # "Accept-Encoding": "gzip, deflate",
        # "X-Gorgon": "040100bd40057911a16ffc7137250d8e5fe083451c638240d49e",
        # "X-Khronos": "1578022377",
        'Accept': 'image/webp,image/*;q=0.8',
        'User-Agent': 'News/6.9.8.36 CFNetwork/975.0.3 Darwin/18.2.0',
        # "User-Agent": "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI 5s Build/MXB48T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.1",
        'Accept-Language': 'zh-cn'

    }
    # res = requests.get('http://115.29.174.137:3333/xdn/proxies/get?count=10&type=0&all=0')
    # proxies_list = json.loads(res.text)
    # proxies = (proxies_list['RESULT'])
    # proxies = [{"ip":"180.127.10.170","port":"47256"},{"ip":"121.226.44.197","port":"22689"},{"ip":"171.11.197.33","port":"31089"},{"ip":"116.209.62.128","port":"29818"},{"ip":"183.51.190.104","port":"44683"},{"ip":"117.169.78.54","port":"18929"},{"ip":"117.169.78.54","port":"17176"},{"ip":"117.169.78.54","port":"14252"},{"ip":"117.169.78.54","port":"18332"},{"ip":"117.169.78.54","port":"17029"}]
    # print(url)
    proxies = {"http": "http://116.16.179.170:41301"}

    res = requests.get(url, headers=header)
    # print(res.text)
    con = json.loads(res.text)
    try:
        data = con['data']
        print(data)
    except:
        return False
    # print(data)
    for item in data:
        article_data = {}
        content = item['content']
        content = json.loads(content)
        try:
            if content['is_stick'] == True:
                behot_time = content['behot_time']
                if behot_time > max_time:
                    continue

        except KeyError:
            behot_time = content['behot_time']

            if behot_time > max_time:
                continue
            elif behot_time < min_time:
                return True

    #     article_data['title'] = content['title']
    #     article_data['item_id'] = content['item_id']
    #     article_data['group_source'] = content['group_source']
    #     video_detail_info = content['video_detail_info']
    #     if video_detail_info == None:
    #         image_url = 'None'
    #     else:
    #         image_url = video_detail_info['detail_video_large_image']['url']
    #     # chinece_tag
    #     article_data['image_url'] = image_url
    #     article_data['source'] = content['source']
    #     article_data['source_url'] = content['article_url']
    #     article_data['behot_time'] = content['behot_time']
    #     article_data['is_original'] = content['is_original']
    #     article_data['go_detail_count'] = content['read_count']
    #     article_data['comments_count'] = content['comment_count']
    #     article_data['like_count'] = content['like_count']
    #     article_data['share_count'] = content['share_count']
    #     article_data['has_video'] = content['has_video']
    #     article_data['gallary_image_count'] = content['gallary_image_count']
    #     article_data['abstract'] = content['abstract']
    #     print(article_data)
    offset = con["offset"]
    return offset


def get_content(uid):
    offset = 0
    global num, sleep

    while True:
        offset = get_toutiao_app_data(uid, offset)
        num += 1
        if num % 100 == 0:
            time.sleep(60)
        print(num)
        if offset == False:
            return False
        if offset == True:
            return True
        time.sleep(random.choice(sleep))


def main():
    # user_id = [5954781019, 7019727691, 75934815307, 1710471115190999, 62081460499, 54396682278, 4272471903, 62080421410,
    #            52291289132, 52569448261, 5788750304
    #     , 56203464796, 5343541488, 54194780584, 56744006869, 5332278629, 103360532572, 75933841180, 80349420724,
    #            111186666602, 50049588506, 78757011081
    #     , 66391148945, 58616497526, 111426243613, 63919037637, 6037307865, 109967641866, 50113153906,
    #            110591969657, 80326185806, 50123140644, 63557154537, 51866066902
    #     , 51817119205, 4557914163, 51749594619, 58001913963, 67737009923, 77641017138, 80951438187]
    user_id = [3200725091]
    file_handle = open('AA.txt', mode='a')
    file_handle.write('开始：' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    file_handle.write('\r\n')
    file_handle.close()
    for uid in user_id:
        res = get_content(uid)
        if res == False:
            break
        if res == True:
            continue
    file_handle = open('AA.txt', mode='a')
    file_handle.write('休息{}s:  '.format(str(sleep)) + str(num) + ' 条json数据')
    file_handle.write('\r\n')
    file_handle.write('结束：' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    file_handle.write('\r\n')
    file_handle.close()
    # time.sleep(10)


if __name__ == '__main__':
    # while True:
    #     a = test()
    #     if a == 'yes':
    main()
