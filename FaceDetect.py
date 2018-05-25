import cv2
import os


#loads trained algorthim for face detection
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascade= cv2.CascadeClassifier("haarcascade_eye.xml")

#counting functions
MF=0
FC=0
NF=0

#appends IDs with a ] and executes
rawfile = open("SelfieImages/IDs.txt","r")
runfile = open("SelfieImages/tempID.txt","w")
runfile.write(rawfile.read()+"]")
runfile.close()
rawfile.close()
runfile = open("SelfieImages/tempID.txt","r")
execfile("SelfieImages/tempID.txt")


#opens the X file which counts which iteration of searching this is
try:
    Xf = open("X.txt", "r")
    if len(Xf.read())==0:
        Xf.close()
        Xf = open("X.txt","w")
        Xf.write("X=1")
except IOError:
        Xf = open("X.txt", "w")
        Xf.write("X=1")

Xf.close()
Xf = open("X.txt", "r")

execfile("X.txt")

#opens the sorted file for this execution
Sorted = open("SelfieImages/Sorted"+str(X)+".txt","w")
X+=1
Xf.close()
Xf = open("X.txt","w")
Xf.write("X="+str(X)) #adds 1 to X file



for info in IDs:
    # Read the image
    try:
        image = cv2.imread("SelfieImages/"+info["TweetID"]+".jpg")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print info["TweetID"]

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=20,
            minSize=(30, 30),
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            sub_face_gray = gray[y:y+h,x:x+h]
            sub_face_colour = image[y:y+h,x:x+h]

            eyes = eyeCascade.detectMultiScale(
                sub_face_gray,
                scaleFactor=1.1 ,
                minNeighbors=20,
                minSize=(30, 30),
            )

            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(sub_face_colour, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)


        if len(faces)>1:
            print "multiface"
            MF+=1
            os.remove("SelfieImages/"+info["TweetID"] + ".jpg")
        elif len(faces)<1:
            print "no face"
            NF+=1
            os.remove("SelfieImages/"+info["TweetID"] + ".jpg")
        elif len(faces)==1:
            cv2.imwrite("SelfieImages/AF"+ str(info["TweetID"])+ ".jpg",image) #saves only those with faces
            FC+=1
            print "YAY!! a face"
            info["Sort"] = 1
            Sorted.write(str(info) + ",")
    except cv2.error: #error if tweet is deleted
        print "Error"

#print counts of each varible
print "Multiface = " + str(MF)
print "No Face = " + str(NF)
print "Face count = " + str(FC)