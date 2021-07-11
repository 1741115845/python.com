#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:dyy
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,ai_settings,screen,ship):
		super(Bullet,self).__init__()
		self.screen=screen
		# 在0，0处绘制一个bullet_width宽，bullet_heigtt长的矩形
		self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top
		self.y=float(self.rect.y)
		self.color=ai_settings.bullet_color
		self.speed_factor=ai_settings.bullet_speed_factor

	def update(self):
		# 向上移动
		self.y -=self.speed_factor
		self.rect.y=self.y

	def draw_bullet(self):
		# 在屏幕上绘制子弹 在screen中绘制color色的rect图形
		pygame.draw.rect(self.screen,self.color,self.rect)