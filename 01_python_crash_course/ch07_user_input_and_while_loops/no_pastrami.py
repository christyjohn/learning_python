sandwich_orders = ['tuna', 'pastrami', 'falafel', 'pastrami', 'beef patty', 'chicken', 'pastrami']

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print("We have run out of pastrami. \nWe made following sandwiches.")
for sandwich in sandwich_orders:
	print(sandwich)