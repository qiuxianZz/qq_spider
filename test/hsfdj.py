import json

import pymysql
import requests

city_list = ['北京市', '上海市', '广州市', '深圳市', '成都市', '杭州市', '武汉市', '重庆市', '南京市', '天津市', '苏州市', '西安市', '长沙市', '沈阳市', '青岛市',
             '郑州市','大连市','东莞市','宁波市',
             '厦门市', '福州市', '无锡市', '合肥市', '昆明市', '哈尔滨市', '济南市', '佛山市', '长春市', '温州市', '石家庄市', '南宁市', '常州市', '泉州市', '南昌市',
             '贵阳市', '太原市', '烟台市', '嘉兴市', '南通市', '金华市', '珠海市', '惠州市', '徐州市', '海口市', '乌鲁木齐市', '绍兴市', '中山市', '台州市', '兰州市'
             "保定市", "镇江市", "扬州市", "桂林市", "唐山市", "三亚市", "湖州市", "呼和浩特市", "廊坊市", "洛阳市", "威海市", "盐城市", "临沂市", "江门市", "汕头市",
             "泰州市", "漳州市", "邯郸市", "济宁市", "芜湖市", "淄博市", "银川市", "柳州市", "绵阳市", "湛江市", "鞍山市", "赣州市", "大庆市", "宜昌市", "包头市",
             "咸阳市", "秦皇岛市", "株洲市", "莆田市", "吉林市", "淮安市", "肇庆市", "宁德市", "衡阳市", "南平市", "连云港市", "丹东市", "丽江市", "揭阳市",
             "延边朝鲜族自治州", "舟山市", "九江市", "龙岩市", "沧州市", "抚顺市", "襄阳市", "上饶市", "营口市", "三明市", "蚌埠市", "丽水市", "岳阳市", "清远市",
             "荆州市", "泰安市", "衢州市", "盘锦市", "东营市", "南阳市", "马鞍山市", "南充市", "西宁市", "孝感市", "齐齐哈尔市"
             "信阳市", "滁州市", "锦州市", "潮州市", "黄冈市", "开封市", "德阳市", "德州市", "梅州市", "鄂尔多斯市", "邢台市", "茂名市", "大理白族自治州", "韶关市",
             "商丘市", "安庆市", "黄石市", "六安市", "玉林市", "宜春市", "北海市", "牡丹江市", "张家口市", "梧州市", "日照市", "咸宁市", "常德市", "佳木斯市",
             "红河哈尼族彝族自治州", "黔东南苗族侗族自治州", "阳江市", "晋中市", "渭南市", "呼伦贝尔市", "恩施土家族苗族自治州", "河源市", "郴州市", "阜阳市", "聊城市", "大同市",
             "宝鸡市", "许昌市", "赤峰市", "运城市", "安阳市", "临汾市", "宣城市", "曲靖市", "西双版纳傣族自治州", "邵阳市", "葫芦岛市", "平顶山市", "辽阳市", "菏泽市",
             "本溪市", "驻马店市", "汕尾市", "焦作市", "黄山市", "怀化市", "四平市", "榆林市", "十堰市", "宜宾市", "滨州市", "抚州市", "淮南市", "周口市",
             "黔南布依族苗族自治州", "泸州市", "玉溪市", "眉山市", "通化市", "宿州市", "枣庄市", "内江市", "遂宁市", "吉安市", "通辽市", "景德镇市", "阜新市", "雅安市",
             "铁岭市", "承德市", "娄底市",
             "克拉玛依市", "长治市", "永州市", "绥化市", "巴音郭楞蒙古自治州", "拉萨市", "云浮市", "益阳市", "百色市", "资阳市", "荆门市", "松原市", "凉山彝族自治州",
             "达州市", "伊犁哈萨克自治州", "广安市", "自贡市", "汉中市", "朝阳市", "漯河市", "钦州市", "贵港市", "安顺市", "鄂州市", "广元市", "河池市", "鹰潭市",
             "乌兰察布市", "铜陵市", "昌吉回族自治州", "衡水市", "黔西南布依族苗族自治州", "濮阳市", "锡林郭勒盟", "巴彦淖尔市", "鸡西市", "贺州市", "防城港市", "兴安盟",
             "白山市", "三门峡市", "忻州市", "双鸭山市", "楚雄彝族自治州", "新余市", "来宾市", "淮北市", "亳州市", "湘西土家族苗族自治州", "吕梁市", "攀枝花市", "晋城市",
             "延安市", "毕节市", "张家界市", "酒泉市", "崇左市", "萍乡市", "乌海市", "伊春市", "六盘水市", "随州市", "德宏傣族景颇族自治州", "池州市", "黑河市", "哈密市",
             "文山壮族苗族自治州", "阿坝藏族羌族自治州", "天水市", "辽源市", "张掖市", "铜仁市", "鹤壁市", "儋州市", "保山市", "安康市", "白城市", "巴中市", "普洱市",
             "鹤岗市", "莱芜市", "阳泉市", "甘孜藏族自治州", "嘉峪关市", "白银市", "临沧市", "商洛市", "阿克苏地区", "海西蒙古族藏族自治州", "大兴安岭地区", "七台河市",
             "朔州市", "铜川市", "定西市", "迪庆藏族自治州", "日喀则市", "庆阳市", "昭通市", "喀什地区", "怒江傈僳族自治州", "海东市", "阿勒泰地区", "平凉市", "石嘴山市",
             "武威市", "阿拉善盟", "塔城地区", "林芝市", "金昌市", "吴忠市", "中卫市", "陇南市", "山南市", "吐鲁番市", "博尔塔拉蒙古自治州", "临夏回族自治州", "固原市",
             "甘南藏族自治州", "昌都市", "阿里地区", "海南藏族自治州", "和田地区", "克孜勒苏柯尔克孜自治州", "海北藏族自治州", "那曲地区", "玉树藏族自治州", "黄南藏族自治州",
             "果洛藏族自治州", "三沙市"
             ]





