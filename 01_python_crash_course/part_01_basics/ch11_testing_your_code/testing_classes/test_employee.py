import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Test the Employee class."""

	def setUp(self):
		self.christy = Employee('christy', 'john', 45000)

	def test_give_default_raise(self):
		self.assertEqual(50000, self.christy.give_raise())

	def test_custom_raise(self):
		self.assertEqual(55000, self.christy.give_raise(10000))

unittest.main()