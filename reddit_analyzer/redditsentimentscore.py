"""
This file analyzes a dataframe as outputted by the redditpraw.py script.

This file will parse and analyze the text using sentiment analysis.
"""

from reddit_analyzer import redditpraw
import pandas as pd
import numpy as np
import datetime as dt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

def save_file(data, filename):
    """
    Save an array of data as a csv file.

    :param data: data is a pandas df object

    :param filename: the string to use as the filename when saving as csv
    """
    data.to_csv(filename, index=False)

def load_data(filename):
    """
    Load a .csv file
    """
    return pd.read_csv(filename)

def convert_created(df):
    """
    Convert create_utc to readable format
    """
    def get_date(created_utc):
        return dt.datetime.fromtimestamp(created_utc)

    df['created_utc'] = df['created_utc'].apply(get_date)

def nltk_sentiment(text):
    """
    Does sentiment analysis on a string of text and return the polarity scores of the result.
    
    pol_scores is an array with pos, neg, neu, and composite scores.
    """
    pol_score = SIA().polarity_scores(text)
    return pol_score

def append_nltk_sentiment(df):
    """
    Appends sentiment scores to the reddit data.
    """
    scores = []
    for title in df['title']:
        scores.append(nltk_sentiment(title))
    df2 = pd.DataFrame(scores)
    df = pd.concat([df, df2], axis=1)
    return df

def analyze_comments():
    pass

def append_comment_scores():
    pass

def analyze_submissions(data, save_file_name):
    """
    Analyzes reddit data from submissions.
    """
    df = pd.read_csv(data)
    convert_created(df)
    df = append_nltk_sentiment(df)
    save_file(df, save_file_name)

def main():
    """
    Only used for testing.
    """
    df = pd.read_csv('politics.csv')
    convert_created(df)
    df = append_nltk_sentiment(df)
    save_file(df, "politics2.csv")

if __name__ == '__main__':
    main()