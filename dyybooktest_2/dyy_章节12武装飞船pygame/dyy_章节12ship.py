#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:dyy
import pygame
import time
class Ship():
	def __init__(self,ai_settings,screen):
		# 初始化飞船并设置初始位置
		self.screen=screen
		self.ai_seetings=ai_settings
		# 加载飞船图像并获取其外接矩形
		self.image=pygame.image.load('images\ship.jpg')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		# 将每艘新飞船放在屏幕底部中央
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		# rect.contenx只能移动整数所以通过变量进行转成浮点数
		self.center=float(self.rect.centerx)
		self.moving_right=False
		self.moving_left=False

	def blitme(self):
		# 在屏幕的指定位置绘制飞船
		self.screen.blit(self.image,self.rect)
	def update(self):
		 if self.moving_right and self.rect.right < self.screen_rect.right:
			 time.sleep(0.1)
			 self.center +=self.ai_seetings.ship_speed_factor
		 elif self.moving_left and self.rect.left>0:
			 time.sleep(0.1)
			 self.center -=self.ai_seetings.ship_speed_factor
		 # 飞船的X轴只认这个rect.centerx属性，且只存储整数值，对小数部分抹去
		 self.rect.centerx=self.center

