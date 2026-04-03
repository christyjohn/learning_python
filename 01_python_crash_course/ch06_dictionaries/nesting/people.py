people = [
	{'first_name' : 'Christy', 'last_name': 'john', 'country': 'india'},
]

person_2 = {
	'first_name': 'Marco',
	'last_name': 'Jansen',
	'country': 'south africa',
}

person_3 = {
	'first_name': 'bill',
	'last_name': 'gates',
	'country': 'usa',
}

people.append(person_2)
people.append(person_3)

#print(people)

for person in people:
	full_name = person['first_name'].title() + " " + person['last_name']
	print(full_name + " lives in " + person['country'].title() + ".")



