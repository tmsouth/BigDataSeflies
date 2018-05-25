# DataGrab executes a series of scripts that:
#   a)Download "selfie tweets" via the Twitter REST API - TwitterAccess.py
#   b)Download the corresponding images - ImageDownloader.py
#   c)Filter out images without, or with too many faces - FaceDetect.py
#
# DataGrab was written with the intention of setting up a cron job to run over a period of a few weeks


execfile("TwitterAccess.py")
print "Access Complete"

execfile("ImageDownloader.py")
print "Downloading Complete"


execfile("FaceDetect.py")
print "Detection Complete"