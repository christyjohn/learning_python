filename = "text_files/python.txt"

print("Here are the advantages of Python as a language:")

'''
with open(filename) as file_object:
	contents = file_object.read()

print(contents.strip())
'''

'''
pi_string = ''
with open(filename) as file_object:
	l

for line in lines:
	pi_string += line.strip()


print(pi_string)
'''

with open(filename) as file_object:
	lines = file_object.readlines()
	
for line in lines:
	new_line = line.replace('Python', 'Ruby')
	print(new_line)