import json

filename = "json/fav_number.json"

fav_number = input("Input your favorite number: ")

with open(filename, 'w') as f_obj:
	json.dump(fav_number, f_obj)
	print("We will remember your favorite number: " + fav_number + "!")