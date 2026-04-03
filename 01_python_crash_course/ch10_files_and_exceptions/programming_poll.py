filename = "text_files/programming_poll.txt"

with open(filename, 'a') as file_object:
	while True:
		reason = input("Enter why you like programming (Ente 'q' to quit')")
		if(reason == 'q'):
			break
		else:
			file_object.write(reason + "\n")