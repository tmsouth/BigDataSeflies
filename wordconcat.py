# wordconcat takes all words tweeted by 'left' and 'right' users, and concatinates all words into 2 lists
# for subsequent analysis

import pickle
import regex


#loading lists of ID's, dictionary and data:
leftids=pickle.load(open("LeftUserIDs","r"))
rightids=pickle.load(open("RightUserIDs","r"))
stopwords=pickle.load(open("stopwords","r"))
dictionary=pickle.load(open("HappinessDictionary","r"))


#for aaaallll de right ppls
count=0
rightwords=[]
for user in rightids:
    count+=1
    print len(rightids)-count
    tweets=pickle.load(open("UserTweets/"+str(user)+"tweets","r"))                  #loading tweets
    for tweet in tweets :
        for word in tweet['text'].lower().split():
            word=regex.sub(ur"\p{P}+", "", word)                                    #stripping punctuation
            if word not in stopwords:                                               #removing stopwords
                if word in dictionary:                                              #ensuring word is in dictionary
                    rightwords.append(word)                                         #appending word



# for aaaaalll the wrong(left... ha gedditt) ppls
count=0
leftwords=[]
for user in leftids:
    count+=1
    print len(leftids)-count
    tweets=pickle.load(open("UserTweets/"+str(user)+"tweets","r"))                  #loading tweets
    for tweet in tweets :
        for word in tweet['text'].lower().split():
            word=regex.sub(ur"\p{P}+", "", word)                                    #stripping punctuation
            if word not in stopwords:                                               #removing stopwords
                if word in dictionary:                                              #ensuring word is in dictionary
                    leftwords.append(word)                                         #appending word


#saving results.
pickle.dump(rightwords,open("rightwords","w"))
pickle.dump(leftwords,open("leftwords","w"))