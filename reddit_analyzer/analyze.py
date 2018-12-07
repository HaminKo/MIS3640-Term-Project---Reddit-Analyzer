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

@bp.route('/download_data', methods=['POST'])
def download_data():
    """
    Route for downloading data from reddit.
    """
    subreddit = request.form.get('subreddit')
    sort = request.form.get('sort')
    time_period = request.form.get('time_period')
    limit = request.form.get('lmit')
    # print(subreddit, sort, time_period, limit)

    # Redditpraw
    print('Downloading data from reddit.')
    data = rp.scrape_subreddits(subreddit, sort=sort, time_period=time_period, limit=limit)
    rp.save_file(data, "reddit.csv")
    print('Done downloading data from reddit')
    return redirect('/analyze_data', code=307)

@bp.route('/analyze_data', methods=['GET', 'POST'])
def analyze_data():
    """
    Route for analyzing data from reddit.
    """
    # Redditsentiment
    print('Analyzing data from reddit.')
    rs.analyze_submissions("reddit.csv", "reddit.csv")
    print('Done analyzing data from reddit.')
    return redirect('graph_data', code=307)

@bp.route('/graph_data', methods=['GET', 'POST'])
def graph_data():
    """
    Route for graphing data from reddit.
    """
    # Redditanalyzer
    print('Graphing data from reddit.')
    ra.create_graphs("reddit.csv")
    print('Done graphin data from reddit.')
    return redirect('/analysis')

@bp.route('/analysis')
def show_analysis():
    """
    Render analysis page.
    """
    return render_template('analysis/analysis.html')