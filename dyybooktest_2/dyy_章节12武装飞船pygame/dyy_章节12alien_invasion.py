#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:dyy

import pygame
from dyy_章节12武装飞船pygame import dyy_章节12settings as settings
import dyy_章节12ship as Ship
import dyy_章节12game_functions as gf
from pygame.sprite import Group
from dyy_章节13alien import Alien

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	# 设置画布窗口大小
	ai_settings=settings.Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	# screen=pygame.display.set_mode((600,400))
	# 设置窗口标题
	pygame.display.set_caption('Alen Ivasion')
	# 创建一只飞船
	ship=Ship.Ship(ai_settings,screen)
	bullets=Group()
	aliens=Group()
	gf.creat_fleet(ai_settings,screen,ship,aliens)
	# alien=Alien(ai_settings,screen)

	while True:
		# 循环监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,bullets)
		# 船移动
		ship.update()
		# 子弹移动
		gf.update_bullets(bullets)
		# 外星人移动
		gf.update_aliens(aliens)
		# 重新更新绘制屏幕
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)
	# pygame.display.flip()
run_game()
