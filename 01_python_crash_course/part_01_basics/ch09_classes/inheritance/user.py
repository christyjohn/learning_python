class User():
	"""A simple attempt to model a user."""

	def __init__(self, first_name, last_name, **user_info):
		self.user_details = {}
		self.first_name = first_name
		self.last_name = last_name
		for key, value in user_info.items():
			self.user_details[key] = value
		self.login_aattempts = 0

	def describe_user(self):
		"""Describing the user"""
		print(self.first_name)
		print(self.last_name)
		print(self.user_details)
		print("Login attempts: " + str(self.login_aattempts))

	def get_full_name(self):
		return self.first_name.title() + " " + self.last_name.title()

	def increment_login_attempts(self):
		self.login_aattempts += 1

	def reset_login_attempts(self):
		self.login_aattempts = 0


class Privilege():
	"""Model a privilege class to add in Admin class."""

	def __init__(self, privileges):
		self.privileges = privileges

	def show_privileges(self):
		"""Show privileges of admin user."""
		for privilege in self.privileges:
			print("- " + privilege)


class Admin(User):
	"""Model an admin user."""

	def __init__(self, first_name, last_name, privileges=[], **user_info):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to the admin user.
		"""
		super().__init__(first_name, last_name, **user_info)
		self.privileges = Privilege(privileges)


christy = Admin('christy', 'john', 
							location='Chengannur',
							field='Artificial Intelligence',
							job='Researcher',
							iq = 169)
christy.privileges.privileges = ['Can add post', 'Can delete post']
christy.describe_user()
print(christy.get_full_name() + " has following privileges:")
christy.privileges.show_privileges()

print()

cecil = Admin('cecil', 'john',
				location = 'Cochin',
				field = 'moderator')
cecil.privileges.privileges = ['Delete comments', 'Approve comments']
cecil.describe_user()
print(cecil.get_full_name() + " has following privileges:")
cecil.privileges.show_privileges()