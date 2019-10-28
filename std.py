import csv
import numpy as np
#import spotify

"""
File to find the standard deviation of the metrics within the training data in order to weight our difference

(acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,valence,tempo, popularity)
Title, ID, Acousticness, Danceability, Energy, Instrumentalness, Liveness, Loudness, Speechiness, Valence, Tempo, Popularity
  0     1     2                3          4            5             6         7          8          9       10        11

"""
fh = open("/Users/nalutripician/Documents/GitHub/Verse-a-tility/song-features.csv",'r')
reader = csv.reader(fh,delimiter = ',')

acousticness = []
danceability = []
energy = []
instrumentalness = []
liveness = []
loudness = []
speechiness = []
valence = []
tempo = []
popularity = []

for line in reader:
    if line[0] == "Title":
        pass
    else:
        acousticness.append(float(line[2]))
        danceability.append(float(line[3]))
        energy.append(float(line[4]))
        instrumentalness.append(float(line[5]))
        liveness.append(float(line[6]))
        loudness.append((float(line[7])))
        speechiness.append(float(line[8]))
        valence.append(float(line[9]))
        tempo.append(float(line[10]))
        popularity.append(float(line[11]))
fh.close()

acousticness = np.std(acousticness)
danceability = np.std(danceability)
energy = np.std(energy)
instrumentalness = np.std(instrumentalness)
liveness = np.std(liveness)
loudness = np.std(loudness)
speechiness = np.std(speechiness)
valence = np.std(valence)
tempo = np.std(tempo)
popularity = np.std(popularity)

open("std.text",'w').write("acousticness: " + str(acousticness) + "\ndanceability: " + str(danceability) + "\nenergy: " + str(energy) + "\ninstrumentalness: " + str(instrumentalness) + "\nliveness: " + str(liveness) + "\nloudness: " + str(loudness) + "\nspeechiness: " + str(speechiness) + "\nvalence: " +  str(valence) + "\ntempo: " + str(tempo) + "\npopularity: " + str(popularity))
