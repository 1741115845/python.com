#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:dyy
class Settings():
	def __init__(self):
		self.screen_width=1100
		self.screen_height=600
		self.gb_color=(230,230,230)
		self.ship_speed_factor =8.5
		# 子弹设置
		self.bullet_speed_factor=1
		self.bullet_width=3
		self.bullet_height=15
		self.bullet_color=(60,60,60)
		self.bullet_allowed=3
		# 外星人速度
		self.alien_speed_factor=0.1
		self.fleet_drop_speed=0.2
		# fleet_direction为1表示向右移动，-1表示向左
		self.fleet_direction=1

