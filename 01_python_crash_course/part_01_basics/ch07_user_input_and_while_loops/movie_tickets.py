prompt = "Please enter your age, and we will give you the price for your ticket"
prompt += ("\n(Enter 'quit' to quit)")

active = True

while(active):
	age = input(prompt)
	if age == 'quit':
		active = False
		break
	else:
		age = int(input(prompt))

	if age < 3:
		print("You are free to enter.")
	elif age >= 3 and age <= 12:
		print("Please pay $12 to enter.")
	else:
		print("Please pay $15 to enter.")

