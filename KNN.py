import math
from SetGenerator import setGenerator

"""
Think the goal here is just to use K-Nearest Neighbor to naively find what is closest to the average from setGenerator
(acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,valence,tempo)
       0          1          2            3            4       5         6          7      8


takes in k, number of most karaokeable songs desired, and a dictionary of all songs in playlists from a given user formatted in {songID: (songTitle,songArtist,(acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,valence,tempo))
and returns closest_k: an ordered list of the most karaokeable songs in the form (ID,songTitle,songArtist)
"""
def kNN(k,songdic):

    # Average generated from the list of good karaoke songs, (acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,valence,tempo)
    avg = (0.19487723953488362,0.6460232558139537,0.6768981395348841,0.006793604372093021,0.18605953488372096,-6.775758139534885,0.08851116279069769,0.584454418604651,120.67776744186055)

    # Generate empty k length list
    closest_k = [""]*k

    # iterate through dictionary of songs
    for id in songdic:
        # take the audio features for a given song
        p2 = songdic[id][2]
        # Calculate the 9 dimensional distance from the average "good" point
        distance = (math.sqrt(((avg[0]-p2[0])/0.85172278917612)**2
                                +((avg[1]-p2[1])/0.57212957365857)**2
                                +((avg[2]-p2[2])/0.65426874799986)**2
                                +((avg[3]-p2[3])/0.13654304306084)**2
                                +((avg[4]-p2[4])/0.53479358532162)**2
                                +((avg[5]-p2[5])/10.636845286776)**2
                                +((avg[6]-p2[6])/0.31753369128471)**2
                                +((avg[7]-p2[7])/0.84343775557373)**2
                                +((avg[8]-p2[8])/100)**2))
        # Replace audio features with the distance float within the dictionary
        songdic[id] = (songdic[id][0],songdic[id][1],distance)

        # Checks distance of current song to those of the closest_k thus far
        for i in range(k):
            # checks if the current item of closest_k is empty or not, breaks if empty to stop duplication
            if closest_k[i] == "":
                closest_k[i] = id
                break
            else:
                # Compares current item's distance to that of current song, breaks if replaced to prevent duplication
                if songdic[closest_k[i]][2] > songdic[id][2]:
                    j = k-1
                    while j > i:
                        closest_k[j] = closest_k[j-1]
                        j -= 1
                    closest_k[i] = id
                    break

    # Converting closest_k from [id] to [id,songTitle,songArtist]
    # for i in range(k):
    #     closest_k[i] = (closest_k[i],songdic[closest_k[i]][0],songdic[closest_k[i]][1])

    return closest_k
