import re

import  requests
from lxml import etree

url = 'https://search.suning.com/%E6%89%8B%E6%9C%BA/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',

}

res = requests.get(url,headers=headers)


# re.findall('id="0000000000-11379532392')
tree = etree.HTML(res.text)

ul = tree.xpath('//*[@id="product-list"]/ul')
print(ul[0])
for item in ul[0]:
    print(item)