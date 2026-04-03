def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, 'r', encoding='utf-8') as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		#msg = "Sorry, the file " + filename + " does not exist."
		#print(msg)

		# fail silently
		pass
	else:
		# count the approximate number of words in the file
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

#filename = '../text_files/alice.txt'
filenames = ['../text_files/alice.txt', '../text_files/siddhartha.txt', 
			'../text_files/moby_dick.txt', '../text_files/little_women.txt']

for filename in filenames:
	count_words(filename)
