from twitterApi import TwitterAPI, GamingPlatform
from ScoutsActivity import Advertisment

# Helper Function
def printOutPlatforms(listOfPlatforms):
    for item in listOfPlatforms:
        print("{: ^15} | Positive Views: {: ^3} | Negative Views: {: ^3}".format
         (item.name, item.positiveView,item.negativeView))
    print("") 


# Create Twitter API Object
twitterApi = TwitterAPI()

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



# PROBLEM 1

# Get views for each platform
platformsWithViews = advertisment.get_platform_views(listOfPlatforms)

# check your output
if(len(platformsWithViews) != len(listOfPlatforms) ):
    print("Error! We were returned %d platforms by GetPlatformViews()!\n" % len(platforms_with_views))
    
    
# Print result
print("\nResults from GetPlatformViews(): ")
printOutPlatforms(platformsWithViews)



# PROBLEM 2

# Get platform with highest positive view
topPlatform = advertisment.get_top_platform(platformsWithViews)

# print result
print("Result from GetTopPlatform(): ")
print("{: ^15} | Positive Views: {: ^3} | Negative Views: {: ^3}".format
(topPlatform.name, topPlatform.positiveView,topPlatform.negativeView))
print("")



# BONUS BONUS BONUS

# Sort Gaming Platforms by Positive Views
sortedPlatforms = advertisment.sort_platforms(platformsWithViews) 

# check result
if(len(sortedPlatforms) != 0):
    print("Results from SortPlatforms")
    printOutPlatforms(sortedPlatforms)
        


# PROBLEM 3

# todo: use created function
advertisment.tweet_message("This is our first ever test of python tweeting!")


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^