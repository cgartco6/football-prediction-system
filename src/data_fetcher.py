import requests
from datetime import datetime

class DataFetcher:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.base_url = "https://api.football-data.org/v4"

    def get_todays_fixtures(self):
        today = datetime.now().date().isoformat()
        url = f"{self.base_url}/matches"
        headers = {'X-Auth-Token': self.api_key} if self.api_key else {}
        params = {'dateFrom': today, 'dateTo': today}
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=10)
            if resp.status_code == 200:
                return resp.json()
        except:
            return {"matches": []}
        return {"matches": []}

    def get_injuries_suspensions(self, team):
        # Placeholder - extend with API-Football or scraping
        return {"injured": [], "banned": []}

    def get_external_factors(self, venue):
        return {"weather": "Clear 22°C", "pitch": "Good", "ref": "Neutral"}
