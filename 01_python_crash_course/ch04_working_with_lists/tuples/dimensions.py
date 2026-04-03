dimensions = (200, 50)
# dimensions[0] = 250 # TypeError: 'tuple' object does not support item assignment
# print(dimensions[0]) # 200
# print(dimensions[1]) # 50

print("original dimensions")
for dimension in dimensions:
	print(dimension)

dimesnions = (400, 100)
print("\nModified dimensions")
for dimension in dimensions:
	print(dimension)


