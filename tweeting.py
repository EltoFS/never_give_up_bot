import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("API_KEY", "API_SECRET")
auth.set_access_token("AUTH_KEY", "AUTH_SECRET")

# Negative filters (I don't want those words on the tweet)
negative_filter = ["not giving", "giveaway", "GIVEAWAY", "giving away", 
                   "election", "Election", "never giving", "never give", 
                   "giving you", "giving it", "giving this"]

# Positive filters
positive_filter = ["I'm giving up", "i'm giving up", "im giving up", "Im giving up"]
negative = False
positive = []
api = tweepy.API(auth)
media = api.media_upload(filename="nevergiveup.mp4", chunked=True)

for tweet in api.search(q="i'm giving up", count=10):
    for i in negative_filter:
        if i not in tweet.text and negative is False:
            negative = False
        else:
            negative = True

    for i in positive_filter:
        if i in tweet.text:
                positive.append(True)
    if True in positive and negative is False:
        api.update_status(status='', in_reply_to_status_id=tweet.id, 
                          media_ids=[media.media_id],
                          auto_populate_reply_metadata=True)
        print(f"{tweet.user.name}:{tweet.id}:{tweet.text}")
    
    negative = False
    positive = True
    positive = []
