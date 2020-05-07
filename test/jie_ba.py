import jieba

# -*- coding: utf-8 -*-
import jieba
#
# seg_str = "好好学习，天天向上。"
#
# print("/".join(jieba.lcut(seg_str)))    # 精简模式，返回一个列表类型的结果
# print("/".join(jieba.lcut(seg_str, cut_all=True)))      # 全模式，使用 'cut_all=True' 指定
# print("/".join(jieba.lcut_for_search(seg_str)))     # 搜索引擎模式

txt = open("三国演义.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)     # 使用精确模式对文本进行分词
counts = {}     # 通过键值对的形式存储词语及其出现的次数

for word in words:
    if len(word) == 1:    # 单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序

for i in range(10):
    word, count = items[i]
    print("{0:<5}{1:>5}".format(word, count))
