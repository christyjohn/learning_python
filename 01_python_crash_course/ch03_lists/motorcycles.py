motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append(['honda', 'enfield']) # ['ducati', 'yamaha', 'suzuki', ['honda', 'enfield']]
motorcycles.append('tvs') # ['ducati', 'yamaha', 'suzuki', ['honda', 'enfield'], 'tvs'] 
# motorcycles.append('ola', 'uber') # error
print(motorcycles)
motorcycles.insert(1, 'bmw') 
print(motorcycles) # ['ducati', 'bmw', 'yamaha', 'suzuki', ['honda', 'enfield'], 'tvs']
del motorcycles[4] 
print(motorcycles) # ['ducati', 'bmw', 'yamaha', 'suzuki', 'tvs']
del motorcycles[-1]
print(motorcycles) # ['ducati', 'bmw', 'yamaha', 'suzuki']
motorcycles.append('indian')
motorcycles.insert(3, 'harley')
motorcycles.append('enfield')
print(motorcycles) # ['ducati', 'bmw', 'yamaha', 'harley', 'suzuki', 'indian', 'enfield']
motorcycles.insert(-1, 'lml') 
print(motorcycles) # ['ducati', 'bmw', 'yamaha', 'harley', 'suzuki', 'indian', 'lml', 'enfield']
motorcycles.insert(-0, 'ola') # same as motorcycles.insert(0, 'ola')
print(motorcycles) # ['ola', 'ducati', 'bmw', 'yamaha', 'harley', 'suzuki', 'indian', 'lml', 'enfield']
last_owned = motorcycles.pop()
print(last_owned) # enfield
print("The last motorcycle I owned was a " + last_owned.title() + ".")  # The last motorcycle I owned was a Enfield.
print(motorcycles) # ['ola', 'ducati', 'bmw', 'yamaha', 'harley', 'suzuki', 'indian', 'lml']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.') # The first motorcycle I owned was a Ola.
motorcycles.remove('lml')
print(motorcycles) # ['ducati', 'bmw', 'yamaha', 'harley', 'suzuki', 'indian']
too_expensive = 'indian'
motorcycles.remove(too_expensive)
print("\nA " + too_expensive.title() + " is too expensive for me.")