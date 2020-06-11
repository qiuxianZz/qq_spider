
import  requests

url = 'https://broadcast.chat.bilibili.com:7823/sub'
headers = {
'Host': 'broadcast.chat.bilibili.com:7823',
'Connection': 'Upgrade',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
'Upgrade':'websocket',
'Origin': 'https://www.bilibili.com',
'Sec-WebSocket-Version': '13',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': "fts=1512536357; buvid3=98F07B63-F162-4266-B52E-3A2E59B3DD9547209infoc; pgv_pvi=6066786304; LIVE_BUVID=2b1b2a628039177645c7dbc2be795290; LIVE_BUVID__ckMd5=bdade4501f3ce28c; stardustvideo=1; CURRENT_FNVAL=16; rpdid=|(u)l~lmmJk)0J'ullYY|kk||; sid=4n3dlq79; _uuid=965BDB1A-5C7B-8B9C-9706-DED45CAA600C12128infoc; CURRENT_QUALITY=80; im_notify_type_430343910=0; DedeUserID=430343910; DedeUserID__ckMd5=24cad682056a3e26; SESSDATA=3c3fdaa6%2C1604462309%2C6fc80*51; bili_jct=ecb1d16eb9abeff02d5d5ffb3ff37e8c",
'Sec-WebSocket-Key': 'VGp4+jJXHiLwC79VVgLlCw==',
'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
}
res = requests.get(url,headers)
print(res.text)
