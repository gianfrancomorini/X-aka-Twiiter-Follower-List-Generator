import tweepy

def get_formatted_following_list(api_key, api_secret, access_token, access_token_secret, account_name):
    # Authenticate with Twitter using OAuth 1.0a
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Get the list of friends (accounts the user is following)
    following = []
    try:
        for friend in tweepy.Cursor(api.get_friends, screen_name=account_name).items():
            following.append(friend.screen_name)

        # Format the list as requested
        formatted_list = ", ".join(f"'{name}'" for name in following)
        return formatted_list

    except tweepy.TweepError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
account_name = 'techversetrends'

formatted_following = get_formatted_following_list(api_key, api_secret, access_token, access_token_secret, account_name)
if formatted_following:
    print(formatted_following)