def get_conn():
    # 建立链接
    conn = pymysql.Connection(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        database='qx_data'
    )
    return conn


def execute_sql(sql, conn):
    # 获取游标
    cursor = conn.cursor()
    cursor.execute(sql)


def close_conn(conn):
    conn.commit()
    # 关闭连接
    conn.close()








def save_result_album(city):
    """储存专辑信息"""
    try:
        conn = get_conn()
        # print(item)
        # name 关键字 用`name
        # {'album_id': '80535308', 'artist_id': '1873', 'album_name': '火火的歌', 'head_img': 'http://p2.music.126.net/PAlBviJ_B9j3Hm91SDzhjw==/109951164236701524.jpg?param=177y177', 'singer': '阿宝', 'publish_time': '2019-07-21', 'publish_company': '\n墨枫文化\n', 'share_count': '', 'comment_count': '1', 'desc': ''}

        sql = 'insert ignore into city (city,`STATUS`  )VALUES(\"%s\",0)'% city
        execute_sql(sql,conn)
        close_conn(conn)
    except Exception as e:
        print(e)
        print(sql)


# for item in city_list:
#     save_result_album(item)





url = 'https://www.52hsfdj.com/haoshifu/userWorker/worker/list?token=bdf0bdf091244b8fb6720c80e06f82fc&digest=e757f6efc8ac3d4fb957e3a56e68bd23447ba5832420b9bf034df10d3fa02ae9&platformSource=wxapp&city=成都市&pageNum={}&screenType=1&lat=30.64242&lag=104.04311'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat"
}


def getlist(num):
    print(num)
    res = requests.get(url.format(num), headers=headers)
    print(res.text)
    data = json.loads(res.text)

    content = data["content"]
    for item in content:
        print(item)
        appointmentVal = item["appointmentVal"]
        city = item["city"]
        favorableVal = item["favorableVal"]
        fensi = item["fensi"]
        icon = item["icon"]
        id = item["id"]
        service1Name = item["service1Name"]
        skill1Name = item["skill1Name"]
        userName = item["userName"]
        tel = item["tel"]
    hasNextPage = data["hasNextPage"]
    return hasNextPage

# getlist(1)
# num = 1
# while True:
#     hasNextPage = getlist(num)
#     if hasNextPage == 'False':
#         break
#     num += 1


url = 'https://www.52hsfdj.com/haoshifu/userWorker/getUser/300052349?token=bdf0bdf091244b8fb6720c80e06f82fc&digest=42e15a051ba0cff78922a59659e53a6229bd09a7588798a206b5f2fcac63d068&platformSource=wxapp&lat=30.64242&lag=104.04311'
res = requests.get(url,headers=headers)
print(res.text)