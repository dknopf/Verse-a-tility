import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util


def Merge(dict1, dict2):
    """
    Merges two Dictionarys
    """
    return(dict2.update(dict1))

client_id = "1cc2b52f7c6447409439ddc56223fb26"
client_secret = "c1e05ecad59f4208aea0fb91d79fdbd4"
uri = "https://dknopf.github.io/Verse-a-tility"

username = "nalutrip"
scope = "playlist-read-private"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #creates spotify object to access API

token = util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri=uri)

sp = spotipy.Spotify(auth=token)

playlists = sp.user_playlists(username) #gives a list of user playlists

songs = {}

i = 0
for playlist in playlists['items']:
    """
    Each iteration of the loop gets all the songs for that playlist
    """
    if (playlist['owner']['id'] == username): #checks to see if it is a user created playlist vs a saved one
        songDict = sp.user_playlist(username, playlist['id'], fields="tracks,next")
        playlistSongs = songDict['tracks']

        for i in range(len(playlistSongs['items'])):
            try:
                songs[playlistSongs['items'][i]['track']['id']]=(playlistSongs['items'][i]['track']['name'],playlistSongs['items'][i]['track']['artists'][0]['name'])
            except:
                print("empty boi")

print(songs)
print(len(songs))
"""
Dictionary Format:
songID: (songTitle,songArtist,(acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,valence,tempo))
"""

userSongs = {}
