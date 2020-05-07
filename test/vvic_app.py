import json

import  requests

url = 'https://app.vvic.com/v1/shop?id=41697&orderby=up_time&pageSize=12&secret=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ2dmljLmNvbSIsImV4cCI6MTU4NzYwNDQwMywic3ViIjoidnZpY19hbmRyb2lkIn0.8VsXTUtpHHU-CRHQQ33Gd9817qIevNT3tg_A71c7pLs&sort=desc'

headers = {
    "User-Agent": "okhttp/3.12.0"
}

res = requests.get(url,headers=headers)
print(res.text)
data = json.loads(res.text)



def getData(user):
    res = requests.get(url.format(user),headers=headers)
    print(res.text)
