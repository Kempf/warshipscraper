import auth
import pandas as pd
import datetime as dt
import praw
from psaw import PushshiftAPI

# search func
def getsubs (ssubreddit, slimit=1000, start_epoch=int(dt.datetime.now().timestamp())):
    return list(papi.search_submissions(sort='desc',
                            before=start_epoch,
                            subreddit=ssubreddit,
                            filter=['url','author', 'title', 'score', 'upvote_ratio', 'created_utc', 'num_comments','selftext'],
                            limit=slimit))


# auth - fill in auth.py file
reddit = praw.Reddit(client_id=auth.REDDIT_AUTH['client_id'],
                     client_secret=auth.REDDIT_AUTH['client_secret'],
                     password=auth.REDDIT_AUTH['password'],
                     user_agent=auth.REDDIT_AUTH['user_agent'],
                     username=auth.REDDIT_AUTH['username'])
                     
if reddit.user.me() == auth.REDDIT_AUTH['username']:
    print('Logged in as u/'+auth.REDDIT_AUTH['username'])
    
papi = PushshiftAPI(reddit)

topics_dict = { "id":[], \
                "title":[], \
                "score":[], \
                "upvote_ratio":[],\
                "comms": [], \
                "created_utc": [], \
                "url":[]}

# How many submissions to grab (this takes a few hours at 10000)
num = 1000
scrap = getsubs('warshipporn',num,1330388290)

# what data to collect
for submission in scrap:
    print("%5d\r"%num,end="")
    num = num-1
    if(submission.selftext == ""):
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms"].append(submission.num_comments)
        topics_dict["created_utc"].append(submission.created_utc)
        topics_dict["upvote_ratio"].append(submission.upvote_ratio)

print('')

topics_data = pd.DataFrame(topics_dict)

print('Scraped '+str(len(scrap))+' submissions')
print('Saved '+str(len(topics_data))+' submissions')        

# save data
topics_data.to_csv('data.csv')