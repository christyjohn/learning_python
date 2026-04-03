class Restaurant():
	"""A simple attempt to model a restaurant."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize restaurant name and cuisine type."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(self.restaurant_name + " is a restautant serving " +
			self.cuisine_type + " food.")

	def open_restaurant(self):
		print("Restautrant " + self.restaurant_name + " is open.")

	def set_number_served(self, num_served):
		"""Set the number_served to the given value."""
		if num_served >= self.number_served:
			self.number_served = num_served
		else:
			print("You can't reduce the total number of customers served.")

	def increment_number_served(self, new_served):
		if new_served >= 0:
			self.number_served += new_served
		else:
			print("You can't reduce the total number of customers served.")

taj = Restaurant("Taj Hotel", "Indian")
#print(taj.restaurant_name)
#print(taj.cuisine_type)

taj.open_restaurant()
taj.describe_restaurant()
print("Numbers served: " + str(taj.number_served))
taj.number_served = 50
print("Numbers served: " + str(taj.number_served))
taj.set_number_served(345)
print("Numbers served: " + str(taj.number_served))
taj.increment_number_served(34)
print("Numbers served: " + str(taj.number_served))
taj.increment_number_served(-34)

'''
oberon = Restaurant("Oberon", "Continental")
palazo = Restaurant("Palazo", "Italian")

oberon.describe_restaurant()
palazo.describe_restaurant()
'''