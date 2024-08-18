from flask import Flask, request, jsonify
from textblob import TextBlob
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/analyze-sentiment', methods=['POST'])
def analyze_sentiment():
    if not request.json or 'text' not in request.json:
        return jsonify({"error": "Please provide a text review."}), 400
    
    text = request.json['text']
    
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity
    
    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score == 0:
        sentiment = "Neutral"
    else:
        sentiment = "Negative"
    
    return jsonify({"sentiment": sentiment, "score": sentiment_score})

if __name__ == "__main__":
    port = os.getenv("PORT", 5000)
    app.run(debug=True, host='0.0.0.0', port=port)