import requests
import json

# url = 'https://api.amemv.com/aweme/v1/discover/search/?os_api=22&device_type=TAS-AN00&ssmix=a&manifest_version_code=920&dpi=192&uuid=861143247784164&app_name=aweme&version_name=9.2.0&ts=1587435549&app_type=normal&ac=wifi&update_version_code=9202&channel=aweGW&_rticket=1587435564855&device_platform=android&iid=110328814314&version_code=920&cdid=14853dcf-a069-4331-93f3-95802d8687ad&openudid=0425eebe3326b9c2&device_id=71237989952&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=HUAWEI&aid=1128&mcc_mnc=46000'
# url = 'https://api.amemv.com/aweme/v1/discover/search/?os_api=22&device_type=TAS-AN00&ssmix=a&manifest_version_code=920&dpi=192&uuid=861143247784164&app_name=aweme&version_name=9.2.0&ts=1587435547&app_type=normal&ac=wifi&update_version_code=9202&channel=aweGW&_rticket=1587435563514&device_platform=android&iid=110328814314&version_code=920&cdid=14853dcf-a069-4331-93f3-95802d8687ad&openudid=0425eebe3326b9c2&device_id=71237989952&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=HUAWEI&aid=1128&mcc_mnc=46000'
# url = 'https://api.amemv.com/aweme/v1/discover/search/?os_api=22&device_type=TAS-AN00&ssmix=a&manifest_version_code=920&dpi=192&uuid=861143247784164&app_name=aweme&version_name=9.2.0&ts=1587436809&app_type=normal&ac=wifi&update_version_code=9202&channel=aweGW&_rticket=1587435892837&device_platform=android&iid=110328814314&version_code=920&cdid=14853dcf-a069-4331-93f3-95802d8687ad&openudid=0425eebe3326b9c2&device_id=71237989952&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=HUAWEI&aid=1128&mcc_mnc=46000'
#
# data = "cursor=100&keyword=%E7%94%9F%E6%B4%BB&count=10&type=1&is_pull_refresh=1&hot_search=0&search_source=&search_id=2020042110185801000807113511A34568&query_correct_type=1"
# headers = {
#     "X-SS-STUB": "EB9011EB2F3221CEF85F80CB2ECB1A33",
#     "Accept-Encoding": "gzip",
#     "X-SS-REQ-TICKET": "1587436809",
#     "sdk-version": "1",
#     "User-Agent": "ttnet okhttp/3.10.0.2",
#     # "Cookie": "d_ticket=400a18734e12b3182e7032ef0d00b2cecf2a3; odin_tt=a9ed3699b11cbccc2511dee2bcf181f790ec7a9d37c09f51eddd105604987ff7e60966e8d21e3e473d63e41567ce99e2; sid_guard=8241f5387b087b0806dca374eeed9977%7C1585807633%7C5184000%7CMon%2C+01-Jun-2020+06%3A07%3A13+GMT; uid_tt=cd9f43402f9ccdbdd8f834f4867ee8b2; sid_tt=8241f5387b087b0806dca374eeed9977; sessionid=8241f5387b087b0806dca374eeed9977; install_id=110328814314; ttreq=1$164a05654b93f308f77bad34ef1fea7362369373",
#     "Cookie": "d_ticket=400a18734e12b3182e7032ef0d00b2cecf2a3; odin_tt=a9ed3699b11cbccc2511dee2bcf181f790ec7a9d37c09f51eddd105604987ff7e60966e8d21e3e473d63e41567ce99e2; sid_guard=8241f5387b087b0806dca374eeed9977%7C1585807633%7C5184000%7CMon%2C+01-Jun-2020+06%3A07%3A13+GMT; uid_tt=cd9f43402f9ccdbdd8f834f4867ee8b2; sid_tt=8241f5387b087b0806dca374eeed9977; sessionid=8241f5387b087b0806dca374eeed9977; install_id=110328814314; ttreq=1$164a05654b93f308f77bad34ef1fea7362369373",
#     "x-tt-token": "008241f5387b087b0806dca374eeed9977719b99aaad4b506829267a7db9d41eaa52894a52eaf891bb29c0733af58671ad28",
#     "X-Gorgon": "0401603f4005a38df45c3c05c934ed27b3b7009c44957d531d1c",
#     "X-Khronos": "1587435892",
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "Content-Length": "165",
#     "Host": "api.amemv.com",
#     "Connection": "Keep-Alive"
#
# }
# res = requests.post(url,data=json.dumps(data),headers=headers)
# print(res.text)


