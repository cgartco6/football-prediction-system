def deep_analyze_match(home, away, fetcher, predictor):
    print(f"\n🔍 DEEP ANALYSIS: {home} vs {away}")
    features = {
        'home_goals_avg': 1.6, 'away_goals_avg': 1.4,
        'home_form': 0.7, 'away_form': 0.6,
        'injury_impact_home': -0.1,
        'h2h_home_adv': 0.55,
        'weather_impact': 0.0,
        'coach_factor': 0.8,
        'key_players_home': 0.9,
        'cards_home': 1.9,
    }
    pred = predictor.predict(home, away, features)
    print(pred)
    return pred
