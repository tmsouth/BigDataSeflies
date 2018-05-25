# Selfies as Big Data, Analysis 
Using Twitter API’s to download tweets with the #Selfie tag. Detecting the orientation of the face and using this to examine the happiness of the caption used. 

Sentiment Analysis was performed by using the LabMT word happiness score data set.
 
Below are all the script names and a little description of their jobs:

Data Collection

  DataGrab.py : Created purely to execute the following three scripts sequentially:
  a) TwitterAccess.py : Accesses the twitter REST API to retrieve ‘selfie’ tweets
  b) ImageDownloader: Downloads images associated with the tweets retrieved, along with some filtration
  c) FaceDetect: looks through all downloaded images to detect faces, filtering out images that don’t contain one individual face (seeking an authentic ‘selfie’
  !!Bonus!!
  For some silly reason, an error in the above scripts meant that we were unable to save the tweets that were retrieved. Given that images were saved as the respective TweetID, the following two scripts could be used to get the sneaky tweets back:
  -getids.py :Reads off the TweetID’s from the folder containing the images
  -GetSelfieTweets.py : uses the TweetID’s to go back and re-retreive the tweets
  -SelfieUserTweetGrab.py : Looks at timelines of users who’s selfies have been dowloaded, and accesses up to 1000 of their most recent tweets

Processing

  -Sorter.py : Allows for the classification of images into categories ‘left facing’,’right facing’, ‘neither’ and ‘irrelevant’.
  -GetOrient.py : Retrieves data created by Sorter.py and sanitises for later use
  -UserOrientSort.py : Generates three lists of UserID’s corresponding to the ‘left’, ‘right’ and ’neither’ users

Analysis

  -SelfieUserSentimentAnalysis.py : Carries out sentiment analysis on each of the users, essentially assigning a happiness score to each account
  -OrientCompare.py :Generates a plot visualising the average sentiment of ‘left’,’right’ and ‘neither’ users
  -wordconcat.py : Generates two lists containing all words used by ‘left’ and right’ users respectively
  -OrientWordCompare.py : Generates a Comparison of the frequency with which words are used by left and right users.


