from emoji import emojize

def emojiSent(sentiment):
    if sentiment == 'positive':
        return emojize(":grinning_face:")
    if sentiment == 'negative':
        return emojize(":angry_face:")
    if sentiment == 'neutral':
        return emojize(":neutral_face:")
    