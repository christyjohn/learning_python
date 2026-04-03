def make_sandwiches(*fillings):
	print("Making sandwiches with the following fillings: ")
	for filling in fillings:
		print("- " + filling)

make_sandwiches('cheese')
make_sandwiches('cheese', 'beef patty')
make_sandwiches('chicken patty', 'mayonnaise', 'onion')