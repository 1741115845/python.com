#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:dyy
import json
import pygal
import pygal_maps_world.maps
import dyy_章节16系统countries国别码 as country

filename='population_data.json'
print("测试git撤销修改123")
with open(filename) as f:
	# 将json数据转换成python能处理的数据格式
	pop_date=json.load(f)
cc_populatin={}
cc_pop1,cc_pop2,cc_pop3={},{},{}
for pop_dict in pop_date:
	if pop_dict['Year']=='2010':
		# 拿取国家名称
		country_name=pop_dict['Country Name']
		# 将数据转换成pytplot能处理的数据 拿取人口数据
		population=int(float(pop_dict['Value']))
		# print(country_name,':',population)
		code=country.get_country_code(country_name)
		if code:
			# 国别码为key,人口为value
			cc_populatin[code]=population
			# print(code,":",population)
		else:
			print("ERROR-",country_name)
for cc,pop in cc_populatin.items():
	if pop<10000000:
		cc_pop1[cc]=pop
	elif pop<1000000000:
		cc_pop2[cc]=pop
	else:
		cc_pop3[cc]=pop
wm=pygal_maps_world.maps.World()
# 南美洲分布
# wm.title='North,Central,and South America'
# wm.add('North America',['ca','mx','us'])
# wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
# wm.add('Soutn America',['ar','bo','cl','co','ec','gf','gy','pe','py','sr','uy','ve'])
# wm.render_to_file('america.svg')
# 南美洲人口分布
# wm.title='Population od Countries in North America'
# wm.add('North America',{'ca':3412600,'us':30934900,'mx':11342300})
# wm.render_to_file('na_population.svg')
# 全球人口分布
# wm.title='World Population in 2010, by Country'
# wm.add('2010',cc_populatin)
# wm.render_to_file('world_population.svg')
# 全球人口分组后分布
wm.title='World Population in 2010, by Country'
wm.add('0-10m',cc_pop1)
wm.add('10m-1bn',cc_pop2)
wm.add('>1bn',cc_pop3)
wm.render_to_file('group_world_population.svg')
