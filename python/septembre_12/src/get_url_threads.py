import urllib, threading
import time
 
class FileGetter(threading.Thread):
    def __init__(self, url):
        self.url = url
        self.result = None
        threading.Thread.__init__(self)
 
    def get_result(self):
        return self.result
 
    def run(self):
        try:
            mytime = time.ctime()
            f = urllib.urlopen(url)
            contents = f.read()
            f.close()
            self.result = contents
            print mytime+" "+url+" OK"
        except IOError:
            print "Could not open document: %s" % url

time_ini = time.ctime()

tab = []
for url in ["http://dl.google.com/android/android-sdk_r3-linux.tgz"]*5:
     tab.append(FileGetter(url))
     tab[len(tab)-1].start()

for thread in tab:
     thread.join()

print time_ini
print time.ctime()
