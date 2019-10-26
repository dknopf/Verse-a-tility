import math
from SetGenerator import setGenerator

"""
Think the goal here is just to use K-Nearest Neighbor to naively find what is closest to the average from setGenerator
(acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,valence,tempo)
       0          1          2            3            4       5         6          7      8


takes in k, number of most karaokeable songs desired, and a dictionary of all songs in playlists from a given user formatted in {songID: (songTitle,songArtist,(acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,valence,tempo))
and returns closest_k: an ordered list of the most karaokeable songs in the form (ID,songTitle,songArtist)
"""
def kNN(k,songlist):

    # Average generated from the list of good karaoke songs
    avg = _______

    # Generate empty k length list
    closest_k = [""]*k

    # iterate through dictionary of songs
    for id in songlist:
        # take the audio features for a given song
        p2 = songlist[id][2]
        # Calculate the 9 dimensional distance from the average "good" point
        distance = (math.sqrt((avg[0]-p2[0])**2+(avg[1]-p2[1])**2+(avg[2]-p2[2])**2+(avg[3]-p2[3])**2+(avg[4]-p2[4])**2+(avg[5]-p2[5])**2+(avg[6]-p2[6])**2+(avg[7]-p2[7])**2+(avg[8]-p2[8])**2))
        # Replace audio features with the distance float within the dictionary
        songlist[id] = (songlist[id][0],songlistid[1],distance)

        # Checks distance of current song to those of the closest_k thus far
        for i in range(len(closest_k)):
            # checks if the current item of closest_k is empty or not, breaks if empty to stop duplication
            if closest_k[i] == "":
                closest_k[i] = id
                break
            else:
                # Compares current item's distance to that of current song, breaks if replaced to prevent duplication
                if songlist[closest_k[i]][2] > songlist[id][2]:
                    closest_k[i] = id
                    break

    # Converting closest_k from [id] to [id,songTitle,songArtist]
    for i in range(len(closest_k)):
        closest_k[i] = (closest_k[i],songlist[closest_k[i]][0],songlist[closest_k[i]][1])

    return closest_k
