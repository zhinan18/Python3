#! python3
# -*- coding: utf-8 -*-
import jieba  # 导入结巴模块
from collections import Counter  # 导入collections模块的Counter类


# 对文本文件txt进行分词，并统计词频，再显示结果
def get_words(txt):
    # S1 对文本进行分词
    list = jieba.cut(txt)  # 结巴模块的cut函数用于中文分词
    # S2 统计词频
    c = Counter()  # 创建空的Counter计数器，关于counter的知识可参考本博客的另一篇博文，位于python文件夹内
    for x in list:  # 分词结果中循环提取词语
        if len(x) > 1 and x != '\r\n':  # 略掉只有一个字的词语和回车、换行
            c[x] += 1  # 统计每个单词的计数值
    # S3 将结果可视化
    print('常用词频统计结果')
    for (k, v) in c.most_common(100):  # 只取出现值最高的前100个词语
        print('%s%s %s  %d' % ('  ' * (5 - len(k)), k, '*' * int(v / 3), v))  # 前5个位置打印空格或词语，有右对齐的效果


# 读取某文本文件(默认uft-8格式)
with open('1.txt','rb') as f:
    txt = f.read()
# 对该文件进行分词，并统计词频，显示结果
get_words(txt)