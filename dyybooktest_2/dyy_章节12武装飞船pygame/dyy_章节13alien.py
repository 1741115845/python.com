#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:dyy
import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	def __init__(self,ai_settings,screen):
		super(Alien, self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		# 创建外星人
		# alien_url='image'+'\\'+'alien.jpg'
		self.image=pygame.image.load('images'+'\\'+'alien.jpg')
		self.rect=self.image.get_rect()
		# 每个外星人的位置都在左上边角附近
		self.rect.x=self.rect.width#设置为外星人的宽
		self.rect.y=self.rect.height#设置为外星人的高

		self.rect.x=float(self.rect.x)

	def bitme(self):
		self.screen.blit(self.image,self.rect)
	# 检查外星人移动是否到了边缘
	def check_edges(self):
		screen_rect=self.screen.get_rect()
		# 外星人的rect.right大于屏幕右边的话说明已经到了右边缘
		if self.rect.right>=screen_rect.right:
			return True
		elif self.rect.left<=screen_rect.left:
			return True

	# 外星人移动
	def update(self):
		self.x +=self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
		self.rect.x=self.x
