# Imports
import facebook
import requests
# Secret Access Token
access_token = 'EAANmZARlE02EBAA6ZBV6H5BgNAbyaxE9kTv6fgZAV5vYsXLg7ZAXQYyQHUx1JNAUTjELSnWFDfF48QlGI7teNfyGDyh7XhyEJcTFbhYccdAO6jTX66mOwuTtZCBOKtmzybcoBOVakuvq3qhMzK0TXrX9XP2Bk3ZBokQIEDuIN0QZAuL2cwK2TnoirHsZB0ltABb3nxU1Bs1ZBlCYoMvjIm7YdZAjv8k7ZCKepByRoyUrF3kW4zgdL3A4m5G'

# Define graph
graph = facebook.GraphAPI(access_token="your_token", version="2.12")

# Events


def get_events():
    events = graph.request('/search?q=Poetry&type=event&limit=10000')
    return events

# Posts


def get_friends():
    # Get the active user's friends.
    friends = graph.get_connections(id='me', connection_name='friends')
    return friends


def put_post(msg):
    # Your Access Keys
    page_id_1 = 123456789
    post_url = 'https://graph.facebook.com/{}/feed'.format(page_id_1)
    payload = {
        'message': msg,
        'access_token': access_token
    }
    r = requests.post(post_url, data=payload)
    print('posting ', r.text)
