#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:dyy
import matplotlib.pyplot as plt
from random import choice

plt.rcParams["font.sans-serif"]=["Microsoft YaHei"]
# # 在x轴为2,y轴为4处画一个点
# # plt.scatter(2,4,s=200)
plt.title("散布图",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Square of Vaule",fontsize=14)
# plt.tick_params(axis="both",which='major',labelsize='14')
# plt.show()

# 绘制一系列的点
# x_values=[1,2,3,4,5]
# y_value=[1,4,9,16,25]
# matplotlib依此读取列表的数据进行绘制点
# plt.scatter(x_values,y_value,s=100)
# plt.show()

# 系统生成数据进行绘制点
# x_values=list(range(1,1001))
# y_values=[x**2 for x in x_values]
# print(y_values)
# 参数c可设置数据点颜色
# plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)
# plt.axis([0,1100,0,1100000])
# plt.show()

# 练习题15-1和2
# x_values=list(range(0,5001))
# y_values=[x**2 for x in x_values]
# plt.axis([0,5001,0,10000000])
# plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=8)
# plt.show()

#随机漫步图
class RandomWalk():
	def __init__(self,num_points=5000):
		self.num_points=num_points
		self.x_values=[0]
		self.y_values=[0]
	def get_step(self):
		derection=choice([1,-1])
		distance=choice([1,2,3,4,5])
		step = derection * distance
		return step

	def fill_walk(self):
		while len(self.x_values)<self.num_points:
			# x轴方向移动的位置
			x_step=self.get_step()
			# y轴方向移动的位置
			y_step=self.get_step()
			# y_derection=choice([1,-1])
			# y_distance=choice([1,2,3,4,5])
			# y_step=y_derection * y_distance
			# 如果在原地则重新开始
			if x_step==0 and y_step==0:
				continue

			# 计算下一次的x和y的位置
			next_x=self.x_values[-1] +x_step
			next_y=self.y_values[-1] +y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)

def re_visual():
	while True:
		rw=RandomWalk(5000)
		rw.fill_walk()
		# current_axes = plt.axes()
		# current_axes.get_xaxis().set_visible(False)
		# current_axes.get_yaxis().set_visible(False)

		point_numbers = list(range(rw.num_points))
		# plt.plot(rw.x_values,rw.y_values,linewidth=10)
		plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)
		# 突出起点和终点
		plt.scatter(0, 0, c='green', edgecolors='none', s=100)
		plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
		# plt.axis('off')
		# 关闭x轴刻度
		plt.xticks([])
		plt.yticks([])

		plt.show()

		keep_running = input("Make another walk? (y/n): ")
		if keep_running == 'n':
			break

re_visual()


