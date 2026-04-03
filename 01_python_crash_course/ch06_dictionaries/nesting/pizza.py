pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}

# Summerize the order.
print('You ordered a ' + pizza['crust'] + '-crust pizza ' +
		'with following toppings:')

for topping in pizza['toppings']:
	print("\t" + topping)