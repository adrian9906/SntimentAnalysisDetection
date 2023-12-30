from IPython.display import display
from tabulate import tabulate
from SentimentAlgorithm.nltk.sentimentAnalysis import nltkSentimentAnalysis
from SentimentAlgorithm.textBlob.sentimentDetection import sentimentTextBlob


tweets = [
 "dear @verizonsupport your service is straight shit in dallas.. been with y'all over a decade and this is all time low for y'all. i'm talking no internet at all.",
 "@verizonsupport I sent you a dm",
 "thanks to michelle et al at @verizonsupport who helped push my no-show-phone problem along. Order canceled successfully, and I ordered this for pickup today at the Apple store in the mall."
 ]

df = sentimentTextBlob(tweets)

df2 = nltkSentimentAnalysis(tweets)


print(tabulate(df, headers="keys", tablefmt="pretty"))

print('\n\n')

print(tabulate(df2, headers="keys", tablefmt="pretty"))