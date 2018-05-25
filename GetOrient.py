import pickle

execfile("datastuff.txt")

print Dataarray
pickle.dump(Dataarray,open("Orientations","w"))