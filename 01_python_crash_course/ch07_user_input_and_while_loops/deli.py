sandwich_orders = ['tuna', 'falafel', 'beef patty', 'chicken']
finished_sanwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print("I made you a " + sandwich + " sandwich.")
	finished_sanwiches.append(sandwich)

print("--- Finshed Sandwiches ---")
for sandwich in finished_sanwiches:
	print(sandwich)