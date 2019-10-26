import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import csv

"""
Song Features we care about: acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,valence,tempo

Generates a CSV with the song features for every karaoke song given by a CSV
Also generates an average feature set to be passed to a naive classifier

Need to make the first part a function, and then pass a variable for writing CSVs so that it can be imported without constantly writing the CSVs
"""

def setGenerator(write,filepath):
    # Spotify Authorization informnation
    client_id = "1cc2b52f7c6447409439ddc56223fb26"
    client_secret = "c1e05ecad59f4208aea0fb91d79fdbd4"
    uri = "https://dknopf.github.io/Verse-a-tility"



    token = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret, proxies=None).get_access_token()

    # Open CSV of song names
    fh = open(filepath, 'r')
    reader = csv.reader(fh, delimiter = ',')
    songs = []
    for line in reader:
        song = line[0]
        songs.append(song)
    fh.close()

     # Access Spotify iteration
    spotify = spotipy.Spotify(token)

    ids = []
    for song in songs:
        track = spotify.search(song, limit = 1, market = 'US')
        id = track['tracks']['items'][0]['id']
        name = track['tracks']['items'][0]['name']
        ids.append((id,name))

    # Writes the CSV for all the song features for maybe implementing a better classifier
    if write:
        songcsv = open("song-features.csv",'w')
        songcsv.write("Title, ID, Acousticness, Danceability, Energy, Instrumentalness, Liveness, Loudness, Speechiness, Valence, Tempo\n")

    # Generating song features for each song given
    features = []
    for id,name in ids:
        fts = spotify.audio_features(id)[0]
        flist = [name,id,fts['acousticness'],fts['danceability'],fts['energy'],fts['instrumentalness'],fts['liveness'],fts['loudness'],fts['speechiness'],fts['valence'],fts['tempo']]
        features.append(flist)
        if write:
            songcsv.write(flist[0] + ',' + flist[1] + ',' + str(flist[2]) + ',' + str(flist[3]) + ',' + str(flist[4]) + ',' + str(flist[5]) + ',' + str(flist[6]) + ',' + str(flist[7]) + ',' + str(flist[8]) + ',' + str(flist[9]) + ',' + str(flist[10])+'\n')
    if write:
        songcsv.close()

    # Averaging all of the features together
    length = len(features)
    avg = [0,0,0,0,0,0,0,0,0]
    for list in features:
        for i in range(len(avg)):
            avg[i] += list[i+2]
    for i in range(len(avg)):
        avg[i] = avg[i]/length

    average = avg
    return average


"""
Everything down here was just experimentation with the dictionary scaffolding of spotipy
"""
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
