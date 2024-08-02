from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.before_request
def before_request():
    if request.is_json:
        request.data = request.get_json()
    else:
        return jsonify({"error": "Request must be JSON"}), 400

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.data
    result = {"sentiment": "Positive", "confidence": 0.95}
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 5000))