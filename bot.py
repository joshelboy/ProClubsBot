import tweepy

# Authenticate to Twitter

#übergangslösung
from datascraper import currentPoints

#Kann ich hier nicht reinschreiben, weil sonst jmd den Token benutzen könnte
consumerKey = ""
consumerKeySecret = ""

accessToken = ""
accessTokenSecret = ""


auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)

#wichtig, um die Tweepy Methoden nutzen zu können
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

api.update_status("Service Tweet vom Bot." + "Aktuelle Punktzahl:" + currentPoints)
