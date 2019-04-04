from twitterApi import TwitterAPI, GamingPlatform
from typing import List

class Tweet(object):
        def __init__(self):
            self.firstLIne = ""
            self.LastLIne = 0
            self.something = 0

class Advertisment(object):

    def __init__(self,api):
        self.api = TwitterAPI()

    def GetTopPlatforms(self,listOfPlatforms : List[GamingPlatform]):
        # get the positive/neg/ and neutral for each tweet
        # order them by highest -> lowest positive
        # have them sort this out into two functions?
        topPlatforms = []
        for platform in listOfPlatforms:
            platform_with_data = self.api.get_public_views_on_platform(platform)
            topPlatforms.append(platform)
        return topPlatforms
    
    def SendTweet(self,tweet: Tweet):
        print("Entered sendTweet") 
        # need to have the students put their 'signature' at the end

#I'm going to need to do checks so that they do not overload twitter and get us blocked    

adv = Advertisment( TwitterAPI() )
listOfPlatforms = [
                    GamingPlatform("xbox"),
                    GamingPlatform("playstation"),
                    GamingPlatform("nintendo switch"),
                    GamingPlatform("PC"), # gaming computer
                    GamingPlatform("iPhone"),
                    GamingPlatform("android")
                    ]
topPlatforms = adv.GetTopPlatforms(listOfPlatforms)
print(topPlatforms[0].positiveView)

# Lesson goals:
#       - understand the what an object is, and how to use it
#       - undestand functions
#       - understand how to devise their own sorting algorithm
#       - understand what APIs are, and how they can be used
# objects, functions, lists, loops



# next, go through your list, get all values
# check all the values, get top 3 result
# tweet at the end with your name maybe?
# we can also follow people, or unfollow people.
