class Employee():

	def __init__(self, first_name, last_name, annual_salary):
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = annual_salary

	def give_raise(self, amount=''):
		if amount:
			self.annual_salary += amount
		else:
			self.annual_salary += 5000

		return self.annual_salary

	def show_employee(self):
		print(self.first_name.title() + ' ' + self.last_name.title() + 
			" - Annual salary: " + str(self.annual_salary))

christy = Employee('christy', 'john', 45000)
christy.give_raise()
christy.show_employee()
christy.give_raise(10000)
christy.show_employee()