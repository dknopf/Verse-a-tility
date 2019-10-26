import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

client_id = "1cc2b52f7c6447409439ddc56223fb26"
client_secret = "c1e05ecad59f4208aea0fb91d79fdbd4"
uri = "https://dknopf.github.io/Verse-a-tility"

username = "nalutrip"
scope = playlist-read-private

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #creates spotify object to access API

util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri=uri)
"""
Dictionary Format:
(songID,songTitle,songArtist,acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,valence,tempo)

"""

userSongs = {}
