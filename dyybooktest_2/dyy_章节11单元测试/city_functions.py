#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:dyy
def city_councry(ciyt,country,population=None):
	# ciyt=ciyt
	# contry=contry
	if population!=None:
		city_councry=ciyt.title()+","+country.title()+"-population "+population
	else:
		city_councry=ciyt.title()+","+country.title()
	return city_councry
# 问卷
class AnonymousSurvey():
	# 收集问题
	def __init__(self,question):
		self.question=question
		self.responses=[]
	# 展示问题
	def show_question(self):
		print(self.question)
	# 添加问题答案
	def store_response(self,new_response):
		self.responses.append(new_response)
	# 展示问题答案
	def show_results(self):
		print("Survey results:")
		for response in self.responses:
			print('-',response)


# def main():
# 	question="What language did you first learn to speak?"
# 	my_survey=AnonymousSurvey(question)
# 	my_survey.show_question()
# 	print("Enter 'q' at any time to quit.")
# 	while True:
# 		response=input('Language:')
# 		if response!='q':
# 			my_survey.store_response(response)
# 		else:
# 			break
# 	print('Thank for everyone who participated in the survey!')
# 	my_survey.show_results()
#
# main()

class Employee():
	def __init__(self,first_name,last_name,annula_salary):
		self.first_name=first_name
		self.last_name=last_name
		self.annula_salary=annula_salary
	def give_rasie(self,add_salary=5000):
		self.annula_salary+=add_salary
