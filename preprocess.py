# Cleaning the tweets
import re
from nltk.stem import WordNetLemmatizer


def preprocess(tweet):
    # remove links
    tweet_str = str(tweet)

    tweet_str = re.sub(r'http\S+', '', tweet_str)
    # remove mentions
    tweet_str = re.sub("@\w+", "", tweet_str)
    # alphanumeric and hashtags
    tweet_str = re.sub("[^a-zA-Z#]", " ", tweet_str)
    # remove multiple spaces
    tweet_str = re.sub("\s+", " ", tweet_str)
    tweet_str = tweet_str.lower()
    # Legitimatize
    lemmatizer = WordNetLemmatizer()
    sent = ' '.join([lemmatizer.lemmatize(w) for w in tweet_str.split() if len(lemmatizer.lemmatize(w)) > 3])
    return sent
