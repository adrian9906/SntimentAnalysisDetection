

import pandas as pd
from textblob import TextBlob

from emojiSentiment.emoji import emojiSent


def sentimentTextBlob(texts):
    sentimentList = []
    
    for text in texts:
        if text != '':
            blob = TextBlob(text)
            sentiment = detectSentiment(blob.polarity)
            dic = {
                'text': text,
                'sentiment': sentiment,
                'emoji': emojiSent(sentiment) 
            }
            sentimentList.append(dic)
      
    df = pd.DataFrame(sentimentList)
      
    return df

def detectSentiment(polarity):
    if polarity < 0:
        return 'negative'
    if polarity >= 0.5:
        return 'positive'
    if polarity >= 0 and polarity < 0.5:
        return 'neutral'
      



