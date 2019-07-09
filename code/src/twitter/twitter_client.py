import requests
import requests_oauthlib
import sys
import json

def init_auth(file):
    (CONSUMER_KEY,CONSUMER_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET) = open(file, 'r').read().splitlines()
    auth_obj = requests_oauthlib.OAuth1(CONSUMER_KEY, CONSUMER_SECRET,
                                        OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    if verify_credentials(auth_obj):
        print('Validated credentials OK')
        return auth_obj
    else:
        print('Credentials validation failed')
        sys.exit(1)

def verify_credentials(auth_obj):
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    response = requests.get(url, auth=auth_obj)
    return response.status_code == 200

def get_mentions(since_id, auth_obj):
    params = {'count': 200, 'since_id': since_id, 'include_rts': 0, 'include_entities': 'false'}
    url = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json'
    response = requests.get(url, params=params, auth=auth_obj)
    #Checking if the request is successful.
    #It will raise an HTTPError if the request returned an unsuccessful status code.
    response.raise_for_status()
    return json.loads(response.text)

def search(auth_obj):
    params = {'q': 'python'}
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    response = requests.get(url, params=params, auth=auth_obj)
    return response

if __name__ == '__main__':
    auth_obj = init_auth('credentials.txt')

    # Get mentions
    # since_id = 1
    # for tweet in get_mentions(since_id, auth_obj):
        # print(tweet['text'])

    # Search tweets
    response = search(auth_obj)
    print (json.dumps(response.json(),indent = 2))