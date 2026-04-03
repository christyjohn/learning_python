def city_country(city, country):
	city_country = city.title() + ", " + country.title()
	return city_country

print(city_country('santiago', 'chile'))
print(city_country('delhi', 'india'))
print(city_country('kathmandu', 'nepal'))