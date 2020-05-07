import time
from datetime import datetime
# import datetime

from QQ_music.qq_music_info import getinfo, parameter, parameter_1, current_time

#
# while True:
#     getinfo(62, 100, current_time)  # 飙升榜时间 100 每天更新
#     getinfo(27, 100, current_time)  # 新歌歌榜时间 100 新歌日榜
#     getinfo(4, 100, current_time)  # 流行指数榜时间 100 每天更新
#     getinfo(67, 100, current_time)  # 听歌识曲榜 100 每天更新
#     dayOfWeek = datetime.now().isoweekday()  ###返回数字1-7代表周一到周日
#     if dayOfWeek == 4:
#         getinfo(26, 300, parameter_1)  # 热歌榜时间 300 每周四更新
#         getinfo(59, 100, parameter_1)  # 香港榜 100 每周四更新
#         getinfo(5, 100, parameter_1)  # 内地榜 100 每周四更新
#         getinfo(61, 100, parameter_1)  # 台湾榜 100 每周四更新
#         getinfo(3, 100, parameter_1)  # 欧美榜 100 每周四更新
#         getinfo(16, 100, parameter_1)  # 韩国榜 100 每周四更新
#         getinfo(17, 100, parameter_1)  # 日本榜 100 每周四更新
#         getinfo(60, 100, parameter_1)  # 抖音排行榜 100 每周四更新
#         getinfo(28, 100, parameter_1)  # 网络歌曲榜 100 每周四更新
#         getinfo(57, 50, parameter_1)  # 电音榜 50 每周四更新
#         getinfo(58, 50, parameter_1)  # 说唱榜 50 每周四更新
#         getinfo(66, 50, parameter_1)  # AGG新歌榜 100 每周四更新
#         getinfo(65, 100, parameter_1)  # 国风热歌榜 100 每周四更新
#         getinfo(64, 100, parameter_1)  # 综艺新歌榜 100 每周四更新
#         getinfo(29, 100, parameter_1)  # 影视金曲榜 100 每周四更新
#         getinfo(70, 100, parameter_1)  # 达人音乐榜 100 每周四更新
#         getinfo(36, 100, parameter_1)  # 全名k歌 50 每周四更新
#     elif dayOfWeek == 3:
#         getinfo(52, 100, parameter_1)  # 腾讯音乐人 100 每周三更新
#         getinfo(105, 20, parameter)  # 日本公信榜 20 每周三更新
#     elif dayOfWeek == 2:
#         getinfo(108, 100, parameter)  # 美国公告榜 100 每周二更新
#     elif dayOfWeek == 5:
#         getinfo(107, 40, parameter)  # 英国uk榜 40 每周周五更新
#         getinfo(127, 50, parameter)  # 台湾kkbox榜 50 每周五更新
#     elif dayOfWeek == 6:
#         getinfo(114, 20, parameter)  # 香港商台榜 20 每周六更新
#     elif dayOfWeek == 1:
#         getinfo(129, 100, parameter)  # 韩国melon榜 100 每周一更新
#         getinfo(128, 100, parameter)  # YouTube榜 100 每周一更新
#     elif dayOfWeek == 7:
#         getinfo(123, 100, parameter)  # 美国iTunes榜 100 每周周日更新


getinfo(62, 100, current_time)  # 飙升榜时间 100 每天更新



