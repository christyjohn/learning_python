import json

filename = "json/fav_number.json"

with open(filename) as f_obj:
	fav_number = json.load(f_obj)

print("Your favorite number is " + fav_number + "!")