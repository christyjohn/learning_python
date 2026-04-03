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

	def increment_login_attempts(self):
		self.login_aattempts += 1

	def reset_login_attempts(self):
		self.login_aattempts = 0


christy = User('christy', 'john', 
							location='Chengannur',
							field='Artificial Intelligence',
							job='Researcher',
							iq = 169)

christy.increment_login_attempts()
christy.increment_login_attempts()
christy.increment_login_attempts()
christy.increment_login_attempts()
christy.describe_user()
christy.reset_login_attempts()
christy.describe_user()