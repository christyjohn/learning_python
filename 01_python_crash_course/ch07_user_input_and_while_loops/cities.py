prompt = "\nPlease enter the name of the city you would like to visit:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print("I'd like to go to " + city.title() + " !")