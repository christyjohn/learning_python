usernames = ['admin', 'eric', 'christy', 'cecil']

for user in usernames:
	if user == 'admin':
		print("Hello " + user.title() + ", would you like to see as status " +
						" report?")
	else:
		print("Hello " + user.title() + ", thank you for logging in again.")

usernames = []

if usernames:
	for user in usernames:
		if user == 'admin':
			print("\nHello " + user.title() + ", would you like to see as status " +
							" report?")
		else:
			print("\nHello " + user.title() + ", thank you for logging in again.")
else:
	print("\nWe need some users")