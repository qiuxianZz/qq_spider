import time

import  requests


# url = 'https://profile.zjurl.cn/api/feed/profile/v1/?category=profile_all&visited_uid=80920050890&stream_api_version=82&request_source=1&offset=0&version_code=755&user_id=80920050890&media_id=&app_name='
# url = 'https://profile.zjurl.cn/api/feed/profile/v1/?category=profile_all&visited_uid=6029241157&stream_api_version=82&request_source=1&offset=0&version_code=755&version_name=70505&user_id=6029241157&media_id=&active_tab=&device_id=0'
#
url= 'https://profile.zjurl.cn/api/feed/profile/v1/?category=profile_all&visited_uid=6061879406&stream_api_version=82&request_source=1&offset=0&version_code=755&version_name=70505&user_id=6061879406&media_id=0&active_tab=dongtai&device_id=65&app_name=news_article'


url = 'https://profile.zjurl.cn/api/feed/profile/v1/?category=profile_all&visited_uid=55481971604&stream_api_version=82&request_source=1&offset=0&version_code=755&version_name=70505&user_id=55481971604&media_id=&active_tab=&device_id=&app_name=news_article'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'cookie': 'ga=GA1.2.949505188.1584421131; gftoken=NDQyNTk1NzkwfDE1ODgyMzgwNTE3MHx8MAcHBwcHBwc; UM_distinctid=171ca5d6017362-09499502e81c42-b781636-1fa400-171ca5d6018a04; odin_tt=a50b5d99caab355092145d1b4d0a204343971704964ed5fa33a5fd1f11919aff64222e3a59ff6315529f3c8ef2c4e0b8c6d1746cbbef7bbd227806a0fbb80437; SLARDAR_WEB_ID=f5b884fe-7d31-422d-83d8-cb5634025f2b; CNZZDATA1274386066=1874866619-1588233158-%7C1589857419'

}
while True:
    res = requests.get(url,headers=headers)
    print(res.text)
    time.sleep(3)