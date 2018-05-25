import os
import pickle
import pandas as pd
import regex


# Loading Happiness Dictionary
scores=pickle.load(open("HappinessDictionary","r"))

# Setting id's to iterate through
ids=os.listdir("UserTweets")

for i in range(0,len(ids)):
    ids[i] = ids[i][0:-6]

# Sentiment Analysis:
users=[]
sentiments=[]
count=0
for id in ids[1:5]:
    count+=1
    print count
    print id
    # Initiating:
    usertext=[]
    score=0
    wordcount=0
    # Loading user's tweets:
    usertweets=pickle.load(open("UserTweets/"+str(id)+"tweets","r"))

    # formatting each tweet for analysis
    for tweet in usertweets:
        text = tweet["text"].lower()                    #Lower-case
        text = regex.sub(ur"\p{P}+", " ", text)         #Stripping punctuation
        text = text.split()                             #Tokenising
        for word in text:
            usertext.append(word)                       #Appending each word to array of all language

    for word in usertext:
        if word in scores:
            wordcount +=1
            score= score+scores[str(word)]              #adding score for each word
        if wordcount!=0:
            ave=score/wordcount -5                      #Taking average
    users.append(id)
    sentiments.append(ave)                         #Appending to dictionary


ID_Sentiments=pd.DataFrame({"Sentiment":sentiments,"User":users},index=users)        #Creating DataFrame of ID's and Sentiment scores

print ID_Sentiments

pickle.dump(ID_Sentiments, open("ID_Sentiments", "w"))