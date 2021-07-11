#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:dyy
import sys
import pygame
from dyy_章节12bullet import Bullet
from dyy_章节13alien import Alien

def check_events(ai_settings,screen,ship,bullets):
	# 响应按键
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type ==pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type==pygame.KEYUP:
			check_keyup_events(event,ship)


# 按键按下后事件
def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key==pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key==pygame.K_LEFT:
		ship.moving_left=True
	elif event.key==pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key==pygame.K_q:
		sys.exit()

# 按键松开后事件
def check_keyup_events(event,ship):
	if event.key==pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key==pygame.K_LEFT:
		ship.moving_left=False

# 更新屏幕颜色
def update_screen(ai_settings,screen,ship,aliens,bullets):
	# 每次循环时都重绘屏幕颜色
	screen.fill(ai_settings.gb_color)
	# 循环绘制子弹颜色
	for bullet in bullets.sprites():
		# 调用子弹中的draw_bullet方法
		bullet.draw_bullet()
	# 在指定位置上绘制飞船
	ship.blitme()
	aliens.draw(screen)
	# alien.blitme()
	# 让最新绘制的屏幕可见
	pygame.display.flip()

# 更新子弹
def update_bullets(bullets):
	# 	编组调用编组.update方法时会里面的每一个sprite进行操作update方法（sprite中的update要自定义）
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom<0:
			bullets.remove(bullet)
# 创建新子弹到编组中
def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets)<ai_settings.bullet_allowed:
		new_bullet=Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
# 屏幕可创建多少个外星人
def get_number_aliens_x(ai_settings,alien_width):
	# 可用屏幕宽度
	avaliable_space_x = ai_settings.screen_width - alien_width
	# 屏幕科容纳外星人人数
	number_aliens_x = int(avaliable_space_x / (2 * alien_width))
	return number_aliens_x
# 计算屏幕可以容纳多少行外星人
def get_number_row(ai_settings,ship_height,alien_height):
	avaliabe_space_y=(ai_settings.screen_height)-3*alien_height-ship_height
	number_rows=int(avaliabe_space_y/(2*alien_height))
	return number_rows
# 创建一行外星人
def creat_alien(ai_setting,screen,aliens,alien_number,row_number):
	# 创建一个外星人并将其放在当前行
	alien=Alien(ai_setting,screen)
	alien_width=alien.rect.width
	alien.x=alien_width+2*alien_width*alien_number
	alien.rect.x=alien.x
	alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
	aliens.add(alien)

def creat_fleet(ai_settings,screen,ship,aliens):
	# 创建当行外星人
	alien=Alien(ai_settings,screen)
	# 屏幕可纳外星人人数
	number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows=get_number_row(ai_settings,ship.rect.height,alien.rect.height)
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			creat_alien(ai_settings,screen,aliens,alien_number,row_number)
# def check_fleet_edges(ai_settings,aliens):
# 	for alien in aliens.sprites():
# 		if alien.check_edges():
# 			change_fleet_direnction(ai_settings,aliens)
# 			break
# 	def change_fleet_direnction(ai_settings,aliens):
# 		for alien in aliens.sprites():
# 			alien.rect.y
def update_aliens(aliens):
	aliens.update()


