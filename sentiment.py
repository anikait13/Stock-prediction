
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is : ", sentiment_dict)

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        return ("Positive")

    elif sentiment_dict['compound'] <= - 0.05:
        return("Negative")

    else:
        return ("Neutral")
