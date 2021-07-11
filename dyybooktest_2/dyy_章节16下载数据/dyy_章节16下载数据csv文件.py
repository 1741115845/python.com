#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:dyy
import csv
from matplotlib import pyplot as plt
filename='sitka_weather_07-2014.csv'
with open(filename) as f:
	reader=csv.reader(f)
	head_row=next(reader)
	# print(head_row)
	# 解析csv文件中头部信息，了解文件数据每列的含义。可看出第0列是日期，第1列是最高温
	for index,column_header in enumerate(head_row):
		print(index,column_header)
	highs=[]
	# 循环获取所有数据的最高温数据，存放在列表中
	for row in reader:
		high=int(row[1])
		highs.append(high)
	# print(highs)
	# 对面板大小的设置
	fig =plt.figure(dpi=128,figsize=(10,6))
	plt.plot(highs,c='red')
	plt.title("Daily high temperatures,July 2014",fontsize=24)
	plt.xlabel('',fontsize=16)
	plt.ylabel("Temperature(F)",fontsize=16)
	plt.tick_params(axis='both',which='major',labelsize=16)
	plt.show()