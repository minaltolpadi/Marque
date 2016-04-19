import tweepy
import json
import textblob
import conf

brand = "trust"

class MyStreamListener(tweepy.StreamListener):

    def on_data(self, data):
    	#json to formatted data conversion
        formatted_data = json.loads(data)
        #check if the sentiment is positive
        if textblob.TextBlob(formatted_data["text"]).sentiment.polarity>0:
        	#print in format "username | message" 
        	print "@" + formatted_data["user"]["screen_name"] + " | " + formatted_data["text"] + "\n"


if __name__ == '__main__':

	#authentication
	auth = tweepy.OAuthHandler(conf.consumer_key, conf.consumer_secret)
	auth.set_access_token(conf.access_token, conf.access_token_secret)
	#create an instance
	myStreamListener = MyStreamListener()
	myStream = tweepy.Stream(auth,myStreamListener)
	#filter according to the brand name
	myStream.filter(track=[brand])



