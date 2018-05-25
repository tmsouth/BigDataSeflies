import os
import pickle


ids=os.listdir("SelfieImages")

ids=ids[0:7140]

for i in range(0,len(ids)):
    ids[i]=ids[i][0:18]

pickle.dump(ids,open("Tweetidslist","w"))

