# OrientWordCompare produces a plot comparing the frequencies with which words are used by left and right facing people

import pickle
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# loading concatinated lists of words (from wordconcat)
leftwords=pickle.load(open("leftwords","r"))
rightwords=pickle.load(open("rightwords","r"))

# computing frequency of all words used
leftcount=Counter(leftwords)
rightcount=Counter(rightwords)

# finding a total 'volume of words' for somewhat of a 'normalisation' for clearer results
tot=float(np.sum(rightcount.values())+np.sum(leftcount.values()))

# initialising lists:
rightscores=[]
leftscores=[]
words=[]

for word in leftcount:
    if len(word)> 2:                                                    #removing BS words
        if word in rightcount:                                          #ensuring word is in both lists
            rightscores.append(float(rightcount[word]/tot))
            leftscores.append(float(leftcount[word]/tot))
            words.append(word)

# plotting results:
plt.figure()
plt.loglog(leftscores,rightscores,"b.")
plt.xlabel("")
plt.show()


