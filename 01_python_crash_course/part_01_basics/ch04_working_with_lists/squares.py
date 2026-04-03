squares = []

for value in range(1, 11):
	#square = value ** 2
	#squares.append(square) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	# similar to
	squares.append(value ** 2)

print(squares)

squares2 = [value ** 2 for value in range(1, 11)]
print(squares2)