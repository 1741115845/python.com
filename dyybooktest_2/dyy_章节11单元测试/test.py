#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:dyy
import city_functions as cf
import unittest

class AllTestCase(unittest.TestCase):

	def setUp(self):
		question="What language did you first learn to speak?"
		self.my_survey=cf.AnonymousSurvey(question)
		self.employee=cf.Employee('邓','莹莹',8000)
	def test_city_country(self):
		city_country=cf.city_councry('guangzhou','china')
		self.assertEqual(city_country,'Guangzhou,China')

	def test_city_country_population(self):
		city_country_population=cf.city_councry('guangzhou','china','5000000')
		self.assertEqual(city_country_population,'Guangzhou,China-population 5000000')

	# def test_surver
	def test_one_response(self):
		# question="What language did you first learn to speak?"
		# my_survey=cf.AnonymousSurvey(question)
		# print(my_survey.show_question())
		self.my_survey.store_response('china')
		# my_survey.show_results()
		self.assertIn('china',self.my_survey.responses)

	def test_more_response(self):
		# question='What language did you first learn to speak?'
		# my_survey=cf.AnonymousSurvey(question)
		responses=['china','english','aaa']
		for response in responses:
			self.my_survey.store_response(response)
		self.assertEqual(responses,self.my_survey.responses,'执行失败')
	def test_give_default_raise(self):
		self.employee.give_rasie()
		self.assertEqual(self.employee.annula_salary,13000,'验证不通过')
	def test_give_custom_raise(self):
		self.employee.give_rasie(7000)
		self.assertEqual(self.employee.annula_salary,15000,'验证不通过')

if __name__ == "__main__":
    unittest.main()
