from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from sentiment_controller import analyze_sentiment

load_dotenv()

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def sentiment_analysis():
    data = request.get_json()
    text = data.get('text', '')
    
    if text:
        result = analyze_sentiment(text)
        return jsonify(result), 200
    else:
        return jsonify({"error": "No text provided"}), 400

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(host='0.0.0.0', port=port)