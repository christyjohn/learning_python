def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a " + str(size) +
		"-inch pizza witht he following toppings:")
	for topping in toppings:
		print("- " + topping)