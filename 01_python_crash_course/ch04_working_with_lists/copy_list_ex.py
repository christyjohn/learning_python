my_pizzas = [ 'chicen', 'pepperoni', 'lamb'] 
friend_pizzasa = my_pizzas[:]
my_pizzas.append('pineapple')
friend_pizzasa.append('bacon')

print("My pizzas are")
print(my_pizzas)
print("My firend pizzas are")
print(friend_pizzasa)

print("\nMy pizzas are")
for pizza in my_pizzas:
	print(pizza)

print("\nMy friend's pizzas are")
for pizza in friend_pizzasa:
	print(pizza)