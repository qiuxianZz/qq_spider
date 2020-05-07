import random
import time

import uiautomator2 as u2

list = ['信任就像一张纸，皱了，即使抚平，也恢复不了原样了。', '时间真是一个让人讨厌的东西，它不经任何人同意就任意改变一切', '每一个你讨厌的现在，都有一个不够努力的曾经',
        '没有人可以回到过去重新开始，但谁都可以从现在开始，书写一个全然不同的结局。', '表白或被表白并不可怕，可怕的是，结局不是谈一次恋爱，而是少一个朋友。',
        '有些记忆，注定无法抹去。就象有些人，注定无法替代一样。',
        '人有两条路要走，一条是必须走的，一条是想走的，你必须把必须走的路走漂亮，才可以走想走的路。',
        '我们最怕看到的，不是两个相爱的人互相伤害，而是两个爱了很久很久的人突然分开了，像陌生人一样擦肩而过。',
        '一个人变强大的最好方式，就是拥有一个想要保护的人。',
        '人生三大遗憾：不会选择。不坚持选择。不断地选择。',
        '人生有两种境界，一种是痛而不言，另一种是笑而不语。',
        '世事离戏只有一步之远。人生离梦也只有一步之遥。生命最有趣的部分，正是它没有剧本没有彩排不能重来。生命最有分量的部分，正是我们要做自身，承担所有的责任。',
        ]


def info():
    d.set_fastinput_ime(True)
    content = random.choice(list)
    d.send_keys(content)
    d.set_fastinput_ime(False)
    d(resourceId="com.tencent.mobileqq:id/fun_btn").click()



d = u2.connect('127.0.0.1:21503')  # 连接设备
d(text="QQ").click()
d.xpath('//*[@resource-id="android:id/tabs"]/android.widget.FrameLayout[1]').click()
# d.xpath('//*[@resource-id="com.tencent.mobileqq:id/elv_buddies"]/android.widget.LinearLayout[2]').click()
# d.xpath('//*[@resource-id="com.tencent.mobileqq:id/elv_buddies"]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
d.xpath('//*[@resource-id="com.tencent.mobileqq:id/elv_buddies"]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.view.View[2]').click()
d(resourceId="com.tencent.mobileqq:id/txt", text="发消息").click()
d(resourceId="com.tencent.mobileqq:id/input").click()
for item in range(10):
    info()
    time.sleep(3)
d(resourceId="com.tencent.mobileqq:id/input")
# d(text="QQ音乐").click()
# d(resourceId="com.tencent.qqmusic:id/byj").click()
# d(resourceId="com.tencent.qqmusic:id/e26", text="飙升榜").click()
# d.xpath('//*[@resource-id="com.tencent.qqmusic:id/r8"]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]').click()
# d(resourceId="com.tencent.qqmusic:id/che").click()
#
# d(text="今日头条").click()
# d(resourceId="com.ss.android.article.news:id/bo_").click()
# d(resourceId="com.ss.android.article.news:id/vr").click()
# d.set_fastinput_ime(True)
# d.send_keys("环球网")
# d.set_fastinput_ime(False)
# d.xpath('//*[@resource-id="tt-nav-bar-ul"]/android.view.View[6]').click()
# d(description="环球网 1867.8万粉丝 · 环球网官方账号").click()

# d(resourceId="com.ss.android.article.news:id/vo").click()
# d(description="环球网 1867.8万粉丝 · 环球网官方账号").click()
# d(scrollable=True).scroll(steps=10)
# # d(resourceId="com.ss.android.article.news:id/cue").click()
