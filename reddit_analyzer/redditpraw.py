"""
    This file captures data from reddit using praw and save the output as a csv file

    For this version, we only get a maximum of 1,000 instances, as Reddit only lets us get 1,000 at a time. 
    This should be sufficient for our level of analysis.
"""

import praw
import pandas as pd
# from reddit_analyzer import config
from dotenv import load_dotenv
load_dotenv()

import os

# print(os.getenv('client_id'))
# print(os.getenv('client_secret'))
# print(os.getenv('username'))
# print(os.getenv('password'))
# print(os.getenv('user_agent'))

# reddit = praw.Reddit(client_id=config.client_id,
#                      client_secret=config.client_secret,
#                      username=config.username,
#                      password=config.password,
#                      user_agent=config.user_agent)

reddit = praw.Reddit(client_id=os.getenv('client_id'),
                     client_secret=os.getenv('client_secret'),
                     username=os.getenv('reddit_username'),
                     password=os.getenv('reddit_password'),
                     user_agent=os.getenv('user_agent'))

def save_file(data, filename):
    """
    Save an array of data as a csv file.

    :param data: data is a pandas df object

    :param filename: the string to use as the filename when saving as csv
    """
    data.to_csv(filename, index=False)

def scrape_subreddits(subreddit, sort='top', time_period='all', limit=None):
    """
    Collects data on submissions in a subreddit.

    :param sort: the sorting mechanism to scrape (E.g. top, best, new, old, controversial)
    
    :param time_period: the time period to scrape (E.g. day, week, month)

    :param limit: the maximum number of submission to scrape. 1,000 is the maximum.
    """
    sub = subreddit

    sort_by = {
        'gilded': reddit.subreddit(sub).gilded(limit=limit),
        'hot': reddit.subreddit(sub).hot(limit=limit),
        'new': reddit.subreddit(sub).new(limit=limit),
        'controversial': reddit.subreddit(sub).controversial(time_period, limit=limit),
        'top': reddit.subreddit(sub).top(time_period, limit=limit),
        'rising':  reddit.subreddit(sub).rising(limit=limit)
    }

    submissions = sort_by.get(sort)

    data = {
        'title': [],
        'subreddit': [],
        'score': [],
        'id': [],
        'url': [],
        'num_comments': [],
        'created_utc': [],
        'selftext': [],
        'over_18': []
    }
    
    for submission in submissions:
        if 'Megathread' not in submission.title:
            data['title'].append(submission.title)
            data['subreddit'].append(submission.subreddit)
            data['score'].append(submission.score)
            data['id'].append(submission.id)
            data['url'].append(submission.url)
            data['num_comments'].append(submission.num_comments)
            data['created_utc'].append(submission.created_utc)
            data['selftext'].append(submission.selftext)
            data['over_18'].append(submission.over_18)
        
    df = pd.DataFrame(data)

    return df

def scrape_submission(url):
    """
    Collects data on comments in a submission.
    """
    # Only implement if have spare time
    pass

def scrape_users():
    """
    Collects data of a user based on parameters.
    """
    # Only implement if have spare time
    pass

def main():
    """
    Only used for testing.
    """
    # sub = 'askreddit'
    # submissions = reddit.subreddit(sub).top('all', limit=500)
    # comments = reddit.subreddit(sub).comments(limit=25)
    # print([(comment.body) for comment in comments])
    # top5 = [(submission.title, submission.selftext, submission.id, submission.num_comments) for submission in submissions]
    # print(top5[0])
    # data = scrape_subreddits('politics', sort='hot', time_period='all', limit=1000)
    save_file(data, "politics.csv")

if __name__ == '__main__':
    main()