#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:dyy
import matplotlib.pyplot as plt
# 解决展示图中的中文显示不了的问题，指定默认字体
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
# 简单的折线图使用plot
squares=[1,4,9,25]
value=[1,2,3,5]
# 绘制x轴是value，y轴是squares，线条宽度为5的折线图
plt.plot(value,squares,linewidth=5)
# 折线图的标题设置
plt.title("平方数折线图",fontsize=24)
# 折线图x轴标题设置
plt.xlabel("value")
# 折线图y轴标题设置
plt.ylabel("squares of value")
plt.tick_params(axis='both',labelsize=10)
plt.show()



