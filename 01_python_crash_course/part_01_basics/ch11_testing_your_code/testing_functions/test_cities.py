import unittest

from city_functions import get_formatted_city_and_coutry

class CityCountryTest(unittest.TestCase):
	"""Tests for city_functions.py."""

	def test_city_country(self):
		formatted_city_and_country = get_formatted_city_and_coutry('santiago', 'chile')
		self.assertEqual(formatted_city_and_country, 'Santiago, Chile')

	def test_city_country_population(self):
		formatted_city_and_country_with_population = \
		get_formatted_city_and_coutry('santiago', 'chile', 500000)
		self.assertEqual(formatted_city_and_country_with_population, 
			'Santiago, Chile - population 500000.')

unittest.main()