import re
import tweepy
from tweepy import OAuthHandler 
from textblob import TextBlob 

class GamingPlatform(object):
    def __init__(self, name):
        self.name = name
        self.positiveView = 0
        self.negativeView = 0


class TwitterAPI(object): 
    
# DO NOT EDIT CODE ABOVE THIS LINE ==========================================


    #   ------------- PROBLEM 1 -------------  
    # Given a sentiment number 
    # if the number is greater than zero, return 'positive'
    # if the number is equal to zero, return 'neutral'
    # if the number is less than zero, return 'negative'
    def get_tweet_sentiment(self, sentiment): 
        
        # todo: return correct sentiment
        
        return 'something fancy'


    
    
# DO NOT EDIT CODE BELOW THIS LINE ===========================================

    def __init__(self): 
        self.authenticate()

# DO NOT EDIT THIS CODE
    def authenticate(self):
        # keys and tokens from the Twitter Dev Console 
        consumer_key = 'ZHvgTVAgG5G2bXCHSe1MIZlH7'
        consumer_secret = '1bZkOCD9KCmrj0BhHzgY1DCpDDpdcDBbNuFJlyb3KXFDz2Dsuo'
        access_token = '956979360308891649-srXjqsUqiSdlXiLCjWnLDzimKutSFK3'
        access_token_secret = 'VYIdOzrllvqJvkOZhnXchO0tjzjniExw3NMmN42TIe7uS'


        try: 
            self.auth = OAuthHandler(consumer_key, consumer_secret) 

            self.auth.set_access_token(access_token, access_token_secret) 

            self.api = tweepy.API(self.auth) 
            self.__isAuthenticated = True
            return True
        except: 
            print("Error: Authentication Failed") 
            return False
        
# DO NOT EDIT THIS CODE
    def clean_tweet(self, tweet): 
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]\w+:\/\/\S+)", " ", tweet).split()) 

# DO NOT EDIT THIS CODE
    def get_tweets(self, query, count = 10):
        tweets = [] 

        try: 
            fetched_tweets = self.api.search(q = query, count = count) 

            for tweet in fetched_tweets: 
                parsed_tweet = {} 

                parsed_tweet['text'] = tweet.text 
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(TextBlob(self.clean_tweet(tweet.text)).sentiment.polarity ) 

                if tweet.retweet_count > 0: 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 

            return tweets 

        except tweepy.TweepError as e: 
            print("Error : " + str(e)) 
            
# DO NOT EDIT THIS CODE            
    def get_public_views_on_platform(self,query):
        result = GamingPlatform(query)
        negative_tweets_percentage = 0
        positive_tweets_percentage = 0

        tweets = self.get_tweets(query,25)

        positive_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
        negative_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
        

        if (len(positive_tweets) != 0): #to protect from zero division
            positive_tweets_percentage = 100*len(positive_tweets)/len(tweets)
        
        if (len(negative_tweets) != 0):
            negative_tweets_percentage = (len(tweets) - len(negative_tweets) - len(positive_tweets))/len(tweets)

        result.positiveView = positive_tweets_percentage
        result.negativeView = negative_tweets_percentage
        return result

# DO NOT EDIT THIS CODE
    def get_positive_views(self, name):
        return self.get_public_views_on_platform(name).positiveView

# DO NOT EDIT THIS CODE
    def get_negative_views(self, name):
        return self.get_public_views_on_platform(name).negativeView
  
    # DO NOT EDIT THIS CODE
    def update_status(self,message):
        self.api.update_status(message);
        #need emergency function
        
        
