import execjs
import requests


# def get_sign(id,t):
#     """_signature"""
#     print(id+t)
#     with open('sign.js') as f:
#         js = f.read()
#     ctx = execjs.compile(js)
#     return ctx.call('a',id+t)

def get_sign(id,t):
    """_signature"""
    print(id+t)
    with open('newsign.js') as f:
        js = f.read()
    ctx = execjs.compile(js)
    return ctx.call('a',id+t)



# V-7KXgAgEBylwfgZQiCbzVfuy0AAAno
# FykXgAAgEBLlBiXH9.GkGxcpFpAAEkl
# FykXgAAgEBLlBiXH9.GsUBcpFpAAEkl
# FykXgAAgEBLlBiXH9.E1RBcpFpAAEkl

# eiNyhwAAJCyF3I14rj9nsnojcp
# etqBggAAJNWFJX591yBSU3ragZ

a = get_sign('5954781019','0')
print(a)
# # url = "https://www.toutiao.com/api/pc/feed/?category=pc_profile_ugc&utm_source=toutiao&visit_user_id=5954781019&max_behot_time=0&_signature=GgpccgAgEBfoJW41nd9YnBoKXWAAEQH"
url = "https://www.toutiao.com/api/pc/feed/?category=pc_profile_ugc&utm_source=toutiao&visit_user_id=5954781019&max_behot_time=0&_signature={}".format(a)
print(url)
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Referer": "https://www.toutiao.com/c/user/",
    "Cookie": 'uuid="w:912057c54847457eb48b69d637117cdc"; _ga=GA1.2.750742914.1512468789; tt_webid=6496003991339943438; WEATHER_CITY=%E5%8C%97%E4%BA%AC; csrftoken=5d5451cff324d51738a43be755409d3f; tt_webid=6496003991339943438; UM_distinctid=16bd0953213a12-08ca4cb1e5e02e-b781636-1fa400-16bd0953214703; CNZZDATA1259612802=1368380591-1512950320-https%253A%252F%252Fwww.newrank.cn%252F%7C1571894378; tt_track_id=5b300642d21cf37a5b867ab978f257c5; __tasessionId=q91xdrcwm1577348600504'
}
res = requests.get(url,headers= header)
print(res.text)


