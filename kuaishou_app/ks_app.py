import json
import random
import time

import requests


def get_ks(page):
    dumpJsonData = {"operationName": "SearchDetailQuery",
                    "variables": {"key": "123", "type": "author", "page": page, "lssid": "null", "ussid": "null"},
                    "query": "query SearchDetailQuery($key: String, $type: String, $page: Int, $lssid: String, $ussid: String) {\n  pcSearchDetail(key: $key, type: $type, page: $page, lssid: $lssid, ussid: $ussid) {\n    ... on SearchCategoryList {\n      type\n      list {\n        categoryId\n        categoryAbbr\n        title\n        src\n        __typename\n      }\n      __typename\n    }\n    ... on SearchUserList {\n      type\n      ussid\n      list {\n        id\n        name\n        living\n        avatar\n        sex\n        description\n        counts {\n          fan\n          follow\n          photo\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    ... on SearchLivestreamList {\n      type\n      lssid\n      list {\n        user {\n          id\n          avatar\n          name\n          __typename\n        }\n        poster\n        coverUrl\n        caption\n        id\n        playUrls {\n          quality\n          url\n          __typename\n        }\n        quality\n        gameInfo {\n          category\n          name\n          pubgSurvival\n          type\n          kingHero\n          __typename\n        }\n        hasRedPack\n        liveGuess\n        expTag\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
    # {"operationName":"SearchDetailQuery","variables":{"key":"123","type":"author","page":"2","lssid":'null',"ussid":'null'},"query":"query SearchDetailQuery($key: String, $type: String, $page: Int, $lssid: String, $ussid: String) {\n  pcSearchDetail(key: $key, type: $type, page: $page, lssid: $lssid, ussid: $ussid) {\n    ... on SearchCategoryList {\n      type\n      list {\n        categoryId\n        categoryAbbr\n        title\n        src\n        __typename\n      }\n      __typename\n    }\n    ... on SearchUserList {\n      type\n      ussid\n      list {\n        id\n        name\n        living\n        avatar\n        sex\n        description\n        counts {\n          fan\n          follow\n          photo\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    ... on SearchLivestreamList {\n      type\n      lssid\n      list {\n        user {\n          id\n          avatar\n          name\n          __typename\n        }\n        poster\n        coverUrl\n        caption\n        id\n        playUrls {\n          quality\n          url\n          __typename\n        }\n        quality\n        gameInfo {\n          category\n          name\n          pubgSurvival\n          type\n          kingHero\n          __typename\n        }\n        hasRedPack\n        liveGuess\n        expTag\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
    header = {
        # "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        # "Connection": "keep-alive",
        # "Content-Length": "1430",
        "content-type": "application/json",
        "Cookie": "did=web_7f0cee25eca802e32cd6315f6983833f; didv=1572953497000; kuaishou.live.bfb1s=9b8f70844293bed778aade6e0a8f9942; clientid=3; client_key=65890b29; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1578905924,1578906680,1578966296,1578971152; Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee=1578971152; userId=12892832; userId=12892832; kuaishou.live.web_st=ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgAd2O1FVvabZVzcsnE3PJW4KgPdr_ZKa4u4O5dY1PuxkxKgBSvWM36YQPWHoweAaGRq-Tp7emNSOXKJwQs_1lW_MaYKrrGWlg_9F5438rpwqqOEKxQb5EfuFZpyRhCN2CKybhop7h0MjnOUgjqTuVmj0sp1ta-bF6LfiTkPiTViFuwM29HaOC_zAz82_7aSS6KnG7oDMtO6T3fW8M_QyMHYMaEsvpGUru20c-iIt7T0W8MQrXwiIgZKCwBKsVm_YDbNEX5hl5R9JI2enatyvac5ijrWMw6nooBTAB; kuaishou.live.web_ph=9bbec063a8aa7416f02c81b9ed13c2479c49",
        # "Cookie": "did=web_7f0cee25eca802e32cd6315f6983833f; didv=1572953497000; kuaishou.live.bfb1s=9b8f70844293bed778aade6e0a8f9942; clientid=3; client_key=65890b29; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1578905924,1578906680,1578966296,1578971152; Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee=1578971152; userId=1664743631; userId=1664743631; kuaishou.live.web_st=ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgAaLBgles5FjE5NQ8TIrYDq_bqoQcRFdRKY_sc1wGKDqI0lkgb1nMnGYSPcOJ9rcj-8y_xYY6r7cvZl8iQCpaEIWKuoBN1BpQmzooVyrPjgEN-P5dej3BZsq39T7c03bK__1a1tGNRNLp_1wj9E8aiSgSJpTjNkIjCgn4aIKNFHxsQHp8Tz2MHDFJmY8X750f2Ofywz_eH7AicXFaRV2S5cAaEqzjCHq0fUXesXMf4ciyRnDKKyIgxpI1qyW4K6jRISiQm5Lj7JObHcbxVbRBBQq6d374W8UoBTAB; kuaishou.live.web_ph=5eab1925c33a4ea0759ed725872679421a17",
        # "Cookie":"did=web_7f0cee25eca802e32cd6315f6983833f; didv=1572953497000; clientid=3; client_key=65890b29; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1578986959,1579056400,1579142011,1579663761; Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee=1579663761; kuaishou.live.bfb1s=477cb0011daca84b36b3a4676857e5a1",
        # "Cookie":"did=web_7f0cee25eca802e32cd6315f6983833f; didv=1572953497000; clientid=3; client_key=65890b29; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1578986959,1579056400,1579142011,1579663761; Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee=1579663761; kuaishou.live.bfb1s=477cb0011daca84b36b3a4676857e5a1; userId=12892832; userId=12892832; kuaishou.live.web_st=ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgATL74ShIHPsIqqw4omiZrVFTJcmoxc9ioWiSjxOfP8S-prvVuN6u7EgWqOmmCR4wiNHE7K-Tsr7am3Bxmy-4HH7V8QREF8lBzdvCxFbqrfp9-yeGJsP4WL9Vrt0Gm5a5xnv4WEpGbR4z2NyU1pG659jjdc5oeFQmHuBr17y9KEV1IUXrvMFu1zD6HO_t4DfZqn7ovlW5Zrtn7t7FJjr0YmwaErZBy_JDfEY0lUogcFFbVS54zCIg75zH9dt1e1FatlHexDjfiZLRyHk2-ELsJ0WDxQcUU-IoBTAB; kuaishou.live.web_ph=12d423f899142d8ae555a8a0ea1c3e63171e",
        # "Host": "live.kuaishou.com",
        # "Origin": "https://live.kuaishou.com",
        "Referer": "https://live.kuaishou.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",

        # "Connection": "keep-alive",
        # "Content-Length": "333",个
        # "Content-Type": "application/json",
        # "Date": "Tue, 14 Jan 2020 02:29:48 GMT",
        # "X-KSLOGID": "578968988332485822",
    }
    proxies = [{"ip": "180.127.10.170", "port": "47256"}, {"ip": "121.226.44.197", "port": "22689"},
               {"ip": "171.11.197.33", "port": "31089"}, {"ip": "116.209.62.128", "port": "29818"},
               {"ip": "183.51.190.104", "port": "44683"}, {"ip": "117.169.78.54", "port": "18929"},
               {"ip": "117.169.78.54", "port": "17176"}, {"ip": "117.169.78.54", "port": "14252"},
               {"ip": "117.169.78.54", "port": "18332"}, {"ip": "117.169.78.54", "port": "17029"}]

    res = requests.post('https://live.kuaishou.com/m_graphql', headers=header, data=json.dumps(dumpJsonData),
                        proxies=random.choice(proxies))
    res.encoding = 'utf-8'
    print(res.json())


for p in range(1, 50):
    get_ks(p)
    time.sleep(10)

# {'data': {'pcSearchDetail': {'type': 'authors', 'ussid': None, 'list': [], '__typename': 'SearchUserList'}}}
# {'data': {'pcSearchDetail': None}, 'errors': [{'message': 'Need captcha', 'locations': [{'line': 2, 'column': 3}], 'path': ['pcSearchDetail'], 'extensions': {'code': 'GRAPHQL_VALIDATION_FAILED'}}], 'captcha': {'captchaKey': 'ouZN2nq4ppymGGcb4jHoAZsblYYAvkscBJd2upkGTUm2tmYA4HlwigmAUxMwyLVi', 'captchaType': '4', 'captchaUri': '/rest/k/live/search/user'}}
