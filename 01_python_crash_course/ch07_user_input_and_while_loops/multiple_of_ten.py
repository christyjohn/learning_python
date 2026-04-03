number = input("Please enter a number and I'll tell you if it is a " +
	"multiple of 10.")
number = int(number)

if number % 10 == 0:
	print("The number " + str(number) + " is divisible by 10.")
else:
	print("The number " + str(number) + " is not divisible by 10.")