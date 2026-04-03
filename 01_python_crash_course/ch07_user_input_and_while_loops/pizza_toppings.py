prompt = "Please enter a pizza topping that you want on your pizza."
prompt += "\n(Enter 'quit' to stop adding toppings.)"
topping = ""

while(topping != 'quit'):
	print("We'll add " + topping + " to your pizza.")
	topping = input(prompt)
	
