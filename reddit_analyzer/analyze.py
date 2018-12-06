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

@bp.route('/handle_data', methods=['POST'])
def handle_data():
    # projectpath = request.form['projectFilepath']
    subreddit = request.form.get('subreddit')
    sort = request.form.get('sort')
    time_period = request.form.get('time_period')
    limit = request.form.get('lmit')
    # print(subreddit, sort, time_period, limit)

    # Redditpraw
    data = rp.scrape_subreddits(subreddit, sort=sort, time_period=time_period, limit=limit)
    rp.save_file(data, "reddit.csv")

    # Redditsentiment
    rs.analyze_submissions("reddit.csv", "reddit.csv")

    # Redditanalyzer
    ra.create_graphs("reddit.csv")

    return redirect('/analysis')

@bp.route('/analysis')
def show_analysis():
    """
    Show page of analysis
    """
    return render_template('analysis/analysis.html')