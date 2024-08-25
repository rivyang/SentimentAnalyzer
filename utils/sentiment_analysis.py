from textblob import TextBlob
import os
from dotenv import load_dotenv

load_dotenv()

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return {
        "polarity": sentiment.polarity,
        "subjectivity": sentiment.subjectivity
    }

if __name__ == "__main__":
    text = "I really enjoy learning with ChatGPT, it's so insightful and engaging!"
    result = analyze_sentiment(text)
    print(f"Sentiment Analysis Result: {result}")