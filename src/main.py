import os
from dotenv import load_dotenv
from data_fetcher import DataFetcher
from predictor import Predictor
from analyzer import deep_analyze_match

load_dotenv()

def main():
    api_key = os.getenv('FOOTBALL_API_KEY')
    fetcher = DataFetcher(api_key)
    predictor = Predictor()
    
    # Example
    deep_analyze_match("Team A", "Team B", fetcher, predictor)

if __name__ == "__main__":
    main()
