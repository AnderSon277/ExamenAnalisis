
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "URgKLmlHaoUGggjynVvgELYqz"
csecret = "dLnT08kNMPB5hzEPjlslPdYtw2KAVtkAzujXAnjFX016EvJSTR"
atoken = "1279073084696399875-267GJBsV8ABXsCnAjx08jljsek666V"
asecret = "NMLRNi6Y6MYC7RornNesFggDxs3SBF9EgGQsR9eYSQd0J"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:ander123@localhost:5984/')
try:
    db = server.create('newyork')
except:
    db = server['newyork']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-74,40,-73,41]) 
