## importar mongo y twitter 
import pymongo
import pprint
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

'''========Conexion mongodb=========='''

myClient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myClient["DonalTrump"]
mycol = mydb["DonalTrump"]
posts = mydb.posts

########################API ########################
ckey = "URgKLmlHaoUGggjynVvgELYqz"
csecret = "dLnT08kNMPB5hzEPjlslPdYtw2KAVtkAzujXAnjFX016EvJSTR"
atoken = "1279073084696399875-267GJBsV8ABXsCnAjx08jljsek666V"
asecret = "NMLRNi6Y6MYC7RornNesFggDxs3SBF9EgGQsR9eYSQd0J"
####################################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = posts.insert_one(dictTweet);
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
    
'''===============LOCATIONS or BUSQUEDA=============='''    

#twitterStream.filter(locations=[-73.9544134,40.7642011,-73.9544134,40.7642011])
twitterStream.filter(track=['Donal','Trump'])