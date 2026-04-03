dream_vacation = {}

# Set a flag to indicate polling is active
polling_active = True

while polling_active:
	# Prompt for person's name and dream vacation spot
	name = input('What is your name?')
	location = input('What is your dream vacation spot?')

	# Store the response in the dictionary:
	dream_vacation[name] = location

	# Find out if anyone else is going to take the poll.
	repeat = input("Would you like to let another person respond? (yes/ no)")
	if repeat == 'no':
		polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, location in dream_vacation.items():
	print(name.title() + " would like to visit " + location.title() + 
		" one day.")