import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import csv

"""
acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,valence,tempo
"""
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

songs = ['whip it','eye of the tiger']
ids = []
for song in songs:
    track = spotify.search(song, limit = 1, market = 'US')
    id = track['tracks']['items'][0]['id']
    name = track['tracks']['items'][0]['name']
    ids.append((id,name))


songcsv = open("song-features.csv",'w')
songcsv.write("Title, ID, Acousticness, Danceability, Energy, Instrumentalness, Liveness, Loudness, Speechiness, Valence, Tempo\n")

features = []

for id,name in ids:
    fts = spotify.audio_features(id)[0]
    feat_tup = (name,id,fts['acousticness'],fts['danceability'],fts['energy'],fts['instrumentalness'],fts['liveness'],fts['loudness'],fts['speechiness'],fts['valence'],fts['tempo'])
    features.append(feat_tup)
    songcsv.write()
print(features)

# song = "Whip it"
# track = spotify.search(song, limit = 1, market = 'US')
# id = track['tracks']['items'][0]['id']
# fts = spotify.audio_features(id)[0]
# comparison_tup = (fts['acousticness'],fts['danceability'],fts['energy'],fts['instrumentalness'],fts['liveness'],fts['loudness'],fts['speechiness'],fts['valence'],fts['tempo'])
# print(comparison_tup)



    # print(thing['id'],thing['name'],thing['artists'][0]['name'])



# print(res['tracks']['items'][0].keys())
# print(res['tracks']['items'])







# util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri=uri)

# spotify = spotipy.Spotify()

# res = spotify.search(q = "Whip it", type = "song", limit = 10)
# print(res)
