import requests

url = 'https://www.zhipin.com/wapi/zpchat/geek/historyMsg?bossId=73ab9abaec5c4b981HZy3ti6FFU~&groupId=73ab9abaec5c4b981HZy3ti6FFU~&maxMsgId=0&c=20&page=1&src=0&securityId=fThlydhpXNaXszlFEY8vwPTqojfAHECMtuifEOgF03ZOta2CeXrrV_bR-AHfHyHuImkyaVnTFk_WCFo1SpM2AxAxP0gscloQY6M5sc1BRf96DkmcSjz8oKQjgzpW-BvENmeZTEdDKXPW5dbfReH0A9gwSdBVVSu78wzV7udizf3h9ufYvN_bYXnN1dxRWzJrn7UDxAA6gloFi8-4rd_E8sHUxAlCVmIcMMuZIfKlqtAZiJPMxaQM4AriAu3vlvQXM7ljeovS9tilj-0UoKnmCxSuj9oHhw~~&loading=true&_t=1586848552654'
url = 'https://www.zhipin.com/wapi/zpgeek/chat/bossdata.json?bossId=83a0f0ac67b103b11Hd909q8EFc~&bossSource=0&securityId=mp9y6zy9GJL8jooF30ctHn3EgLpX1YZB-10HENkANKBZnMwJ2vBMUsdoF-40cCZ41mcKFS9wqK5ge3rwCOG9n5Dq46alLtOK9NwY6idjGL-nUl0YGPYJ4vZ7GQeKrI8e7N6O67xcsFlSYs28uMprWcY7FI6rtGT2BvNgKhu-DahqJpC7uZOc5T_bXA1eZQMGKIXed6sL-5XsmLiw95Kq0sX2Vw1ewImSaJP82QB62xbOrF-2Oj7SW3OJiZ_aLevfZlDGvKY00GDyBuBVbmKLEpzftXbxgw~~'

url = 'https://www.zhipin.com/analytics/upload?rid=fb2f1656804eff7d&sid=fd0578ffa677b1907a57608b1d30ef74'
header = {
"wup_version": "3.0",
"TYPE_COMPRESS": "2",
"encr_type": "rsapost",
"bea_key": "Ly4KrCVRqqFMBvy7Jyj5SJo71ITCZigmDZXjIY8D/nROKF+6ljC9wUIjI9E1SB7tkx3CqMMEpd4s5DvvBs61kNoaG4ntVddCjem1q0FhYGEJhZ8aqNCQHsxFd4L1FmlLFbhNRShJGHfPFRqu26huTWuCkjuqK8LyWldZ8WE1Yxs=",
"Content-Length": "416",
"Host": "oth.eve.mdt.qq.com:8080",
"Connection": "Keep-Alive"
}
data = "fThlydhpXNaXszlFEY8vwPTqojfAHECMtuifEOgF03ZOta2CeXrrV_bR-AHfHyHuImkyaVnTFk_WCFo1SpM2AxAxP0gscloQY6M5sc1BRf96DkmcSjz8oKQjgzpW-BvENmeZTEdDKXPW5dbfReH0A9gwSdBVVSu78wzV7udizf3h9ufYvN_bYXnN1dxRWzJrn7UDxAA6gloFi8-4rd_E8sHUxAlCVmIcMMuZIfKlqtAZiJPMxaQM4AriAu3vlvQXM7ljeovS9tilj-0UoKnmCxSuj9oHhw~~"
res = requests.post(url,data=data,headers=header)
print(res.text)