from twitterApi import TwitterAPI, GamingPlatform
from ScoutsActivity import Advertisment
import sys

# Helper Function
def printOutPlatforms(listOfPlatforms):
    for item in listOfPlatforms:
        print("{: ^15} | Positive Views: {: ^3} | Negative Views: {: ^3}".format
         (item.name, item.positiveView,item.negativeView))
    print("") 

# Notify user that code is running
print("Python Code Started!!\n")



    #   ------------- PROBLEM 1 -------------  

# Create Twitter API Object
twitterApi = TwitterAPI()

# Call get_tweet_setiment with multiple values
positiveTest1 = twitterApi.get_tweet_sentiment(3)
positiveTest2 = twitterApi.get_tweet_sentiment(33)

negativeTest1 = twitterApi.get_tweet_sentiment(-1)
negativeTest2 = twitterApi.get_tweet_sentiment(-11)

neutralTest = twitterApi.get_tweet_sentiment(0)

# Test results
if(positiveTest1 == 'positive' and 
   positiveTest2 == 'positive' and
   negativeTest1 == 'negative' and
   negativeTest2 == 'negative' and
   neutralTest   == 'neutral'):
    print("get_tweet_sentiment() function is correct!\n")
else:
    print("get_tweet_sentiment() function has failed!\n")
    sys.exit()



# Create Advertisement Object (give it twitter API)
advertisment = Advertisment(twitterApi)

# Create List of Platforms
listOfPlatforms = [
                    GamingPlatform("xbox"),
                    GamingPlatform("playstation"),
                    GamingPlatform("nintendo switch"),
                    GamingPlatform("PC"), 
                    GamingPlatform("iPhone"),
                    GamingPlatform("android")
                    ]



    #   ------------- PROBLEM 2 -------------  

# Get views for each platform
platformsWithViews = advertisment.get_platform_views(listOfPlatforms)

# check your output
if(len(platformsWithViews) != len(listOfPlatforms) ):
    print("Error! We were returned %d platforms by GetPlatformViews()!\n" % len(platformsWithViews))
    sys.exit()
    
# Print result
print("\nResults from GetPlatformViews(): ")
printOutPlatforms(platformsWithViews)



    #   ------------- PROBLEM 3 -------------  

# Get platform with highest positive view
topPlatform = advertisment.get_top_platform(platformsWithViews)

# print result
print("Result from GetTopPlatform(): ")
print("{: ^15} | Positive Views: {: ^3} | Negative Views: {: ^3}".format
(topPlatform.name, topPlatform.positiveView,topPlatform.negativeView))
print("")



    #   ------------- PROBLEM 4 -------------  


# todo: use created function





    #   -------------  BONUS   -------------  

# Sort Gaming Platforms by Positive Views
sortedPlatforms = advertisment.sort_platforms(platformsWithViews) 

# check result
if(len(sortedPlatforms) != 0):
    print("Results from SortPlatforms")
    printOutPlatforms(sortedPlatforms)
    
# https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
