import wget
url = 'http://115.29.174.137:3333/xdn/proxies/get?count=10&type=0&all=0'
filename = wget.download(url)

# 指定输出文件, 相当于 `-O output`
filename = wget.download(url)