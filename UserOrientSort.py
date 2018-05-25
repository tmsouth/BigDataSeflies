import pandas
import pickle
import matplotlib.pyplot as plt


orients=pickle.load(open("Orientations","r"))
SelfieTweets=pickle.load(open("SelfieTweets"))

USERIDs=[]
ORIENTS=[]

for selfie in SelfieTweets:
    TweetID=selfie["TweetID"]
    # print TweetID
    UserID=selfie["UserID"]
    # print UserID
    for tweet in orients:
        if tweet["Orient"]!= "fail":
            if tweet["ID"]==str(TweetID):
                USERIDs.append(UserID)
                ORIENTS.append(tweet["Orient"])


LeftUserIDs=[]
RightUserIDs=[]
NeitherUserIDs=[]

for i in range(len(USERIDs)):
    if ORIENTS[i]=="left":
        LeftUserIDs.append(USERIDs[i])
    elif ORIENTS[i]=="right":
        RightUserIDs.append(USERIDs[i])
    else:
        NeitherUserIDs.append(USERIDs[i])

print "left"
print LeftUserIDs

print "right"
print RightUserIDs

print "neither"
print NeitherUserIDs

pickle.dump(LeftUserIDs,open("LeftUserIDs","w"))
pickle.dump(RightUserIDs,open("RightUserIDs","w"))
pickle.dump(NeitherUserIDs,open("NeitherUserIDs","w"))
