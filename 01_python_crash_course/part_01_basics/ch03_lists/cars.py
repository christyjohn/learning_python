cars = [ 'bmw', 'audi', 'toyota', 'suburu' ]
print("Here is the original list:")
print(cars) # ['bmw', 'audi', 'toyota', 'suburu']
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars.sort()
print("\nCars after permanently sorting:")
print(cars) # ['audi', 'bmw', 'suburu', 'toyota']
cars = [ 'bmw', 'audi', 'toyota', 'suburu' ]
print("\nHere is the original list:")
print(cars) # ['bmw', 'audi', 'toyota', 'suburu']
cars.sort(reverse=True)
print("\nHere is the cars list after permanently reverse sorted:")
print(cars) # ['toyota', 'suburu', 'bmw', 'audi']

cars = [ 'bmw', 'audi', 'toyota', 'suburu' ]
cars.reverse()
print("\nPrinting the original cars list in reverse:")
print(cars) # ['suburu', 'toyota', 'audi', 'bmw']
print("\nLength of cars list:")
print(len(cars))