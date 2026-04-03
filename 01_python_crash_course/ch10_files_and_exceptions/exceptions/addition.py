def addition(num1, num2):
	"""Adding two numbers"""
	return num1 + num2
	

while True:
	print("Enter 2 numbers, I will add them. (Enter 'q' to quit.)")
	num1 = input("Number 1: ")
	num2 = input("Number 2: ")
	if(num1 == 'q' or num2 == 'q'):
		break
	else:
		try:
			num1 = int(num1) # also can check if isinstance(numi1, (int, float)):
			num2 = int(num2)
		except (ValueError, TypeError):
			print("Please make sure you enter numbers.")
		else:
			print(addition(num1, num2))


""" 
# First approach
try:
	num1 = int(num1) 
	num2 =int(num2)
except ValueError:
	print("Please make sure you enter numbers.")
else:
	print(addition(num1, num2))
"""

# Second approach

	

 