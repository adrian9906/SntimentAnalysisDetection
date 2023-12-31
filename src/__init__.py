import json
from IPython.display import display
from sklearn.metrics import accuracy_score
from tabulate import tabulate
from Audio2Text.audio_text import voiceToText
from ExtractPDFInfo.pdfExtractor import extractText
from SentimentAlgorithm.nltk.sentimentAnalysis import nltkSentimentAnalysis
from SentimentAlgorithm.textBlob.sentimentDetection import sentimentTextBlob


def sentimenDetectMain(data):
    dfTextBlob = sentimentTextBlob(data)

    dfNLTK = nltkSentimentAnalysis(data)
    
    return dfNLTK, dfTextBlob

        
        
#PDF Extractor
# texts = extractText('D:/apps/Proyectos Freelance/SntimentAnalysisDetection/dataset/Raven.pdf')
# df, df2 = sentimenDetectMain(texts)

# print(df)

# print(df2)

# Tweet dataset
# datatext = []
# with open ('D:/apps/Proyectos Freelance/SntimentAnalysisDetection/dataset/Sentiment_EN_WorldCup.json',mode='r') as file:
#     data = json.load(file)

# datatext = [x['tweet_text'] for x in data]
# dataLabel = [x['sentiment'].lower() for x in data]

# df, df2 = sentimenDetectMain(datatext)

# labelTextBlob = [x for x in df2['sentiment']]
# labelNLTK = [x for x in df['sentiment']]


# accuracy = accuracy_score(labelNLTK, dataLabel)
# accuracy2 = accuracy_score(labelTextBlob, dataLabel)    

# print(accuracy)

# print(accuracy2)

audio = [voiceToText('es')]

if audio != 'still waiting':
    df, df2 = sentimenDetectMain(audio)
    print(df)
    print(df2)    