url = 'https://api.amemv.com/aweme/v1/discover/search/?os_api=22&device_type=TAS-AN00&ssmix=a&manifest_version_code=920&dpi=192&uuid=861143247784164&app_name=aweme&version_name=9.2.0&ts=1587436945&app_type=normal&ac=wifi&update_version_code=9202&channel=aweGW&_rticket=1587436976382&device_platform=android&iid=110328814314&version_code=920&cdid=14853dcf-a069-4331-93f3-95802d8687ad&openudid=0425eebe3326b9c2&device_id=71237989952&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=HUAWEI&aid=1128&mcc_mnc=46000'
url = 'https://api.amemv.com/aweme/v1/discover/search/?os_api=22&device_type=TAS-AN00&ssmix=a&manifest_version_code=920&dpi=192&uuid=861143247784164&app_name=aweme&version_name=9.2.0&ts=1587436945&app_type=normal&ac=wifi&update_version_code=9202&channel=aweGW&_rticket=1587436976382&device_platform=android&iid=110328814314&version_code=920&cdid=14853dcf-a069-4331-93f3-95802d8687ad&openudid=0425eebe3326b9c2&device_id=71237989952&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=HUAWEI&aid=1128&mcc_mnc=46000'
headers = {
    # 'X-SS-STUB': '564B8CC8C6ED7BB8476C3A90FABD0804',
    'Accept-Encoding': 'gzip',
    'X-SS-REQ-TICKET': '1587436976379',
    'sdk-version': '1',
    'User-Agent': 'ttnet okhttp/3.10.0.2',
    'Cookie': 'd_ticket=400a18734e12b3182e7032ef0d00b2cecf2a3; odin_tt=a9ed3699b11cbccc2511dee2bcf181f790ec7a9d37c09f51eddd105604987ff7e60966e8d21e3e473d63e41567ce99e2; sid_guard=8241f5387b087b0806dca374eeed9977%7C1585807633%7C5184000%7CMon%2C+01-Jun-2020+06%3A07%3A13+GMT; uid_tt=cd9f43402f9ccdbdd8f834f4867ee8b2; sid_tt=8241f5387b087b0806dca374eeed9977; sessionid=8241f5387b087b0806dca374eeed9977; install_id=110328814314; ttreq=1$164a05654b93f308f77bad34ef1fea7362369373',
    'x-tt-token': '008241f5387b087b0806dca374eeed9977719b99aaad4b506829267a7db9d41eaa52894a52eaf891bb29c0733af58671ad28',
    'X-Gorgon': '0401400440059034a3c61d64f1cb0af0b28c06fa18c754063d24',
    'X-Khronos': '1587436976',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Content-Length': '164',
    'Host': 'api.amemv.com',
    'Connection': 'Keep-Alive',
}

data = 'cursor=10&keyword=%E7%94%9F%E6%B4%BB&count=10&type=1&is_pull_refresh=1&hot_search=0&search_source=&search_id=20200421104224010014063086210418F5&query_correct_type=1'
#
# res = requests.post(url, data=data, headers=headers)
# print(res.text)

