import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from KNN import kNN


def createTopTen(username):
    client_id = "1cc2b52f7c6447409439ddc56223fb26"
    client_secret = "c1e05ecad59f4208aea0fb91d79fdbd4"
    uri = "https://dknopf.github.io/Verse-a-tility"

    scope = "playlist-read-private,playlist-modify-private,user-read-private"

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #creates spotify object to access API

    token = util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri=uri)

    sp = spotipy.Spotify(auth=token)

    userID = sp.me()['id']
    playlists = sp.user_playlists(userID) #gives a Dictionary of user playlists

    songs = {}

    for playlist in playlists['items']:
        """
        Each iteration of the loop gets all the songs for that playlist
        """
        if (playlist['owner']['id'] == userID): #checks to see if it is a user created playlist vs a saved one
            songDict = sp.user_playlist(userID, playlist['id'], fields="tracks")
            playlistSongs = songDict['tracks']

            for i in range(len(playlistSongs['items'])):
                try:
                    songs[playlistSongs['items'][i]['track']['id']]=(playlistSongs['items'][i]['track']['name'],playlistSongs['items'][i]['track']['artists'][0]['name'])
                except:
                    print("empty boi") #for empty playlist

    """
    Dictionary (userSongs) Format:
    songID: (songTitle,songArtist,(acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,valence,tempo))
    """
    songList = songs.items()
    userSongs = {}

    for song in songList:
        """
        Audio analysis for all user songs
        """
        songID = song[0]
        songTitle = song[1][0]
        songArtist = song[1][1]
        try:
            features = sp.audio_features(songID)[0]

            acousticness = features['acousticness']
            danceability = features['danceability']
            energy = features['energy']
            instrumentalness = features['instrumentalness']
            liveness = features['instrumentalness']
            loudness = features['loudness']
            speechiness = features['speechiness']
            valence = features['valence']
            tempo = features['tempo']

            userSongs[songID] = (songTitle,songArtist,(acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,valence,tempo))
        except:
            print("")

    """
    Finding top karaoke songs and Playlist Creation
    <*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
    """

    top10 = kNN(10,userSongs)

    playlistID = (sp.user_playlist_create(user = userID,name = "Your Top 10 Karaoke Songs! Found by Verse-a-tility.",public = False))['id']

    sp.user_playlist_add_tracks(user=userID,playlist_id=playlistID,tracks=top10,position=None)


user = input("Enter your Spotify Username: ")
createTopTen(user)
