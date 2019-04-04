from twitterApi import TwitterAPI, GamingPlatform


class Advertisment(object):

    def __init__(self,api):
        self.api = TwitterAPI()

    #   ------------- PROBLEM 2 -------------
    # Given a list of Platform Objects, 
    # Populate their negativeView and positiveView properties,
    # then return the list of Platform Objects.
    def get_platform_views(self,listOfPlatforms):
        
        # todo: get view data for each platform         
            
        return listOfPlatforms
 
 
    #   ------------- PROBLEM 3 -------------   
    # Given a list of Platform Objects
    # Return Platform Object with the GREATEST Positive View Value
    def get_top_platform(self,platformsWithData):
        result = GamingPlatform("place holder")
                
        # todo: get top platform, then return       
        
        return result


    #   ------------- PROBLEM 4 -------------  
    # Given a string to tweet
    # Post a tweet using the string as content
    # return nothing 
    
    #todo: create function
        
    
    
    
    #   -------------  BONUS   -------------  
    # Given a list of Platform Objects
    # Sort the Platform Objects based on their Positive View Value
    # return this newly sorted list
    def sort_platforms(self, listOfPlatforms):
        result = []
        
        # todo: sort platforms   
        
        return result


