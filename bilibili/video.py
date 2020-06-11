import requests


url = 'https://52sos52.yfcalc.com:21574/upos-dash-mirrorks3u.bilivideo.com/bilibilidash_f956d2965f271c3f563de462227d8220b6f535ee/163323419_da2-1-30080.m4s?scuid=FTJrNMtiIRMAa8wBXjVa&timeout=1591838279&check=1754453267&sttype=90&yfdspt=1591233479373&yfpri=100&yfopt=17&yfskip=1&yfreqid=AJCZhkF06DthLx2AAD&yftt=100&yfhost=iibrs52.yfcache.com&yfpm=1'
url = 'https://ghisss1.yfcalc.com:11207/upos-dash-mirrorks3u.bilivideo.com/bilibilidash_0b09cac3929d865d841148c03b7587a0d1d23f91/168007611_da2-1-30080.m4s?scuid=FTJrNMtiIRMAa8wBXjVa&timeout=1591839107&check=817579913&sttype=90&yfdspt=1591234307712&yfpri=100&yfopt=17&yfskip=1&yfreqid=AJCZhkF0yDthPA6AAF&yftt=100&yfhost=aibrs52.yfcache.com&yfpm=1'
# url = 'https://ghisss1.yfcalc.com:11207/upos-dash-mirrorks3u.bilivideo.com/bilibilidash_0b09cac3929d865d841148c03b7587a0d1d23f91/168007611_da2-1-30080.m4s?scuid=FTMsEaDrD8UeBWofIDTH&timeout=1591839107&check=817579913&sttype=90&yfdspt=1591234307712&yfpri=100&yfopt=17&yfskip=1&yfreqid=AJCZhkF0yDthPA6AAF&yftt=100&yfhost=aibrs52.yfcache.com&yfpm=1'
headers = {
    # 'cookie': "fts=1512536357; buvid3=98F07B63-F162-4266-B52E-3A2E59B3DD9547209infoc; pgv_pvi=6066786304; LIVE_BUVID=2b1b2a628039177645c7dbc2be795290; LIVE_BUVID__ckMd5=bdade4501f3ce28c; stardustvideo=1; CURRENT_FNVAL=16; rpdid=|(u)l~lmmJk)0J'ullYY|kk||; sid=4n3dlq79; _uuid=965BDB1A-5C7B-8B9C-9706-DED45CAA600C12128infoc; CURRENT_QUALITY=80; im_notify_type_430343910=0; DedeUserID=430343910; DedeUserID__ckMd5=24cad682056a3e26; SESSDATA=7b3bae44%2C1605419935%2C68a41*51; bili_jct=a911ca6cef406f45d7bf55ffe125390d; bp_t_offset_430343910=386857346554106024; bp_video_offset_430343910=386857346554106024; PVID=2; bfe_id=6f285c892d9d3c1f8f020adad8bed553",
    'referer': 'https://space.bilibili.com/',
    # 'referer': 'https://space.bilibili.com/299732210?spm_id_from=333.851.b_62696c695f7265706f72745f72656164.23',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
res = requests.get(url,headers=headers)
print(res.content)
with open("./22.mp4", 'ab') as file:
    file.write(res.content)
    file.flush()