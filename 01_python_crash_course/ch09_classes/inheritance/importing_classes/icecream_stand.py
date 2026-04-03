from restaurant import Restaurant

class IcecreamStand(Restaurant):
	"""A simple attempt to model an ice cream stand."""

	def __init__(self, restaurant_name, cuisine_type, flavors = []):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to the icecream stand.
		"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors

	def describe_flavors(self):
		"""List the flavors available in the stand."""
		print("The following flavors are available in this shop.")
		for flavor in flavors:
			print("- " + flavor)

flavors = ['butterscotch', 'vanilla', 'chocolate', 'pista', 'fig & honey']
tasty_corner = IcecreamStand('Tasty Corner', 'Dessert', flavors)
tasty_corner.describe_restaurant()
tasty_corner.describe_flavors()