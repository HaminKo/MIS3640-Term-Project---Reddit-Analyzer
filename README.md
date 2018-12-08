# MIS3640-Term-Project---Reddit-Analyzer
MIS3640 Term Project

demo site:
https://reddit-analyzer-api-heroku.herokuapp.com/analysis

## Table of Contents

- [Dependencies](#Dependencies)
- [Installation Guide](#Installation)
- [Setup Instructions](#Setup)
- [Application Instructions](#Application)
- [Heroku Setup Guide](#Heroku)

## <a name="Dependencies">Installation Guide</a>

### Dependencies
Make sure to install the following:

For the app itself:

- flask
- flask_bootstrap 
- dotenv
- praw
- pandas
- numpy
- nltk
- sentiment.vader from nltk
- matplotlib
- seaborn
- wordcloud

For heroku:

- gunicorn

## <a name="Installation">Instructions</a>

### Set the following environment variables:

```
client_id='example'
client_secret='example'
reddit_username='example'
reddit_password='example'
user_agent='example'
```

### To Run the application locally:
Make sure you are in the main folder:

```
Linuxs/mac:
export FLASK_APP=reddit_analyzer
export FLASK_ENV=development
flask run

Windows cmd:
set FLASK_APP=reddit_analyzer
set FLASK_ENV=development
flask run

Windows powershell:
$env:FLASK_APP = "reddit_analyzer"
$env:FLASK_ENV = "development"
flask run
```

## <a name="Application">Application instructions</a>

Once you have the application up and running, you can start analyzing subreddits.

On the main page, you can set up several search parameters for gathering data from reddit.

![](images/Main_page_2.png)

Once you click submit, the application will scrape, analyze, and create graphs of the subreddit. This process takes around 30 seconds to 1 minute.

After the analysis is complete, you will be redirected to the page with the analysis. Here is a sample output:

![](images/analysis_heatmap.png)
![](images/analysis_wordmap.png)
![](images/analysis_scatterplot.png)

You can also click on the analysis tab at the top in order to see a sample output for a dataset that is already included.

### Project Demo

## <a name="Heroku">Deploying on Heroku</a>

Make sure you have heroku installed in your CLI.

Create the heroku app using

```
heroku create
```

You can create requirements.txt using

```
pip freeze > requirements.txt
```

This allows Heroku to know what packages to install when running your application.
