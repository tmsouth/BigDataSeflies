import cv2
from cv2 import *
import pickle
IDs = pickle.load(open('Tweetidslist','r'))
dataarray=[]
Kill = False
fails=[]
count = 0
for each in IDs:
    try:
        count+=1
        print count
        print each
        image = cv2.imread('SelfieImages/'+str(each) + '.jpg')
        print "got one"
        if Kill == True:
            break

        while True:
            # display the image and wait for a keypress
            key = 0
            cv2.namedWindow("image", flags=WINDOW_NORMAL)
            cv2.resizeWindow("image", 800, 800)
            cv2.imshow("image", image)

            key = cv2.waitKey(1)
            Orient = 'blank'
            # if the 'r' key is pressed, reset the cropping region
            if key == ord('p'):
                fails+=[previous]
                print 'failed'
            elif key == ord('o'):
                Kill = True
                print 'last'
                print each
                break
            elif key == ord("q"):
                Orient = 'left'
                print 'left'
                break
            elif key == ord('e'):
                Orient = 'right'
                print 'right'
                break
            elif key == ord('w'):
                Orient = 'neither'
                print 'neither'
                break
            elif key == ord('c'):
                Orient = 'meme'
                print 'is meme'
                break
            elif key == ord('x'):
                Orient = 'fail'
                print 'not relevant'
                break
        previous = each
        data = {'ID': each, 'Orient': Orient}
        dataarray += [data]
        # save data
    except:
        print 'failed'
print dataarray
file = open('datastuff.txt','w')
file.write('Dataarray =')
file.write(str(dataarray))
print 'fails'