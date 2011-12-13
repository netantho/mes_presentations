import urllib

url = urllib.urlopen("http://search.twitter.com/search.json?q=python")

import json

monjson = json.loads(url.read())
for elem in monjson['results']:
    print elem['from_user_name']+" le "+elem['created_at']    
    print elem['text']+"\n"
