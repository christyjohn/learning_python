cars = ['bmw', 'audi', 'suburu','mitsubishi']

fav_car = 'bmw'

if(fav_car == 'jaguar'):
	print('My favorite car is Jaguar')

if(fav_car == 'bmw'):
	print("My favorite car is BMW")

if(fav_car == 'BMW'.lower()):
	print("My favorite car is BMW")

if('suburu' in cars):
	print("You have a Suburu in your garage.")

if('tata' not in cars):
	print("Tata is not among your cars.")