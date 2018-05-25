# SenimentCompare produces a plot comparing the average sentiment of 'left', 'right', and 'neither' users


import pickle
import matplotlib.pyplot as plt
import numpy as np

# loading data:
LeftUsers=pickle.load(open("LeftUserIDs","r"))
RightUsers=pickle.load(open("RightUserIDs","r"))
NeitherUsers=pickle.load(open("NeitherUserIDs"))
Sentiments=pickle.load(open("ID_Sentiments","r"))

# creating lists of sentiments for each respective category:
LeftSents=[]
for id in LeftUsers:
    LeftSents.append(Sentiments["Sentiment"][str(id)])
NeitherSents=[]
for id in NeitherUsers:
    NeitherSents.append(Sentiments["Sentiment"][str(id)])
RightSents=[]
for id in RightUsers:
    RightSents.append(Sentiments["Sentiment"][str(id)])

# computing averages:
rightmean= np.mean(RightSents)
neithermean= np.mean(NeitherSents)
leftmean= np.mean(LeftSents)

sents=[rightmean,neithermean,leftmean]

# Plotting:
plt.figure()
plt.bar(range(1,4),sents,tick_label= ["Right","Neither","Left"],align="center")
plt.title("Comparison of Orientations and Sentiments")
plt.ylabel("Average Happiness")
plt.axis()
plt.show()
