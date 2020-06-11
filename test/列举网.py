import re

import requests
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
}
type_list = ['http://bj.lieju.com/jiazheng', 'http://bj.lieju.com/baojie', 'http://bj.lieju.com/banjia',
             'http://bj.lieju.com/guandaoshutong_dakong', 'http://bj.lieju.com/zhuangxiu_zhuangshi',
             'http://bj.lieju.com/diannaoweixiu', 'http://bj.lieju.com/shoujiweixiu',
             'http://bj.lieju.com/jiadianweixiu', 'http://bj.lieju.com/jiajuweixiu',
             'http://bj.lieju.com/bangongshebeiweixiu', 'http://bj.lieju.com/liyihunqing',
             'http://bj.lieju.com/xiezhen_sheying', 'http://bj.lieju.com/meirongmeiti', 'http://bj.lieju.com/lvyou',
             'http://bj.lieju.com/dingpiao', 'http://bj.lieju.com/songshui_songqi', 'http://bj.lieju.com/xianhua',
             'http://bj.lieju.com/shuizu_haixianchi', 'http://bj.lieju.com/kuaicanwaimai',
             'http://bj.lieju.com/wupinhuishou', 'http://bj.lieju.com/qitashenghuofuwu',
             'http://bj.lieju.com/kuaidi', 'http://bj.lieju.com/wuliu_huoyun',
             'http://bj.lieju.com/yinshua_baozhuang', 'http://bj.lieju.com/penhuizhaopai_zhika',
             'http://bj.lieju.com/zhaoshangjiameng', 'http://bj.lieju.com/gongsizhuce_nianjian',
             'http://bj.lieju.com/kuaiji_shenji_pinggu', 'http://bj.lieju.com/shejicehua',
             'http://bj.lieju.com/wangzhanjianshe_tuiguang', 'http://bj.lieju.com/zhanxiao_zhanlan',
             'http://bj.lieju.com/zhanhuifuwu', 'http://bj.lieju.com/qingdianyanchu', 'http://bj.lieju.com/zulin',
             'http://bj.lieju.com/fanyi_suji', 'http://bj.lieju.com/lipindingzhi',
             'http://bj.lieju.com/jianzhuweixiu', 'http://bj.lieju.com/falvzixun',
             'http://bj.lieju.com/guanggaomeiti', 'http://bj.lieju.com/qitashangwufuwu',
             'http://bj.lieju.com/jiangzuo_zhaopinhui', 'http://bj.lieju.com/huodongzhaoji',
             'http://bj.lieju.com/tuangou_dazhe', 'http://bj.lieju.com/jiebanchuyou',
             'http://bj.lieju.com/xiangyueyundong', 'http://bj.lieju.com/qitatongchenghuodong',
             'http://bj.lieju.com/jiajiao', 'http://bj.lieju.com/waiyupeixun', 'http://bj.lieju.com/zhiyepeixun',
             'http://bj.lieju.com/jixujiaoyu', 'http://bj.lieju.com/wenyi_tiyu', 'http://bj.lieju.com/liuxue_yimin',
             'http://bj.lieju.com/diannao_wangluo', 'http://bj.lieju.com/zhongxiaoxuejiaoyu',
             'http://bj.lieju.com/kaoyan_gongwuyuan', 'http://bj.lieju.com/qitajiaoyupeixun',
             'http://bj.lieju.com/shouji', 'http://bj.lieju.com/shoujipeijian', 'http://bj.lieju.com/zuoji',
             'http://bj.lieju.com/chongzhika', 'http://bj.lieju.com/xuniwupin', 'http://bj.lieju.com/taishidiannao',
             'http://bj.lieju.com/bijibendiannao', 'http://bj.lieju.com/pingbandiannao_ipad',
             'http://bj.lieju.com/diannaopeijian', 'http://bj.lieju.com/shuma_shelu',
             'http://bj.lieju.com/jiayongdianqi', 'http://bj.lieju.com/jiaju_chuju',
             'http://bj.lieju.com/jiaju_riyongbaihuo', 'http://bj.lieju.com/bangongyongpin_haocai',
             'http://bj.lieju.com/yinxiang_leqi_yingyin', 'http://bj.lieju.com/tushu_guangpan',
             'http://bj.lieju.com/yishu_gongyi_shoucangpin', 'http://bj.lieju.com/muying_ertongyongpin',
             'http://bj.lieju.com/fushi_xiangbao_xiemao', 'http://bj.lieju.com/yundong_jianshenqicai',
             'http://bj.lieju.com/wanju_youxiji', 'http://bj.lieju.com/jiancaizhuangshi',
             'http://bj.lieju.com/ershoushebei_jixie', 'http://bj.lieju.com/shuizu_yuju',
             'http://bj.lieju.com/qitawupin', 'http://bj.lieju.com/qichepiaoyuding',
             'http://bj.lieju.com/tejiajipiao', 'http://bj.lieju.com/yanchu_dianying',
             'http://bj.lieju.com/tiyusaishi', 'http://bj.lieju.com/jingqumenpiao', 'http://bj.lieju.com/jianshenka',
             'http://bj.lieju.com/youhuiquan', 'http://bj.lieju.com/xiaofeika', 'http://bj.lieju.com/gouwuquan',
             'http://bj.lieju.com/qitapiaowu', 'http://bj.lieju.com/chongwugou', 'http://bj.lieju.com/chongwumao',
             'http://bj.lieju.com/huaniaoyuchong', 'http://bj.lieju.com/chongwuyongpin_shipin',
             'http://bj.lieju.com/chongwudian_fuwu', 'http://bj.lieju.com/qitachongwuxiangguan',
             'http://bj.lieju.com/ershouqichemaimai', 'http://bj.lieju.com/xinchemaimai',
             'http://bj.lieju.com/diandongchemaimai', 'http://bj.lieju.com/zixingchemaimai',
             'http://bj.lieju.com/motuochemaimai', 'http://bj.lieju.com/pinche_shunfengche',
             'http://bj.lieju.com/jiaxiao_peilian', 'http://bj.lieju.com/zuche_daijia',
             'http://bj.lieju.com/qixiu_baoyang', 'http://bj.lieju.com/cheliangpeijian',
             'http://bj.lieju.com/qitacheliangxiangguan', 'http://bj.lieju.com/fangwuchuzu',
             'http://bj.lieju.com/fangwuqiuzu', 'http://bj.lieju.com/fangwuhezu', 'http://bj.lieju.com/fangwuduanzu',
             'http://bj.lieju.com/xinloupanchushou', 'http://bj.lieju.com/ershoufangchushou',
             'http://bj.lieju.com/ershoufangqiugou', 'http://bj.lieju.com/shangpuzushou_zhuanrang',
             'http://bj.lieju.com/xiezilouzushou', 'http://bj.lieju.com/changfang_cangku_tudi',
             'http://bj.lieju.com/zhongcanguan', 'http://bj.lieju.com/rihanliaoli', 'http://bj.lieju.com/xicanting',
             'http://bj.lieju.com/kuaican_xiaochi', 'http://bj.lieju.com/zizhucanting',
             'http://bj.lieju.com/dongnanyacai', 'http://bj.lieju.com/tianpinlengyin',
             'http://bj.lieju.com/mianbao_dangao', 'http://bj.lieju.com/kafeiguan', 'http://bj.lieju.com/chaguan',
             'http://bj.lieju.com/qitacanyin', 'http://bj.lieju.com/zhuangxiujiancai',
             'http://bj.lieju.com/huagongyuanliao', 'http://bj.lieju.com/wujinpeijian',
             'http://bj.lieju.com/dianziqijian', 'http://bj.lieju.com/diangongzhaoming',
             'http://bj.lieju.com/wujingongju', 'http://bj.lieju.com/gongyehaocai',
             'http://bj.lieju.com/jianzhushebei', 'http://bj.lieju.com/jixieshebei',
             'http://bj.lieju.com/hangyeshebei', 'http://bj.lieju.com/dianqishebei',
             'http://bj.lieju.com/jiaotongyunshushebei', 'http://bj.lieju.com/yiqiyibiao',
             'http://bj.lieju.com/wangluoanfangshebei', 'http://bj.lieju.com/qimopeijian',
             'http://bj.lieju.com/shenghuoxiaofeipin', 'http://bj.lieju.com/nonglinmuyu',
             'http://bj.lieju.com/xiaoshou_yewu', 'http://bj.lieju.com/kefu',
             'http://bj.lieju.com/shichang_yingxiao', 'http://bj.lieju.com/renshi_xingzheng_houqin',
             'http://bj.lieju.com/caiwu_shenji', 'http://bj.lieju.com/falv_zixun_cehua',
             'http://bj.lieju.com/jisuanji_wangluo_tongxin', 'http://bj.lieju.com/jinrong_baoxian',
             'http://bj.lieju.com/shangwu_maoyi_caigou', 'http://bj.lieju.com/wuliu_cangchu',
             'http://bj.lieju.com/fangchan_jianzhu_zhuangshi', 'http://bj.lieju.com/canyin_fuwu_lvyou',
             'http://bj.lieju.com/meishu_sheji_chuangyi', 'http://bj.lieju.com/guanggao',
             'http://bj.lieju.com/yiliao_yiyao', 'http://bj.lieju.com/dianzi_jixie_yibiao',
             'http://bj.lieju.com/wenti_yanyi_liyi', 'http://bj.lieju.com/bianji_chuban_chuanbo',
             'http://bj.lieju.com/jiaoyu_keyan_fanyi', 'http://bj.lieju.com/chanpin_pinpai_xiangmu',
             'http://bj.lieju.com/zhiliangguanli', 'http://bj.lieju.com/jingyingguanli',
             'http://bj.lieju.com/lingshou_cuxiao', 'http://bj.lieju.com/pugong_jigong', 'http://bj.lieju.com/siji',
             'http://bj.lieju.com/jiazheng_baojie', 'http://bj.lieju.com/wuye_baoan',
             'http://bj.lieju.com/meirong_meifa_jianshen', 'http://bj.lieju.com/xiuli_anzhuang',
             'http://bj.lieju.com/duanqigong', 'http://bj.lieju.com/zagong_xuetu', 'http://bj.lieju.com/jianzhi',
             'http://bj.lieju.com/qitazhaopin']

# for item in type_list:
#     print(item + '-page-1')


res = requests.get("http://bj.lieju.com/jiazheng-page-200", headers=headers)

tree = etree.HTML(res.text)
title = tree.xpath('/html/body/div[3]/div[1]/div[2]/div[1]')
for item in title[0]:
    urls = item.xpath('./div[2]/strong/a/@href')
    # tels = item.xpath('./div[3]/div[2]/a/div/@data-phone')
    tels = item.xpath('./div[3]/a/div/@data-phone')
    # tels = item.xpath('./div[2]/a/div/@data-phone')

    print(tels)
    if urls ==  []:
        continue
    urs = urls[0]
