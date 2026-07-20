import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import joblib
import os

class Predictor:
    def __init__(self, model_dir="models"):
        self.model_dir = model_dir
        os.makedirs(model_dir, exist_ok=True)
        self.model_1x2 = None
        self.model_btts = None
        self.load_models()

    def load_models(self):
        try:
            self.model_1x2 = joblib.load(f"{self.model_dir}/1x2_model.pkl")
            self.model_btts = joblib.load(f"{self.model_dir}/btts_model.pkl")
        except:
            print("No trained models found. Train first.")

    def train(self, historical_data):
        X = historical_data[['home_goals_avg', 'away_goals_avg', 'home_form', 'away_form',
                             'injury_impact_home', 'injury_impact_away', 'h2h_home_adv',
                             'weather_impact', 'coach_factor', 'key_players_home', 'cards_home']]
        y_1x2 = historical_data['result']
        y_btts = historical_data['btts']
        
        self.model_1x2 = RandomForestClassifier(n_estimators=200, random_state=42)
        self.model_1x2.fit(X, y_1x2)
        
        self.model_btts = xgb.XGBClassifier(random_state=42)
        self.model_btts.fit(X, y_btts)
        
        joblib.dump(self.model_1x2, f"{self.model_dir}/1x2_model.pkl")
        joblib.dump(self.model_btts, f"{self.model_dir}/btts_model.pkl")
        print("Models trained and saved.")

    def predict(self, home_team, away_team, features_dict):
        features = [
            features_dict.get('home_goals_avg', 1.5),
            features_dict.get('away_goals_avg', 1.4),
            features_dict.get('home_form', 0.65),
            features_dict.get('away_form', 0.6),
            features_dict.get('injury_impact_home', 0),
            features_dict.get('injury_impact_away', 0),
            features_dict.get('h2h_home_adv', 0.5),
            features_dict.get('weather_impact', 0),
            features_dict.get('coach_factor', 0.7),
            features_dict.get('key_players_home', 1.0),
            features_dict.get('cards_home', 1.8),
        ]
        if self.model_1x2 is None:
            return {"error": "Train model first"}
        
        pred_1x2_prob = self.model_1x2.predict_proba([features])[0]
        btts_prob = self.model_btts.predict_proba([features])[0][1]
        
        outcome_idx = np.argmax(pred_1x2_prob)
        outcomes = ['Home Win', 'Draw', 'Away Win']
        
        return {
            'match': f"{home_team} vs {away_team}",
            '1X2': outcomes[outcome_idx],
            '1X2_Prob_%': round(pred_1x2_prob[outcome_idx] * 100, 1),
            'BTTS': 'Yes' if btts_prob > 0.5 else 'No',
            'BTTS_Prob_%': round(btts_prob * 100, 1),
            'Confidence_%': round(max(pred_1x2_prob) * 100, 1)
        }
