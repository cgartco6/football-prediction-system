from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from src.data_fetcher import DataFetcher
from src.predictor import Predictor
from src.analyzer import deep_analyze_match

load_dotenv()
app = Flask(__name__)

fetcher = DataFetcher(os.getenv('FOOTBALL_API_KEY'))
predictor = Predictor()

@app.route('/')
def home():
    return """
    <h1>Football Predictor API</h1>
    <p>Use /predict?home=Manchester%20United&away=Liverpool</p>
    """

@app.route('/predict')
def predict():
    home = request.args.get('home', 'Home')
    away = request.args.get('away', 'Away')
    result = deep_analyze_match(home, away, fetcher, predictor)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
