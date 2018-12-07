# Text Mining Project

### MIS3640 - Problem Solving & Software Design

## Table of Contents:

- [Project Overview](#Overview)
- [Implementation](#Implementation)
- [Results](#Results)
- [Reflection](#Reflection)

## Packages Used:

- [config](https://pypi.org/project/config/)
- [matplotlib](https://matplotlib.org/)
- [nltk](https://www.nltk.org/)
- [numpy](http://www.numpy.org/)
- [pickle](https://docs.python.org/3/library/pickle.html)
- [praw](https://praw.readthedocs.io/en/latest/)

## <a name="Project">Project Overview:</a>

The goal of this project was to analyze the change in sentiment of Reddit's Bitcoin Daily Discussion Threads throughout the months of December 2017, January 2018, and February 2018. These three months were when Bitcoin drastically increased and decreased in value, so I was expecting to see a strong correlation between sentiment and price. In order to test this theory I decided to gather the top 100 comments on every Daily Discussion thread and run them through a sentiment analysis, ultimately plotting the results on bar charts.

## <a name="Implementation">Implementation:</a>

I broke up this project into three files that each served their own purpose. The first file, reddit_miner.py, was used to pull data from reddit and store it using pickle. The difficult part was pulling the correct submissions from Reddit's Bitcoin subreddit. However, using praw's search feature I was able to search for 'Daily Discussion, December' to pull all of the December discussions, and so on for each month.

With a list of submission objects stored using pickle I then created a file, reddit_analyzer.py, which was used to reformat the submission data and run a sentiment analysis. First, I filtered out a few irrelevant submissions and then converted the list to a dictionary for each month that included a key for each day of the month and a value of the associated submission for that day. With these dictionaries, I was then able to analyze all of the comments for each Daily Discussion using nltk and average their sentiment scores. This process ran for a few minutes, but once finished I stored the data using pickle once again.

In the final file, reddit_displayer.py, I took the sentiment scores for each day and visualized them on bar charts for each month. Building the charts was made easy by matplotlib, but I had to make 12 total, positive, negative, neutral, and compound for each month.

## <a name="Results">Results:</a>

### Positive Sentiment

In the following charts, one can see that the positive sentiment for Bitcoin was relatively stable. However, we can see a slight peak right from the end of December to the beginning of January. This time period was when Bitcoin reached its peak price as well. Also, we can see a low point at the end of January, followed by a steady increase throughout the month of February. This tells us that there was less positive sentiment when Bitcoin's price dropped quickly, but confidence returned afterwards.

![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/December_pos.png)
![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/January_pos.png)
![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/February_pos.png)

### Negative Sentiment

In the negative charts, we can see a huge valley during Bitcoin's peak at the end of December. This tells us that barely anyone had anything bad to say about Bitcoin during its peak. However, one other interesting thing to note here is that there seems to be a cycle pattern where there is more negative sentiment every week or so. With a quick calendar check, most of these peaks of bad sentiment line up with weekends, probably because people have more time to post on Reddit when they're not working.

![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/December_neg.png)
![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/January_neg.png)
![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/February_neg.png)

### Neutral Sentiment

The neutral sentiment remained relatively static during the three months of Bitcoin chaos.

![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/December_neu.png)
![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/January_neu.png)
![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/February_neu.png)

### Compound Sentiment

In the compound sentiment charts, we can see the patterns that we saw in the positive and negative charts more drastically. For example, in the middle to end of January when Bitcoin dropped in price we see a few days of negative compound sentiment.

![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/December_comp.png)
![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/January_comp.png)
![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/February_comp.png)

### Bitcoin price

![alt text](https://github.com/KyleLawson16/text-mining/blob/master/charts/Bitcoin.png)

## <a name="Reflection">Reflection:</a>

The hardest part of this project was first learning the praw package and how to pull more complicated data sets (especially because I didn't have a lot of background experience with Reddit) and second reformatting/structuring the data for each specific use. For example, in order to score the sentiment with nltk, the data had to be formatted in a much different way than in order to build charts with matplotlib. I actually had to implement a few exception handlers when reformatting data because when pulling from an API you never quite know exactly what data will be returned. I wish I had explored Reddit more before taking on this project because it would have saved me some time with figuring out how to use their API.