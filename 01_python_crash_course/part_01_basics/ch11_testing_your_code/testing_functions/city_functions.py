def get_formatted_city_and_coutry(city, country, population=''):
	city_and_country = city.title() + ', ' + country.title()
	if population:
		city_and_country += ' - population ' +  str(population) + '.'
	return city_and_country
