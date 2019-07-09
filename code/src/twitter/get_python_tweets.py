import twitter 
 
def get_info_twitter(tw):
    if tw is not None:
        query = tw.search.tweets(q="#python", lang="en", count="10")["statuses"]
        for q in query:
            for key,value in q.items():
                if(key=='text'):
                    print(value+'\n')

def main():
    try:
        tw = twitter_connection("credentials.txt")
        get_info_twitter(tw)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()