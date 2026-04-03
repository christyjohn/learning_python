filename = 'text_files/guest.py'

with open(filename, 'a') as file_object:
	name = input("Input your name:")
	file_object.write(name)