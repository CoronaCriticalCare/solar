import requests
from datetime import datetime, timedelta
from config import SOLAR_URL, API_KEY




def get_solar():
    end_date = datetime.today()
    start_date = end_date - timedelta(days=30)

    end = end_date.strftime("%Y-%m-%d")
    start = start_date.strftime("%Y-%m-%d")

    params = {
        "startDate": start,
        "endDate": end,
        "api_key": API_KEY
    }

    response = requests.get(SOLAR_URL, params=params)
    response.raise_for_status()

    data = response.json()
    
    if not data:
        return None

    return data
