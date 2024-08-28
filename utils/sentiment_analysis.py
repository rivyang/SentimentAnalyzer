from textblob import TextBlob
import os
from dotenv import load_dotenv

load_dotenv()

def analyze_text_sentiment(text):
    sentiment_analysis_result = TextBlob(text).sentiment
    return {
        "polarity": sentiment_analysis_result.polarity,
        "subjectivity": sentiment_analysis_result.subjectivity
    }

def analyze_file_sentiment(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file_content:
            text = file_content.read()
            return analyze_text_sentiment(text)
    except FileNotFoundError:
        return "The specified file does not exist."

def main():
    # Direct text sentiment analysis
    input_text = "I really enjoy learning with ChatGPT, it's so insightful and engaging!"
    direct_text_analysis_result = analyze_text_sentiment(input_text)
    print(f"Sentiment Analysis Result (Direct Text): {direct_text_analysis_result}")

    # Sentiment analysis from file content
    file_path_environment_variable = os.getenv("SENTIMENT_FILE")
    if file_path_environment_variable:
        sentiment_analysis_file_result = analyze_file_sentiment(file_path_environment_variable)
        print(f"Sentiment Analysis Result (File): {sentiment_analysis_file_result}")
    else:
        print("No file path specified in environment variables for sentiment analysis.")

if __name__ == "__main__":
    main()