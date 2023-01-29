import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment(search, max_results):
    # our search term, using syntax for Twitter's Advanced Search
    # search = "data science since:2023-01-01 until:2023-01-01"

    # the scraped tweets, this is a generator
        # uses Twitter’s advanced search - see here https://github.com/igorbrigadir/twitter-advanced-search 
    scraped_tweets = sntwitter.TwitterSearchScraper(search).get_items()

    # slicing the generator to keep only the first 100 tweets
    sliced_scraped_tweets = itertools.islice(scraped_tweets, max_results)
    # the values of "sliced_scraped_twetts" are retrieved" can only be trieved once, so saving them in here
    data = list(sliced_scraped_tweets)
    if data != []:
        # convert to a DataFrame and keep only relevant columns
        df = pd.DataFrame(data)[['date', 'rawContent']]
        #df = pd.DataFrame(sliced_scraped_tweets)['rawContent']
        
        analyzer = SentimentIntensityAnalyzer()

        scores = []
        for text in df['rawContent']:
            vs = analyzer.polarity_scores(text)
            scores.append(vs['compound'])
         
        df['com_score'] = scores
        
        return df
    else:
        return pd.DataFrame({})
