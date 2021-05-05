
import tweepy

auth = tweepy.OAuthHandler("API_KEY", "API_SECRET")

auth.secure = True
auth_url = auth.get_authorization_url()

print(f'Use this url to authorize: ' + auth_url)

verifier = input('PIN: ').strip()

auth.get_access_token(verifier)
	
print(f"ACCESS_KEY = '%s'" % auth.access_token)
print(f"ACCESS_SECRET = '%s'" % auth.access_token_secret)
