from twitterApi import TwitterAPI, GamingPlatform

class Tweet(object):
    def __init__(self):
        self.firstLIne = ""
        self.LastLIne = 0
        self.something = 0

class Advertisment(object):

    def __init__(self,api):
        self.api = TwitterAPI()


    # Given a list of Platform Objects, 
    # Populate their negativeView and positiveView properties,
    # then return the list of Platform Objects.
    def get_platform_views(self,listOfPlatforms):
        
        # todo: get view data for each platform
        for platform in listOfPlatforms:          
            platform.positiveView = self.api.get_positive_views(platform.name)
            platform.negativeView = self.api.get_negative_views(platform.name)   
            
            
        return listOfPlatforms
 
 
   
    # Given a list of Platform Objects
    # Return Platform Object with the GREATEST Positive View Value
    def get_top_platform(self,platformsWithData):
        result = GamingPlatform("place holder")
                
        # todo: get top platform, then return    
        for platform in platformsWithData:
            if(platform.positiveView > result.positiveView):
                    result = platform
        
        
        return result


    # --BONUS--
    # Given a list of Platform Objects
    # Sort the Platform Objects based on their Positive View Value
    # return this newly sorted list
    def sort_platforms(self, listOfPlatforms):
        result = []
        
        # todo: sort platforms
        while(len(listOfPlatforms) > 0):
            top = self.get_top_platform(listOfPlatforms)
            result.append(top)
            listOfPlatforms.remove(top)
        
        
        return result

    # Given a string to tweet
    # Post a tweet using the string as content
    # return nothing 
    
    #todo: create function
    def tweet_message(self, message):
        self.api.update_status("This is our very first tweet!")
        
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^