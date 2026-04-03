import json

filename = "json/fav_number.json"

def read_fav_number():
	"""Get favorite number if available."""
	try:
		with open(filename) as f_obj:
			fav_number = json.load(f_obj)
	except FileNotFoundError:
		return None 
	else:
		return fav_number

def write_fav_number():
	"""Prompt for a new favorite number."""
	fav_number = input("What is your favorite number? ")
	with open(filename, 'w') as f_obj:
		json.dump(fav_number, f_obj)
	return fav_number

def fav_number_app():
	fav_number = read_fav_number()

	if fav_number:
		print("Your favorite number is " + fav_number + "!")
	else:
		fav_number = write_fav_number()
		print("We will remember your favorite number: " + fav_number + "!")

fav_number_app()