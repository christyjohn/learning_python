current_users = ['admin', 'Cecil', 'christy', 'mary']
current_users_lower  = [user.lower() for user in current_users]
new_users = ['cecil', 'john', 'Mary']

for new_user in new_users:
	if (new_user.lower() in current_users_lower):
		print("Username " + new_user + " already taken, use a new username.")
	else:
		print("Username " + new_user + " available.")
		