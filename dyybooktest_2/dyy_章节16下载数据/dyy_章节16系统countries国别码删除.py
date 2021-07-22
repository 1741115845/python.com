#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:dyy
from pygal_maps_world.i18n import COUNTRIES
def get_country_code(country_name):
	for code,name in COUNTRIES.items():
		if name==country_name:
			return code
	return None
print("测试删除")
print("这个master分支")
print("这个是开发乙写的数据")




