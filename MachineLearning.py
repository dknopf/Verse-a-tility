import sklearn as sk
from sklearn.linear_model import LogisticRegression
import pandas as pd
import os
from SetGenerator import setGenerator

"""
Think the goal here is just to use K-Nearest Neighbor to naively find what is closest to the average from setGenerator
"""
def kNN(k,songlist):

    average = _______

    closest_k = [""]*k
    for id in songlist:



os.chdir('/Users/SEphron/Documents/GitHub/Karaokinator/')
heart = pd.read_csv('test.csv', sep=',',header=0)
heart.head()

y = heart.iloc[:,9]
X = heart.iloc[:,:9]

LR = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr').fit(X, y)
LR.predict(heart.iloc[460:,:])
round(LR.score(X,y), 4)
