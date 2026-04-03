pets = []

charlie = {
	'type': 'cat',
	'owner': 'christy'
}

brutus = {
	'type': 'dog',
	'owner': 'elizabeth',
}

pets.append(charlie)
pets.append(brutus)

for pet in pets:
	print("A " + pet['type'].title() + " owned by " + pet['owner'].title())