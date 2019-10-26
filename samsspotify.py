import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import csv


# Spotify Authorization informnation
client_id = "1cc2b52f7c6447409439ddc56223fb26"
client_secret = "c1e05ecad59f4208aea0fb91d79fdbd4"
uri = "https://dknopf.github.io/Verse-a-tility"


token = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret, proxies=None).get_access_token()

# Open CSV of song names
# filepath = ""
# fh = open(filepath, 'r')
# reader = csv.reader(fh, delimiter = ',')
# songs = []
# for line in reader:
#     song = line[0]
#     songs.append(song)

# # Access Spotify iteration
spotify = spotipy.Spotify(token)

# for song in songs:
#     res = spotify.search(song, limit = 1, market = 'US')

song = "Whip it"
res = spotify.search(song, limit = 1, market = 'US')
# print(res)
for track in res['tracks']['items']:
    id = track['id']






    # print(thing['id'],thing['name'],thing['artists'][0]['name'])



# print(res['tracks']['items'][0].keys())
# print(res['tracks']['items'])







# util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri=uri)

# spotify = spotipy.Spotify()

# res = spotify.search(q = "Whip it", type = "song", limit = 10)
# print(res)
