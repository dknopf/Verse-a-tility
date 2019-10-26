import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

client_id = "1cc2b52f7c6447409439ddc56223fb26"
client_secret = "c1e05ecad59f4208aea0fb91d79fdbd4"
uri = "https://dknopf.github.io/Verse-a-tility"

username = 'saolep'
scope = "playlist-read-collaborative"
token = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret, proxies=None).get_access_token()

spotify = spotipy.Spotify(token)
res = spotify.search("Whip it")
print(res)







# util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri=uri)

# spotify = spotipy.Spotify()

# res = spotify.search(q = "Whip it", type = "song", limit = 10)
# print(res)
