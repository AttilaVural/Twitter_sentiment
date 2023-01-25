import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment(search, max_results):
    # our search term, using syntax for Twitter's Advanced Search
    # search = '"data science"'

    # the scraped tweets, this is a generator
        # uses Twitter’s advanced search - see here https://github.com/igorbrigadir/twitter-advanced-search 
    scraped_tweets = sntwitter.TwitterSearchScraper(search).get_items()

    # slicing the generator to keep only the first 100 tweets
    sliced_scraped_tweets = itertools.islice(scraped_tweets, max_results)

    # convert to a DataFrame and keep only relevant columns
    df = pd.DataFrame(sliced_scraped_tweets)[['date', 'rawContent']]
    #df = pd.DataFrame(sliced_scraped_tweets)['rawContent']

    analyzer = SentimentIntensityAnalyzer()

    scores = []
    for text in df['rawContent']:
        vs = analyzer.polarity_scores(text)
        scores.append(vs['compound'])
     
    df['com_score'] = scores
    
    return df