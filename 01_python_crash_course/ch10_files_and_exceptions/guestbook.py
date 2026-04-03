filename = "text_files/guestbook.txt"

with open(filename, 'a') as file_object:
	while True:
		name = input("Enter your name (Ente 'q' to quit')")
		if(name == 'q'):
			break
		else:
			print("Hello, " + name)
			file_object.write(name + "\n")
