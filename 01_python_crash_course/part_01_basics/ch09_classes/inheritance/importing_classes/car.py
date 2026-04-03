class Car():
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive na
		me."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_ododmeter(self, mileage):
		"""
		Set the ododmeter reading to the given value.
		Reject the change if it attempts to roll the ododmeter back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer.")

	def increment_ododmeter(self, miles):
		"""Add the given amount to the ododmeter reading."""
		self.odometer_reading += miles

	def fill_gas_tank(self):
		"""Add a method to smulate filling ga in car."""
		print("Filling gas in " + self.__repr__())

	def __repr__(self):
		return self.make.title() + ' ' + self.model.title() + "."