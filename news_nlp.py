from textblob import TextBlob

news_summary = """A woman died from treatment delays after a hospital in Germany hit by a cyberattack was forced to turn away emergency patients.
This is a small sample of the toll from ransomware attacks, in which hackers break into computer networks and freeze the digital information until the targeted organization or city pays for its release.
Victims have two bad choices: Give in to extortion and hope the criminals didn’t do too much damage, or refuse and risk the hackers releasing or deleting essential information.
I spoke to Charles Carmakal, an executive with the cybersecurity response company FireEye Mandiant, about the root causes and fixes for ransomware attacks.
What are the root causes of ransomware?"""

def findSentiment(news_story):
    news = TextBlob(news_story)
    sentiments = []

    for sentence in news.sentences:
        sentiment = sentence.sentiment
        for metric in sentiment:
            sentiments.append(metric)

    print(sentiments)
    polarity = []
    subjectivity = []

    for i in range (len(sentiments)):
        if i%2==0:
            polarity.append(sentiments[i])
        else:
            subjectivity.append(sentiments[i])

    print(polarity)
    print(subjectivity)
    polarity_avg = calculate_avg(polarity)
    subjectivity_avg = calculate_avg(subjectivity)

    print()
    print("FINAL ANALYSIS")
    print("-----------------------------------")
    print("Polarity: " + calculate_sentiment(polarity_avg, "polarity"))
    print("Subjectivity: " + calculate_sentiment(subjectivity_avg, "subjectivity"))


def calculate_avg(list):
    return sum(list) / len(list);

def calculate_sentiment(sentiment, type):
    sentiment_category = ""
    if type == "polarity":
        if sentiment > 0.75:
            sentiment_category = "Extremely positive."
        elif sentiment > 0.5:
            sentiment_category = "Significantly positive."
        elif sentiment > 0.3:
            sentiment_category = "Fairly positive."
        elif sentiment > 0.1:
            sentiment_category = "Slightly positive."
        elif sentiment < -0.1:
            sentiment_category = "Slightly negative."
        elif sentiment < -0.3:
            sentiment_category = "Fairly negative."
        elif sentiment < -0.5:
            sentiment_category = "Significantly negative."
        elif sentiment < -0.75:
            sentiment_category = "Extremely negative."
        else:
            sentiment_category = "Neutral."
        return sentiment_category
    elif type == "subjectivity":
        if sentiment > 0.75:
            sentiment_category = "Extremely subjective."
        elif sentiment > 0.5:
            sentiment_category = "Fairly subjective."
        elif sentiment > 0.3:
            sentiment_category = "Fairly objective."
        elif sentiment > 0.1:
            sentiment_category = "Extremely objective."
        return sentiment_category
    else:
        print("Invalid Input.")


# findSentiment(news_summary)