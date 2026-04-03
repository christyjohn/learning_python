rivers = {
	'nile': 'egypt',
	'misiisipi': 'usa',
	'thames': 'england',
	'ganga': 'India',
}

for river, country in rivers.items():
	print(river.title() + " runs through " + country.title() + ".".title())

print('\nThe rivers mentioned are:')
for river in rivers.keys():
	print(river.title())

print("\nThe countries mentioned are:")
for country in rivers.values():
	if(country == 'usa'):
		print(country.upper())
	else:
		print(country.title())