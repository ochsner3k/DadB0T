import tweepy as tt
import time


#login credentials twitter account
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

#login
auth = tt.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tt.API(auth)

user = api.me()
print(user.name)


#actual stuff below 

    #time.sleep(900) = every 15 minutes

   
