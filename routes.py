from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from sentiment_controller import analyze_sentiment

load_dotenv()

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def sentiment_analysis():
    data = request.json or {}
    text = data.get('text', '').strip()
    
    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = analyze_sentiment(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))