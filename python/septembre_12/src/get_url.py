import urllib
import time

def get_file(url):
     try:
	mytime = time.ctime()
        f = urllib.urlopen(url)
        contents = f.read()
        f.close()
        print mytime+" "+url+" OK"
     except IOError:
        print "Could not open document: %s" % url

time_ini = time.ctime()

for url in ["http://dl.google.com/android/android-sdk_r3-linux.tgz"]*5:
     get_file(url)

print time_ini
print time.ctime()
