from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from reddit_analyzer import redditpraw as rp
from reddit_analyzer import redditsentimentscore as rs
from reddit_analyzer import redditanalyzer as ra

bp = Blueprint('analyze', __name__)

@bp.route('/')
def index():
    """
    Main page of project
    """
    return render_template('analysis/index.html')

# @bp.route('/download_data', methods=['POST'])
# def download_data():
#     # projectpath = request.form['projectFilepath']
#     subreddit = request.form.get('subreddit')
#     sort = request.form.get('sort')
#     time_period = request.form.get('time_period')
#     limit = request.form.get('lmit')
#     # print(subreddit, sort, time_period, limit)

#     print('time 1')
#     # Redditpraw
#     data = rp.scrape_subreddits(subreddit, sort=sort, time_period=time_period, limit=limit)
#     rp.save_file(data, "reddit.csv")

#     print('time 2')
#     # Redditsentiment
#     rs.analyze_submissions("reddit.csv", "reddit.csv")

#     print('time 3')
#     # Redditanalyzer
#     ra.create_graphs("reddit.csv")
#     print('time 4')

#     return redirect('/analysis')

@bp.route('/download_data', methods=['POST'])
def download_data():
    # projectpath = request.form['projectFilepath']
    subreddit = request.form.get('subreddit')
    sort = request.form.get('sort')
    time_period = request.form.get('time_period')
    limit = request.form.get('lmit')
    # print(subreddit, sort, time_period, limit)

    print('time 1')
    # Redditpraw
    data = rp.scrape_subreddits(subreddit, sort=sort, time_period=time_period, limit=limit)
    rp.save_file(data, "reddit.csv")
    print('time 2')
    return redirect('/analyze_data', code=307)

@bp.route('/analyze_data', methods=['GET', 'POST'])
def analyze_data():
    # Redditsentiment
    rs.analyze_submissions("reddit.csv", "reddit.csv")
    print('time 3')
    return redirect('graph_data', code=307)

@bp.route('/graph_data', methods=['GET', 'POST'])
def graph_data():
    print('time 3')
    # Redditanalyzer
    ra.create_graphs("reddit.csv")
    print('time 4')
    return redirect('/analysis')

@bp.route('/analysis')
def show_analysis():
    """
    Show page of analysis
    """
    return render_template('analysis/analysis.html')