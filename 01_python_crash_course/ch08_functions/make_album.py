def make_album(artist_name, album_title, num_tracks = 4):
	album = {}
	album['artist'] = artist_name.title()
	album['title'] = album_title.title()
	album['number of tracks'] = num_tracks
	return album

def prompt_user():
	active = True
	while active:
		prompt = "\nWould you like to add album details?"
		prompt += "\n(Enter 'q' if you want to quit)"
		user_input = input(prompt)
		if user_input == 'q':
			active = False
			break

		prompt = "\nPlease enter the artist name:"
		artist_name = input(prompt)

		prompt = "Please enter album title:"
		album_title = input(prompt)

		prompt = "Please input album track number. Leave blank for default(4)"
		num_tracks = input(prompt)

		if num_tracks:
			print(make_album(artist_name, album_title, num_tracks))
		else:
			print(make_album(artist_name, album_title))
			
prompt_user()