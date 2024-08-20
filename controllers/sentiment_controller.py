from flask import Flask, request, jsonify
from textblob import TextBlob
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/analyze-sentiment', methods=['POST'])
def analyze_sentiment():
    try:
        if not request.json:
            return jsonify({"error": "Request must be JSON."}), 400
        if 'text' not in request.json:
            return jsonify({"error": "Please provide a text review."}), 400
        
        text = request.json['text']
        
        try:
            analysis = TextBlob(text)
            sentiment_score = analysis.sentiment.polarity
            
            if sentiment_score > 0:
                sentiment = "Positive"
            elif sentiment_score == 0:
                sentiment = "Neutral"
            else:
                sentiment = "Negative"
            
            return jsonify({"sentiment": sentiment, "score": sentiment_score})
        except Exception as e:
            return jsonify({"error": "Error processing the text.", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == "__main__":
    try:
        port = os.getenv("PORT", 5000)
        app.run(debug=True, host='0.0.0.0', port=int(port))
    except Exception as e:
        print(f"Unable to start the server: {e}")