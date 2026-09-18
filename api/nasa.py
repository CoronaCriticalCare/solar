import requests
import time
from datetime import datetime, timedelta
from config import *


end_date = datetime.today()
start_date = end_date - timedelta(days=30)

end = end_date.strftime("%Y-%m-%d")
start = start_date.strftime("%Y-%m-%d")

def get_solar():
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

def get_apod():
    params = {
        "api_key": API_KEY
    }

    response = requests.get(APOD_URL, params=params)
    response.raise_for_status()

    data = response.json()

    if not data:
        return None

    return data

def get_cme():
    params = {
        "startDate": start,
        "endDate": end,
        "api_key": API_KEY
    }

    for attempt in range(3):
        try:
            response = requests.get(
                CME_URL,
                params=params,
                timeout=30
            )

            response.raise_for_status()

            data = response.json()

            if not data:
                return []

            return data

        except requests.exceptions.HTTPError as e:
            if response.status_code == 503:
                #print(f"CME API unavailable. Retry {attempt + 1}/3...")
                time.sleep(5)

            else:
                print(f"CME API error: {e}")
                return None

    print("CME API unavailable after 3 attempts.")

    return None