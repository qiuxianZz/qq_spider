import requests
import threading
from lxml import etree
from nwerank.db_helper import get_conn, execute_sql, close_conn







# url = 'http://www.qdaily.com/tags/tagmore/1068/1567043221.json'
#
#
# def get_json(url):
#     """第一个json数据"""
#     headers = {
#         "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
#     }
#     json_data_list = []
#
#     url_list = []
#     response = requests.get(url=url,headers=headers)
#     # print(response.text)
#     data =  response.text
#     patterns = re.compile('"last_key":(.*?),"has_more":true},',re.S)
#     next_page  = patterns.findall(data)
#     # print(ext_page)
#     json_data_list.append(next_page)
#     for i in json_data_list:
#         for item in i:
#             # print(item)
#             url = 'http://www.qdaily.com/tags/tagmore/1068/{}.json'.format(item)
#
#             url_list.append(url)
#             print(url_list)
#
#             for item in url_list:
#                 get_data_url(item)
#
#     get_json(url=url)
#
#     # return next_page
#
#
#


#
# def get_data_url(url):
#     """获取数据的url"""
#     headers = {
#         "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
#     }
#     response = requests.get(url=url,headers=headers)
#     json_Data = response.text
#     urls = re.compile('{"post":{"id":(.*?),"genre"',re.S)
#     urls_list = urls.findall(json_Data)
#     # print(urls_list)
#     for item in urls_list:
#         url = 'http://www.qdaily.com/articles/{}.html'.format(item)
#         data = get_data(url=url)
#         urls_list.remove(item)
#         # print(data)
#         save_result(data)
#     # return urls_list



def formatData(data):
    # 处理字符串""
    if(data == None or data == ''):
        return  ""
    data=data.replace("'","\\\'")
    return data.replace('"','\\\"')



def save_result(result):
    """存储数据"""
    try:
        conn = get_conn()
        for item in result:
            # print(item)
            # name 关键字 用`name`
            sql = "insert into curiosity " \
                  "(genre,time,title,`name`,content_t,content,url)" \
                  "values ('%s','%s','%s','%s'," \
                  "'%s','%s','%s')" % (item["genre"],item["time"],item["title"], item["name"],formatData(item["content_t"]),formatData(item["content"]),item["url"])
            print(sql)
            execute_sql(sql,conn)
        close_conn(conn)
    except Exception as e:
        print(e)


def get_data(url):
    """数据"""
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    data = response.text
    content_list = []
    html = etree.HTML(data)

    genre = html.xpath('/html/body/div[3]/div/div[1]/div[1]/div/p/span[2]/text()')
    # print(genre)
    title = html.xpath('/html/body/div[3]/div/div[1]/div[1]/div/h2/text()')
    # print(title)
    name = html.xpath('/html/body/div[3]/div/div[1]/div[2]/div[1]/div[1]/span[1]/text()')
    # print(name)
    time = html.xpath('/html/body/div[3]/div/div[1]/div[2]/div[1]/div[1]/span[3]/text()')
    # print(time)
    content_t = html.xpath('/html/body/div[3]/div/div[1]/div[2]/p/text()')
    # print(content_t)
    contents = html.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]')
    content = []
    for item in contents:
        for i in item:
            result = ",".join(i.xpath('./text()'))
            content.append(result)
        # print(content)
    if(len(content_t) == 0):
        content_t = [""]
    data = {
        'genre':",".join(genre),
        'time':",".join(time),
        'title':  ",".join(title),
        'name':  ",".join(name),
        'content_t':  ",".join(content_t),
        'content':  ",".join(content),
        'url':url

    }
    content_list.append(data)
    # print(content_list)
    return content_list



# get_json(url=url)






page = 49701
def f():
    while True:
        global page
        page += 1
        url ='http://www.qdaily.com/articles/{}.html'.format(page)

        print(url)
        result = get_data(url)
        # print(result)
        for item in result:
            print(item)
            # for value in item.values():
            #     print(value)
            #     if value == '':
            #         break
            if item['genre'] != '':
                save_result(result)
                print('成功')





def main():
    threads = [threading.Thread(target=f) for _ in range(8) ]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
