# Sentiment analysis using Textblob

from textblob import TextBlob


def sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return "positif"
    elif analysis.sentiment.polarity == 0:
        return "neutre"
    else:
        return "negatif"