# POST https://api.amemv.com/aweme/v1/discover/search/?os_api=22&device_type=TAS-AN00&ssmix=a&manifest_version_code=920&dpi=192&uuid=861143247784164&app_name=aweme&version_name=9.2.0&ts=1587437181&app_type=normal&ac=wifi&update_version_code=9202&channel=aweGW&_rticket=1587437213311&device_platform=android&iid=110328814314&version_code=920&cdid=14853dcf-a069-4331-93f3-95802d8687ad&openudid=0425eebe3326b9c2&device_id=71237989952&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=HUAWEI&aid=1128&mcc_mnc=46000 HTTP/1.1
# X-SS-STUB: D498A28C215AB30706A7E5D6CE54190D
# Accept-Encoding: gzip
# X-SS-REQ-TICKET: 1587437213309
# sdk-version: 1
# User-Agent: ttnet okhttp/3.10.0.2
# Cookie: d_ticket=400a18734e12b3182e7032ef0d00b2cecf2a3; odin_tt=a9ed3699b11cbccc2511dee2bcf181f790ec7a9d37c09f51eddd105604987ff7e60966e8d21e3e473d63e41567ce99e2; sid_guard=8241f5387b087b0806dca374eeed9977%7C1585807633%7C5184000%7CMon%2C+01-Jun-2020+06%3A07%3A13+GMT; uid_tt=cd9f43402f9ccdbdd8f834f4867ee8b2; sid_tt=8241f5387b087b0806dca374eeed9977; sessionid=8241f5387b087b0806dca374eeed9977; install_id=110328814314; ttreq=1$164a05654b93f308f77bad34ef1fea7362369373
# x-tt-token: 008241f5387b087b0806dca374eeed9977719b99aaad4b506829267a7db9d41eaa52894a52eaf891bb29c0733af58671ad28
# X-Gorgon: 040140dc40051279ee789ad353d40cb08fff5815e8db26bc71a9
# X-Khronos: 1587437213
# Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# Content-Length: 164
# Host: api.amemv.com
# Connection: Keep-Alive
#
# cursor=20&keyword=%E7%94%9F%E6%B4%BB&count=10&type=1&is_pull_refresh=1&hot_search=0&search_source=&search_id=20200421104224010014063086210418F5&query_correct_type=1


