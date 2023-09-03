from requests.exceptions import HTTPError, Timeout
from lyricsgenius import Genius
import os

token = "Iw4MnqGJo2rOQPRWA2O7WEWO_aKpW3gvkgBTHdvhvLHm2tSGUME2kMbQ1omm47bw"
cwd = os.getcwd()

path = os.path.join(cwd, "lyrics.txt")

file = open(path, "w")
genius = Genius(token, skip_non_songs=True, 
	excluded_terms=["(Remix)", "(Live)"],
	remove_section_headers=True)


artist = "Metallica"

def get_lyrics(artist, n):
	try:
		songs = (genius.search_artist(artist, max_songs=n, sort='popularity')).songs
		songs = [song.lyrics for song in songs]

		with open(path, "w", encoding='utf-8') as file:
			file.write("\n <end> \n".join(songs))
		
		print(f"Songs grabbed: {len(songs)}")
	except Timeout:
		pass
	except HTTPError as e:
		print(e.errno)   # status code
		print(e.args[0]) # status code
		print(e.args[1]) # error message

