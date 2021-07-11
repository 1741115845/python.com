#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:dyy
import pygal
from random import randint
class Die():
	def __init__(self,num_sides=6):
		self.num_sides=num_sides

	def roll(self):
		return randint(1,self.num_sides)

def die_visual():
	die1=Die(6)
	die2=Die(10)
	results=[]
	for roll_num in range(50000):
		result =die1.roll()+die2.roll()
		results.append(result)
	frequencies=[]
	max_result=die1.num_sides+die2.num_sides
	for value in range(2,max_result+1):
		frequencie=results.count(value)
		frequencies.append(frequencie)
	return frequencies


def view():
	hist=pygal.Bar()
	hist.title="Result of rolling two D6 1000 times"
	hist.x_labels=list(range(2,17))
	hist.x_title="Result"
	hist.y_title="Frequency of Result"
	hist.add("D6+D10",die_visual())
	print(die_visual())
	hist.render_to_file('die_visual.svg')
view()
