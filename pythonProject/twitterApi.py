import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 

class GamingPlatform(object):
    def __init__(self, name):
        self.name = name
        self.positiveView = 0
        self.negativeView = 0

# https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
class TwitterAPI(object): 

	def __init__(self): 
		self.authenticate()

	def authenticate(self):
		# keys and tokens from the Twitter Dev Console 
		consumer_key = 'ZHvgTVAgG5G2bXCHSe1MIZlH7'
		consumer_secret = '1bZkOCD9KCmrj0BhHzgY1DCpDDpdcDBbNuFJlyb3KXFDz2Dsuo'
		access_token = '956979360308891649-srXjqsUqiSdlXiLCjWnLDzimKutSFK3'
		access_token_secret = 'VYIdOzrllvqJvkOZhnXchO0tjzjniExw3NMmN42TIe7uS'

		# attempt authentication 
		try: 
			self.auth = OAuthHandler(consumer_key, consumer_secret) 

			self.auth.set_access_token(access_token, access_token_secret) 

			self.api = tweepy.API(self.auth) 
			self.__isAuthenticated = True
			return True
		except: 
			print("Error: Authentication Failed") 
			return False

	def clean_tweet(self, tweet): 
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]\w+:\/\/\S+)", " ", tweet).split()) 

	def get_tweet_sentiment(self, tweet): 
		analysis = TextBlob(self.clean_tweet(tweet)) 
		if analysis.sentiment.polarity > 0: 
			return 'positive'
		elif analysis.sentiment.polarity == 0: 
			return 'neutral'
		else: 
			return 'negative'

	def get_tweets(self, query, count = 10):
		tweets = [] 

		try: 
			fetched_tweets = self.api.search(q = query, count = count) 

			for tweet in fetched_tweets: 
				parsed_tweet = {} 

				parsed_tweet['text'] = tweet.text 
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 

				if tweet.retweet_count > 0: 
					if parsed_tweet not in tweets: 
						tweets.append(parsed_tweet) 
				else: 
					tweets.append(parsed_tweet) 

			return tweets 

		except tweepy.TweepError as e: 
			print("Error : " + str(e)) 

		# fills in the positve and negative views of a gaming platform
	def get_public_views_on_platform(self,platform : GamingPlatform):
		query = platform.name
		negative_tweets_percentage = 0
		positive_tweets_percentage = 0

		tweets = self.get_tweets(query,25)

		positive_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
		negative_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
		

		if (len(positive_tweets) != 0): #to protect from zero division
			positive_tweets_percentage = 100*len(positive_tweets)/len(tweets)
		
		if (len(negative_tweets) != 0):
			negative_tweets_percentage = (len(tweets) - len(negative_tweets) - len(positive_tweets))/len(tweets)

		platform.positiveView = positive_tweets_percentage
		platform.negativeView = negative_tweets_percentage
		return platform


		#return [positive_tweets_percentage, negative_tweets_percentage] #return an array, or the actual platform
		#need emergency function



# def main(): 

# 	api = TwitterAPI() 
# 	tweets = api.get_tweets(query = 'Nebraska', count = 20) 

# 	ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
# 	print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 

# 	ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
# 	print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
# 	print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets))) 

# 	# # printing first 5 positive tweets 
# 	# print("\n\nPositive tweets:") 
# 	# for tweet in ptweets[:10]: 
# 	# 	print(tweet['text']) 

# 	# # printing first 5 negative tweets 
# 	# print("\n\nNegative tweets:") 
# 	# for tweet in ntweets[:10]: 
# 	# 	print(tweet['text']) 

# if __name__ == "__main__": 
# 	main() 
