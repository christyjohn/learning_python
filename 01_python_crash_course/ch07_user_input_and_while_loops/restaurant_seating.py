num_guests = input("How many guests are there? ")
num_guests = int(num_guests)

if num_guests > 8:
	print("Please wait until a table is free.")
else:
	print("Your table is ready. Please be seated")