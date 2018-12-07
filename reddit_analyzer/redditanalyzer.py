"""
This file analyzes and graphs the data from redditsentimentscore.py file

Will also use matplotlib for graphs as the standard pandas/numpy package.
"""

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Specify path to save graphs to
path = './reddit_analyzer/static/graphs/'

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

def extract_time_info(df):
    """
    Splits date info into multiple columns for futher analysis
    """
    df['created_utc'] = pd.to_datetime(df['created_utc'])
    df['date'] = df['created_utc'].dt.date
    df['day'] = df['created_utc'].dt.day_name()
    df['month'] = df['created_utc'].dt.month_name()
    df['time'] = df['created_utc'].dt.time
    df['hour'] = df['created_utc'].dt.hour

    df["day"] = pd.Categorical(df["day"], categories=['Sunday', 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'], ordered=True)
    df["month"] = pd.Categorical(df["month"], categories=['January', 'February', 'March', 'April' ,'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)

def graph_scatterplots(df):
    """
    Creates and saves relevant scatterplots.
    """
    fig, ax1 = plt.subplots()
    ax1.scatter(df['score'], df['num_comments'])
    ax1.set_title('Score vs Number of Comments')
    fig.savefig(path + 'scatterplot_score_vs_number.png', bbox_inches='tight', format='png')

    fig, ax1 = plt.subplots()
    ax1.scatter(df['score'], df['compound'])
    ax1.set_title('Score vs Compound Sentiment Score')
    fig.savefig(path + 'scatterplot_score_vs_compound.png', bbox_inches='tight', format='png')

    fig, ax1 = plt.subplots()
    ax1.scatter(df['score'], df['neg'])
    ax1.set_title('Score vs Negative Sentiment Score')
    fig.savefig(path + 'scatterplot_score_vs_negative.png', bbox_inches='tight', format='png')

    fig, ax1 = plt.subplots()
    ax1.scatter(df['score'], df['neu'])
    ax1.set_title('Score vs Neutral Sentiment Score')
    fig.savefig(path + 'scatterplot_score_vs_neutral.png', bbox_inches='tight', format='png')

    fig, ax1 = plt.subplots()
    ax1.scatter(df['score'], df['pos'])
    ax1.set_title('Score vs Positive Sentiment Score')
    fig.savefig(path + 'scatterplot_score_vs_positive.png', bbox_inches='tight', format='png')

def graph_lines(df):
    """
    Create and save relevant barcharts
    """
    df2 = df.sort_values(by=['score'], ascending=False)
    
    fig, ax1 = plt.subplots()
    x = np.arange(1, len(df.index) + 1)
    ax1.plot(x, df2['score'])
    fig.savefig(path + 'line_score_desc.png', bbox_inches='tight', format='png')

    df2 = df.sort_values(by=['num_comments'], ascending=False)
    
    fig, ax1 = plt.subplots()
    x = np.arange(1, len(df.index) + 1)
    ax1.plot(x, df2['num_comments'])
    fig.savefig(path + 'line_num_comments_desc.png', bbox_inches='tight', format='png')



def graph_histograms(df):
    """
    Create and saves histograms
    """

    fig, ax = plt.subplots()
    ax.hist(df['score'])
    fig.savefig(path + 'histogram_score.png', bbox_inches='tight', format='png')

    fig, ax = plt.subplots()
    ax.hist(df['num_comments'])
    fig.savefig(path + 'histogram_num_comments.png', bbox_inches='tight', format='png')

def graph_wordcloud(df):
    """
    Creates and saves a wordcloud of all the titles in the dataframe.
    """
    # Generate stopwords
    stopwords = set(STOPWORDS)
    # Add additional stopwords
    # stopwords.update([""])
    
    text = "".join(title for title in df.title)
    fig, ax1 = plt.subplots()
    wordcloud = WordCloud(stopwords=stopwords, max_words=100, background_color="white").generate(text)

    ax1.imshow(wordcloud, interpolation='bilinear')
    ax1.axis("off")
    fig.savefig(path + 'wordcloud.png', bbox_inches='tight', format='png')

def graph_heatmaps(df):
    """
    Generates heatmaps based on time, day, and month
    """
    # Pivot data
    # df2 = df.pivot("day", "time", "score")

    heat_day_hour = df.pivot_table(values="score", index=["day"], columns=["hour"], aggfunc=np.mean)
    fig, ax = plt.subplots()
    ax = sns.heatmap(heat_day_hour ,cmap="YlGnBu")
    fig.savefig(path + 'heatmap_day_hour.png', bbox_inches='tight', format='png')

    # heat_month = df.pivot_table(values="score", index=["month"], columns=["hour"], aggfunc=np.mean)
    # fig, ax = plt.subplots()
    # ax = sns.heatmap(heat_day_hour ,cmap="YlGnBu")
    # fig.savefig('./graphs/heatmap_day_hour.png', bbox_inches='tight'))

def generate_title():
    pass

def generate_comment():
    pass

def compare_two_subreddits():
    pass

def create_graphs(data):
    """
    Creates graphs based on reddit data.
    """
    df = pd.read_csv(data)
    extract_time_info(df)
    graph_scatterplots(df)
    graph_wordcloud(df)
    graph_heatmaps(df)
    graph_lines(df)
    graph_histograms(df)

def main():
    # df = pd.read_csv('politics2.csv')
    # extract_time_info(df)
    # graph_scatterplots(df)
    # graph_wordcloud(df)
    # graph_heatmaps(df)
    # graph_lines(df)
    # graph_histograms(df)
    # save_file(df, "politics3.csv")
    pass

if __name__ == '__main__':
    main()