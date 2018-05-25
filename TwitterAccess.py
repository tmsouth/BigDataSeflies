import os
from TwitterSearch import *


tso = TwitterSearchOrder() # create a TwitterSearchOrder object
tso.set_keywords(['selfie']) #define search term
tso.set_language('en') # set language of tweets

ts = TwitterSearch(
    consumer_key = '',
    consumer_secret = '',
    access_token = '',
    access_token_secret = ''
 )  #create twitter search token

count=0  #counting varibles for seeing how much data was collected
countfiltered=0


IDs = open('SelfieImages/IDs.txt', 'w')
IDs.write("IDs = [") #IDs is file were collected data is saved


for tweet in ts.search_tweets_iterable(tso): #search tweets
    count += 1
    if tweet['text'][0:2]!='RT': #checking if retweet
        print tweet['created_at']
        try:
            TweetID = tweet["id_str"]
            UserID = str(tweet["user"]["id_str"])   #collecting data
            text = tweet['text']
            url = tweet["entities"]["media"][0]["media_url_https"]
            print TweetID
            print tweet['text']
            countfiltered +=1

            data = {"UserID":UserID,"TweetID":TweetID, "text":text,"url":url,"Json":tweet}
                #writing data to the file
            IDs.write(str(data)+",")

        except KeyError: #in case we try to access media when it has none ##tweet not saved
            print "No Media"

        except UnicodeEncodeError: #in case of emoji still saves just doesnt print
            print "Unicode-------------------------------------------"
IDs.close()

print count
print countfiltered