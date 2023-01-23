import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# our search term, using syntax for Twitter's Advanced Search
search = '"data science"'

# the scraped tweets, this is a generator
    # uses Twitter’s advanced search - see here https://github.com/igorbrigadir/twitter-advanced-search 
scraped_tweets = sntwitter.TwitterSearchScraper(search).get_items()

# slicing the generator to keep only the first 100 tweets
sliced_scraped_tweets = itertools.islice(scraped_tweets, 2)

# convert to a DataFrame and keep only relevant columns
#df = pd.DataFrame(sliced_scraped_tweets)[['date', 'rawContent']]
df = pd.DataFrame(sliced_scraped_tweets)['rawContent']

#print(df)


analyzer = SentimentIntensityAnalyzer()
for sentence in df:
    vs = analyzer.polarity_scores(sentence)
    comp_score = vs['compound']
    print("{:-<65} {}".format(sentence, str(vs)))
    print(comp_score)
    