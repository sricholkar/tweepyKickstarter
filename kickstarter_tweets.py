import tweepy

""" prints out the tweets not older than one weeek """

#called function
def retrieveTweets(campaign):
    
    #Authentication
    auth = tweepy.OAuthHandler("TaVqgT6AMTsPLGxxGUdWFC8Yb", "nZICD5ASyXhRWAKeP4eUyWPC6UcvlSzjb7Yta2j1rrJHaFS5je")
    auth.set_access_token("886253580600082432-knZhyGJ6oSKQ3ULUEKK4ZbJatflWZvq","HjZLn3Mv9kVwiamW4ZhqgZzacjsI9xMI6yG8jjpL14Mrd")
    api = tweepy.API(auth)
    
    #Retrieve Tweets
    for page in tweepy.Cursor(api.search, q=campaign, monitor_rate_limit=True, 
                              wait_on_rate_limit=True, lang="en").pages(30): #page variable contains json data
        for tweet in page:
            if (not tweet.retweeted) and ('RT @' not in tweet.text):
                print(tweet.text + " " + str(tweet.created_at) +"\n\n")


#calling function           
retrieveTweets("@coolest_cooler")