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

def analyze_sentiment_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            return analyze_sentiment(text)
    except FileNotFoundError:
        return "The specified file does not exist."

def main():
    # Direct text analysis
    text = "I really enjoy learning with ChatGPT, it's so insightful and engaging!"
    result = analyze_sentiment(text)
    print(f"Sentiment Analysis Result (direct text): {result}")

    # Sentiment analysis from a file
    file_path = os.getenv("SENTIMENT_FILE")
    if file_path:
        file_result = analyze_sentiment_from_file(file_path)
        print(f"Sentiment Analysis Result (from file): {file_result}")
    else:
        print("No file path specified in environment variables for sentiment analysis.")

if __name__ == "__main__":
    main()