from textblob import TextBlob

def detect_mood(user_input):
    analy=TextBlob(user_input)
    pol=analy.sentiment.polarity
    if pol > 0.3:
        return 'positive'
    elif pol < 0.3:
        return 'negative'
    else:
        return 'neutral'
    