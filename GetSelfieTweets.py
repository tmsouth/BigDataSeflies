# Due to silly errors with previous scripts, GetSelfieTweets was written to go back and retrieve the tweets corresponding
# to the images downloaded by ImageDownloader

import pickle
import twython
import time
import os

# accessing API:
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

twitter = twython.Twython(consumer_key, consumer_secret,access_token, access_token_secret)


# Opening list of Tweet ID's
IDs=pickle.load(open("Tweetidslist","r"))

# Retrieving tweets:

SelfieTweets=[]
count=0
for i in range(0,8000):
    try:
        id=IDs[i]
        count+=1
        try:
            tweet = twitter.show_status(id=id)
            TweetID = tweet["id"]
            UserID = str(tweet["user"]["id_str"])
            text = tweet['text']
            url = tweet["entities"]["media"][0]["media_url_https"]
            data = {"UserID": UserID, "TweetID": TweetID, "text": text, "url": url, "Json": tweet}
            print "got it"
            # writing data to the file
            SelfieTweets.append(data)
        except twython.exceptions.TwythonRateLimitError:                        #Rate limits were often hit
            print count
            print id
            print "Tooooooooo many tweets. Hold on, patience is a virtue."
            time.sleep(900)
        except KeyError:
            print "Faulty Tweet"
        except twython.exceptions.TwythonError:
            print "Tweet Deleted"
    except IndexError:                                                          #writing to file when we finished all the tweets
        pickle.dump(SelfieTweets, open("SelfieTweets", "w"))
        print"No More Tweets :D"
        break
