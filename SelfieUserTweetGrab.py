from TwitterSearch import *
import pickle
import os


ts = TwitterSearch(
    consumer_key='',
    consumer_secret='',
    access_token='',
    access_token_secret=''
)  # create twitter search token


SelfieTweets=pickle.load(open("SelfieTweets","r"))
usercount=0
for selfietweet in SelfieTweets[0:len(SelfieTweets)]:
    usercount+=1
    print usercount
    # setting user to search:
    user=int(selfietweet["UserID"])
    print user
    try:
        tuo = TwitterUserOrder(user)  # create a TwitterSearchOrder object
        tweets=[]
        count=0
        for tweet in ts.search_tweets_iterable(tuo): #search tweets
            count+=1
            try:
                TweetID = tweet["id_str"]
                UserID = str(tweet["user"]["id_str"])   #collecting data
                text = tweet['text']

                #appending tweet to tweets array
                data = {"UserID":UserID,"TweetID":TweetID,"text":text,"Json":tweet}
                tweets.append(data)

            except UnicodeEncodeError:
                None
            if count>=1000:
                break
    except :
        print "Account No Longer Accesible"



    pickle.dump(tweets, open("UserTweets/"+str(user)+"tweets", "w"))
