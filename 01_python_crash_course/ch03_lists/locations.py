locations = [ 'zurich', 'las vegas', 'machu pichu', 'mali', 'ethiopia', 'nepal' ]
print("Original location list:")
print(locations) # ['zurich', 'las vegas', 'machu pichu', 'mali', 'ethiopia', 'nepal']

print("\nLocations in sorted order")
print(sorted(locations)) # ['ethiopia', 'las vegas', 'machu pichu', 'mali', 'nepal', 'zurich']

print("See the original list hasn't changed:")
print(locations) # ['zurich', 'las vegas', 'machu pichu', 'mali', 'ethiopia', 'nepal']

print("\nReversing the original list without altering the original list: ")
print(sorted(locations, reverse=True))

print("See the original list hasn't changed:")
print(locations) 

print("\nReversing the list permanently")
locations.reverse()

print("See the original list has reversed:")
print(locations) 

locations.reverse()
print("\nReversing again brigs itback to original order:")
print(locations)

locations.sort()
print("\nSorting the list permanently using sort()")
print(locations)

locations.sort(reverse=True)
print("\nReverse sorting the list permanently using sort()")
print(locations)

