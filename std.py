import csv
import numpy as np
import spotify

"""
File to find the standard deviation of the metrics within the training data in order to weight our difference

(acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,valence,tempo)
Title, ID, Acousticness, Danceability, Energy, Instrumentalness, Liveness, Loudness, Speechiness, Valence, Tempo
  0     1     2                3          4            5             6         7          8          9       10

"""

fh = open("C:/Users/SEphron/Documents/Github/Verse-a-tility/song-features.csv",'r')
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

for line in reader:
    if line[0] == "Title":
        pass
    else:
        acousticness.append(float(line[2]))
        danceability.append(float(line[3]))
        energy.append(float(line[4]))
        instrumentalness.append(float(line[5]))
        liveness.append(float(line[6]))
        loudness.append(float(line[7]))
        speechiness.append(float(line[8]))
        valence.append(float(line[9]))
        tempo.append(float(line[10]))
fh.close()

acousticness = np.std(acousticness)
danceability = np.std(danceability)
instrumentalness = np.std(instrumentalness)
liveness = np.std(liveness)
loudness = np.std(loudness)
speechiness = np.std(speechiness)
valence = np.std(valence)
tempo = np.std(tempo)

print("acousticness: " + str(acousticness) + "\ndanceability: " + str(danceability) + "\ninstrumentalness: " + str(instrumentalness) + "\nliveness: " + str(liveness) + "\nloudness: " + str(loudness) + "\nspeechiness: " + str(speechiness) + "\nvalence: " +  str(valence) + "\ntempo: " + str(tempo))
