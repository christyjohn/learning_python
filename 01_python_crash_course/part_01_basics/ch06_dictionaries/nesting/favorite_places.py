itinerary = {
	'christy': {
		'favorite_places_to_visit': ['zurich', 'bali', 'rio'],
	},
	'cecil': {
		'favorite_places_to_visit': ['london', 'kuala lampur'],
	},
	'elizabeth': {
		'favorite_places_to_visit': ['jerusalem', 'cairo', 'johennasberg']
	}
}

for person, fav_place in itinerary.items():
	for place in fav_place:
		print(person.title() + " likes to visit:" ) 
		for place in fav_place[place]:
			print(place.title())
	print("\n")