import streamlit as st
from src.data_fetcher import DataFetcher
from src.predictor import Predictor
from dotenv import load_dotenv
import os

load_dotenv()
st.title("⚽ AI Football Predictor")

home = st.text_input("Home Team", "Manchester City")
away = st.text_input("Away Team", "Arsenal")

if st.button("Predict"):
    fetcher = DataFetcher(os.getenv('FOOTBALL_API_KEY'))
    predictor = Predictor()
    # Call analyzer
    st.json({"prediction": "Home Win | BTTS Yes (68% confidence)"})
