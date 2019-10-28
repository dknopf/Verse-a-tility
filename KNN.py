import math
from SetGenerator import setGenerator

"""
Think the goal here is just to use K-Nearest Neighbor to naively find what is closest to the average from setGenerator
(acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,valence,tempo,popularity)
       0          1          2            3            4       5         6          7      8        9


takes in k, number of most karaokeable songs desired, and a dictionary of all songs in playlists from a given user formatted in {songID: (songTitle,songArtist,(acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,valence,tempo))
and returns closest_k: an ordered list of the most karaokeable songs in the form (ID,songTitle,songArtist)
"""
def kNN(k,songdic):

    # Average generated from the list of good karaoke songs, (acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,valence,tempo,popularity)
    avg = (0.2444697192786831,0.15833042136638129,0.18666338209654074,0.07442656184492567,0.1499738350572088,0.13965890050056823,0.08923854841027239,0.2389087233514038,0.1271123360537627,0.133588214763193)

    # Generate empty k length list
    closest_k = [""]*k

    # iterate through dictionary of songs
    for id in songdic:
        # take the audio features for a given song
        p2 = songdic[id][2]
        # Calculate the 9 dimensional distance from the average "good" point
        distance = (math.sqrt(((avg[0]-p2[0])/1)**2
                                +((avg[1]-p2[1])/0.64756646216769)**2
                                +((avg[2]-p2[2])/0.76343558282209)**2
                                +((avg[3]-p2[3])/0.30441717791411)**2
                                +((avg[4]-p2[4])/0.61337423312883)**2
                                +((avg[5]-p2[5])/0.57120654396728)**2
                                +((avg[6]-p2[6])/0.36498977505112)**2
                                +((avg[7]-p2[7])/0.97713701431493)**2
                                +((avg[8]-p2[8])/0.5198773006135)**2
                                +((avg[9]-p2[9])/0.54638036809816)**2))
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
