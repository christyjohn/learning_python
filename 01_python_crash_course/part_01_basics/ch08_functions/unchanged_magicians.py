magicians = ['david', 'samrat', 'muthukad']

def make_great(magicians):
	great_magicians = []
	for magician in magicians:
		great_magicians.append("Great " + magician.title())
	return great_magicians

def show_magicians(magicians):
	print(make_great(magicians[:]))

show_magicians(magicians)
print(magicians)