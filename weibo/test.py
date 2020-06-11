import json

import face_recognition
import requests

# url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E8%87%AA%E6%8B%8D&page_type=searchall&page=2'
# url= 'https://m.weibo.cn/p/index?containerid=231051_-_fans_-_2112469561'
from weibo.a import is_face

url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_2112469561&since_id=10'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Cookie': 'SINAGLOBAL=6429106946443.357.1513824889850; _ga=GA1.2.253756793.1535545349; __gads=ID=1fe5c4f14bcc48ce:T=1535545348:S=ALNI_MZUxDmv_9CbGgFhJ_xTjYCHwU2gUg; SSOLoginState=1590981757; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFgX4SPx2oLIraAcO7FCEQX5JpX5KMhUgL.Fo-feoBpSK-RS0z2dJLoIpeLxK.L1hzLBo2LxK.LBozL1-Se; ALF=1622605535; SCF=An0HAsJINgITExhUXk-WTGiSGasIIgT5UZbYkE5gvo2eRcdWViWkdFEopmFGa44keGaf9YdTh11QcqC6VY6ieMI.; SUB=_2A25z0bswDeRhGeNL6VYQ9SvEzD6IHXVQpqv4rDV8PUNbmtAKLRekkW9NSKhhiG5RimATGvyY7LX832DAPhK5UiBJ; SUHB=0HThMjBOedAkQQ; _s_tentry=login.sina.com.cn; UOR=news.ifeng.com,widget.weibo.com,login.sina.com.cn; Apache=4860444952999.752.1591069535559; ULV=1591069535613:121:1:1:4860444952999.752.1591069535559:1586231596026; webim_unReadCount=%7B%22time%22%3A1591079049951%2C%22dm_pub_total%22%3A4%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A43%2C%22msgbox%22%3A0%7D; WBStorage=42212210b087ca50|undefined',
    # 'Host': 's.weibo.com',
    # 'Referer': 'https://s.weibo.com/pic?q=%E8%87%AA%E6%8B%8D&Refer=weibo_pic',
    # 'X-Requested-With': 'XMLHttpRequest',
}
# res = requests.get(url, headers=headers)
# data = json.loads(res.text)
# cards = data["data"]["cards"]
# card_group = cards[0]["card_group"]
# for card in card_group:
#     user = card["user"]
#     followers_count = user["followers_count"]
#     follow_count = user["follow_count"]
#     if follow_count > 300 or followers_count > 300:
#         id = user["id"]
#         print(id)
#
# def getcontainerid(uid):
#     url = 'https://m.weibo.cn/api/container/getIndex?uid=6622287574&luicode=10000011&lfid=231051_-_followerstagBigV_-_5598061413_-_1042015:tagCategory_025&type=uid&value=6622287574'
#     res =  requests.get(url,headers=headers).text
#     data = json.loads(res)
#     data["data"][""]


# url = 'https://s.weibo.com/ajax_pic/list?q=%E8%87%AA%E6%8B%8D&page=11&_t=0&__rnd=1591079280464'
# res = requests.get(url, headers=headers)
# print(res.text)


import requests
import logging
import threadpool


class WbGrawler():
    def __init__(self, start=1, end=500):
        """
        参数的初始化
        :return:
        """
        self.baseurl = "https://m.weibo.cn/api/container/getIndex?containerid=2304131792328230&"
        # self.baseurl = "https://m.weibo.cn/api/container/getIndex?containerid=2304136403404743&"
        self.headers = {
            "Host": "m.weibo.cn",
            "Referer": "https://m.weibo.cn/p/2304131792328230",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "X-Requested-with": "XMLHttpRequest"
        }
        self.start_pages = start
        self.end_pages = end
        # 图片保存位置
        self.path = "./img/"
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    def getPageJson(self, page):
        """
        获取单个页面的json数据
        :param page:传入的page参数
        :return:返回页面响应的json数据
        """
        url = self.baseurl + "page=%d" % page
        try:
            response = requests.get(url, self.headers)
            if response.status_code == 200:
                return response.json()
        except requests.ConnectionError as e:
            print("error")
            self.logger.error("error", e.args)

    def parserJson(self, json):
        """
        解析json数据得到目标数据
        :param json: 传入的json数据
        :return: 返回目标数据
        """
        items = json.get("data").get("cards")
        for item in items:
            pics = item.get("mblog").get("pics")
            picList = []
            # 有些微博没有配图，所以需要加一个判断，方便后面遍历不会出错
            if pics is not None:
                for pic in pics:
                    pic_dict = {}
                    pic_dict["pid"] = pic.get("pid")
                    pic_dict["url"] = pic.get("large").get("url")
                    picList.append(pic_dict)
            yield picList

    # def is_face(self,jpg):
    #     image = face_recognition.load_image_file("./" + jpg)
    #
    #     # Find all the faces in the image using the default HOG-based model.
    #     # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    #     # See also: find_faces_in_picture_cnn.py
    #     face_locations = face_recognition.face_locations(image)
    #     if face_locations != []:
    #         return ("true")
    #     else:
    #         return ("false")

    def imgDownload(self, results):
        """
        下载图片
        :param results:
        :return:
        """
        for result in results:
            for img_dict in result:
                img_name = img_dict.get("pid") + ".jpg"
                try:
                    img_data = requests.get(img_dict.get("url")).content
                    with open(self.path + img_name, "wb") as file:
                        file.write(img_data)
                        file.close()
                        res = is_face(img_name)
                        if res == 'true':
                            print(img_name)
                        # print(img_name + "\tdownload successed!")
                except Exception as e:
                    self.logger.error(img_name + "\tdownload failed!", e.args)

    def startCrawler(self, page):
        page_json = self.getPageJson(page)
        results = self.parserJson(page_json)
        self.imgDownload(results)


if __name__ == '__main__':
    wg = WbGrawler(100, 200)
    pool = threadpool.ThreadPool(10)
    reqs = threadpool.makeRequests(wg.startCrawler, range(wg.start_pages, wg.end_pages))
    [pool.putRequest(req) for req in reqs]
    pool.wait()
