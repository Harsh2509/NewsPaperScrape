from textblob import TextBlob, Word
import random


news_summary = """"A woman died from treatment delays after a hospital in Germany hit by a cyberattack was forced to turn away emergency patients.
This is a small sample of the toll from ransomware attacks, in which hackers break into computer networks and freeze the digital information until the targeted organization or city pays for its release.
Victims have two bad choices: Give in to extortion and hope the criminals didn’t do too much damage, or refuse and risk the hackers releasing or deleting essential information.
I spoke to Charles Carmakal, an executive with the cybersecurity response company FireEye Mandiant, about the root causes and fixes for ransomware attacks.
What are the root causes of ransomware?"""


def nlp_classification(text):
    print("Summary: " + "\n" + text)
    print()
    summary = TextBlob(text)

    print("POS tagging: " + str(summary.tags))
    print()

    print("Words: " + str(summary.words))
    print()

    print("Plural of " + summary.words[1] + "-->" + summary.words[1].pluralize())
    print("Singular of " + summary.words[5] + "-->" + summary.words[5].singularize())

    print("Sentences: " + str(summary.sentences))

    nouns = []
    for word,tag in summary.tags:
        if tag=="NN":
            nouns.append(word)

    print("This text is about...")
    for item in random.sample(nouns, 5):
        word = Word(item);
        word.lemmatize()
        print(word.pluralize())


nlp_classification(news_summary)