# url = 'https://api.amemv.com/aweme/v1/user/following/list/?user_id=72557243297&sec_user_id=MS4wLjABAAAAuC0qHWV0UWcNpEEQE2sZljRfgG1C17OupkXqFs0hp5k&max_time=1572093902&count=20&offset=0&source_type=1&address_book_access=1&gps_access=1&os_api=22&device_type=TAS-AN00&ssmix=a&manifest_version_code=920&dpi=192&uuid=861143247784164&app_name=aweme&version_name=9.2.0&ts=1587437959&app_type=normal&ac=wifi&update_version_code=9202&channel=aweGW&_rticket=1587438002333&device_platform=android&iid=110328814314&version_code=920&cdid=14853dcf-a069-4331-93f3-95802d8687ad&openudid=0425eebe3326b9c2&device_id=71237989952&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=HUAWEI&aid=1128&mcc_mnc=46000'
# url = 'https://api.amemv.com/aweme/v1/user/following/list/?user_id=72557243297&sec_user_id=MS4wLjABAAAAuC0qHWV0UWcNpEEQE2sZljRfgG1C17OupkXqFs0hp5k&max_time=1587437945&count=20&offset=0&source_type=1&address_book_access=1&gps_access=1&os_api=22&device_type=TAS-AN00&ssmix=a&manifest_version_code=920&dpi=192&uuid=861143247784164&app_name=aweme&version_name=9.2.0&ts=1587437945&app_type=normal&ac=wifi&update_version_code=9202&channel=aweGW&_rticket=1587437988785&device_platform=android&iid=110328814314&version_code=920&cdid=14853dcf-a069-4331-93f3-95802d8687ad&openudid=0425eebe3326b9c2&device_id=71237989952&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=HUAWEI&aid=1128&mcc_mnc=46000'
# url = 'https://aweme-eagle.snssdk.com/aweme/v1/user/?sec_user_id=MS4wLjABAAAABvwOLdm1R6t-IZujPh9PFDRq1ZGxQ027jsZIqyCRuNE.&user_id=106168859482&address_book_access=1&retry_type=no_retry'
# url = 'https://aweme.snssdk.com/aweme/v1/user/following/list/?user_id=96348780800&sec_user_id=MS4wLjABAAAArPZnuqkJr2oRq-d8nbmRYm3_LZeUj6fwBrCeBPu4OYk&max_time=1587471028&count=20&offset=0&source_type=1&address_book_access=2&gps_access=1&os_api=22&device_type=TAS-AN00&ssmix=a&manifest_version_code=970&dpi=192&uuid=861143247784164&app_name=douyin_lite&version_name=9.7.0&ts=1587471028&app_type=normal&ac=wifi&update_version_code=9702&channel=360_lite_aweme&_rticket=1587471302159&device_platform=android&iid=113035172582&version_code=970&cdid=f98c5820-3a43-41d5-bb75-ef426599cdc6&openudid=0425eebe3326b9c2&device_id=71237989952&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=HUAWEI&aid=2329&mcc_mnc=46000'
url = 'https://aweme.snssdk.com/aweme/v1/user/following/list/?user_id=96348780800&sec_user_id=MS4wLjABAAAArPZnuqkJr2oRq-d8nbmRYm3_LZeUj6fwBrCeBPu4OYk&max_time=1586956247&count=20&offset=0&source_type=1&address_book_access=2&gps_access=1&os_api=22&device_type=TAS-AN00&ssmix=a&manifest_version_code=970&dpi=192&uuid=861143247784164&app_name=douyin_lite&version_name=9.7.0&ts=1587471109&app_type=normal&ac=wifi&update_version_code=9702&channel=360_lite_aweme&_rticket=1587471109064&device_platform=android&iid=113035172582&version_code=970&cdid=f98c5820-3a43-41d5-bb75-ef426599cdc6&openudid=0425eebe3326b9c2&device_id=71237989952&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=HUAWEI&aid=2329&mcc_mnc=46000'
url = 'https://aweme.snssdk.com/aweme/v1/user/following/list/?user_id={}&sec_user_id={}&max_time={}&count=20&offset=0&source_type=1&address_book_access=2&gps_access=1&os_api=22&device_type=TAS-AN00&ssmix=a&manifest_version_code=970&dpi=192&uuid=861143247784164&app_name=douyin_lite&version_name=9.7.0&ts=1587471753&app_type=normal&ac=wifi&update_version_code=9702&channel=360_lite_aweme&_rticket=1587471753399&device_platform=android&iid=113035172582&version_code=970&cdid=f98c5820-3a43-41d5-bb75-ef426599cdc6&openudid=0425eebe3326b9c2&device_id=71237989952&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=HUAWEI&aid=2329&mcc_mnc=46000'
headers = {
#     'Accept-Encoding': 'gzip',
    # 'X-SS-REQ-TICKET': '1587437988785',
    # 'sdk-version': '1',
    'User-Agent': 'ttnet okhttp/3.10.0.2',
    # 'Cookie': 'd_ticket=400a18734e12b3182e7032ef0d00b2cecf2a3; odin_tt=a9ed3699b11cbccc2511dee2bcf181f790ec7a9d37c09f51eddd105604987ff7e60966e8d21e3e473d63e41567ce99e2; sid_guard=8241f5387b087b0806dca374eeed9977%7C1585807633%7C5184000%7CMon%2C+01-Jun-2020+06%3A07%3A13+GMT; uid_tt=cd9f43402f9ccdbdd8f834f4867ee8b2; sid_tt=8241f5387b087b0806dca374eeed9977; sessionid=8241f5387b087b0806dca374eeed9977; install_id=110328814314; ttreq=1$164a05654b93f308f77bad34ef1fea7362369373',
    # 'x-tt-token': '008241f5387b087b0806dca374eeed9977719b99aaad4b506829267a7db9d41eaa52894a52eaf891bb29c0733af58671ad28',
    # 'X-Gorgon': '0401c0664005fad9efb290365c3bef9a10d01f7dd2cfe093a619',
    # 'X-Khronos': '1587437988',
    # 'Host': 'api.amemv.com',
    # 'Connection': 'Keep-Alive'

}
# res = requests.get(url,headers=headers)
# print(res.text)



def get_user(uid,sec_id,max_tiem):
    res = requests.get(url.format(url,sec_id,max_tiem),headers=headers)
    print(res.text)
    data = json.loads(res.text)
    max_time = data["max_time"]
    followings = data["followings"]
    if len(followings) < 20:
        return "end"
    return  max_time

uid = '72557243297'
sec_id = 'MS4wLjABAAAAuC0qHWV0UWcNpEEQE2sZljRfgG1C17OupkXqFs0hp5k'
max_time = '1572093902'
# get_user(uid,sec_id,max_time)
while True:
    max_time = get_user(uid,sec_id,max_time)
    if max_time == "end":
        break