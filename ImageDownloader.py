import urllib
import os


rawfile = open("SelfieImages/IDs.txt","r")
runfile = open("SelfieImages/tempID.txt","w")
runfile.write(rawfile.read()+"]")
runfile.close()
rawfile.close()
runfile = open("SelfieImages/tempID.txt","r")
execfile("SelfieImages/tempID.txt")
#takes teh if no in IDs and appends a ] and then executes

# For each of the tweets, download the image
for i in range(0, len(IDs)):
    data = IDs[i]
    ID = data["TweetID"]
    url = data["url"]
    print url
    urllib.urlretrieve(str(url),"SelfieImages/"+str(ID)+".jpg")

runfile.close()