from wyy.db_helper import get_conn, execute_sql, close_conn


def save_result_album(data):
    """储存专辑信息"""
    try:
        conn = get_conn()
        # print(item)
        # name 关键字 用`name
        # {'album_id': '80535308', 'artist_id': '1873', 'album_name': '火火的歌', 'head_img': 'http://p2.music.126.net/PAlBviJ_B9j3Hm91SDzhjw==/109951164236701524.jpg?param=177y177', 'singer': '阿宝', 'publish_time': '2019-07-21', 'publish_company': '\n墨枫文化\n', 'share_count': '', 'comment_count': '1', 'desc': ''}

        sql = f'insert into xdn_music_163_album ' \
              f'(album_id,artist_id,album_name,head_img,singer,publish_time,publish_company,share_count,comment_count,`desc`)' \
              f'values ("{data["album_id"]}", "{data["artist_id"]}","{data["album_name"]}", "{data["head_img"]}", ' \
              f'"{data["singer"]}", "{data["publish_time"]}", "{data["publish_company"]}", "{data["share_count"]}",' \
              f' "{data["comment_count"]}", "{data["desc"]}")'
        print(sql)
        execute_sql(sql,conn)
        close_conn(conn)
    except Exception as e:
        print(e)


def save_result_user(data):
    """存储账号数据"""
    try:
        conn = get_conn()
        # print(item)
        # name 关键字 用`name
        sql = f'insert into xdn_music_163_user ' \
              f'(artist_id,user_id,nickname,description,home_url,head_img,tag,gender,dynamic_count,follower_count,fans_count,region,other_contact,introduce,is_china)' \
              f'values ("{data["artist_id"]}", "{data["user_id"]}", "{data["nickname"]}", ' \
              f'"{data["description"]}", "{data["home_url"]}", "{data["head_img"]}", "{data["tag"]}", "{data["gender"]}", "{data["dynamic_count"]}",' \
              f' "{data["follower_count"]}", "{data["fans_count"]}", "{data["region"]}","{data["other_contact"]}","{data["introduce"]}","{data["is_china"]}")'
        print(sql)
        execute_sql(sql,conn)
        close_conn(conn)
    except Exception as e:
        print(e)







def save_result_user_to(data):
    """存储账号数据"""
    try:
        conn = get_conn()
        # print(item)
        # name 关键字 用`name
        sql = f'insert into xdn_music_163_user ' \
              f'(artist_id,nickname,description,is_china)' \
              f'values ("{data["artist_id"]}", "{data["nickname"]}", ' \
              f'"{data["description"]}","{data["is_china"]}")'
        print(sql)
        execute_sql(sql,conn)
        close_conn(conn)
    except Exception as e:
        print(e)




def formatData(data):
    """处理sql字符串引号"""
    if(data == None or data == ''):
        return  ""
    data=data.replace("'","\\\'")
    return  data.replace('"','\\\"')






def save_result_song(data):
    """存储歌曲数据"""
    try:
        conn = get_conn()
        # print(item)
        # name 关键字 用`name
        sql = f'insert into xdn_music_163_song ' \
              f'(artist_id,music_id,mvid,`name`,comment_thread_id,comment_count,copyright_id,duration,`music_status`,`no`,score,album_id,album_name,album_pic_url)' \
              f'values ("{data["artist_id"]}", "{data["music_id"]}", "{data["mvid"]}", ' \
              f'"{data["name"]}", "{data["comment_thread_id"]}", "{data["comment_count"]}",' \
              f' "{data["copyright_id"]}", "{data["duration"]}", "{data["music_status"]}",' \
              f' "{data["no"]}", "{data["score"]}", "{data["album_id"]}",' \
              f' "{data["album_name"]}", "{data["album_pic_url"]}")'
        print(sql)
        execute_sql(sql,conn)
        close_conn(conn)
    except Exception as e:
        print(e)