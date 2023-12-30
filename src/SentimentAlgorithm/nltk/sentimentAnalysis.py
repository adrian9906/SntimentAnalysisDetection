from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

from emojiSentiment.emoji import emojiSent

def nltkSentimentAnalysis(texts):
    sentimentList = []
    
    sia = SentimentIntensityAnalyzer()
    
    for text in texts:
        scores = sia.polarity_scores(text)
        sentiment = scores['compound']
        dic = {
          'text': text,
          'sentiment':  detectSentiment(sentiment),
          'emoji': emojiSent(detectSentiment(sentiment)) 
      }
        sentimentList.append(dic)
    df = pd.DataFrame(sentimentList)
      
    return df
    
def detectSentiment(compound):
    if compound < -0.05:
        return 'negative'
    if compound >= 0.05:
        return 'positive'
    if compound > -0.05 and compound < 0.05:
        return 'neutral'