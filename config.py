import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SOLAR_API")
SOLAR_URL = "https://kauai.ccmc.gsfc.nasa.gov/DONKI/WS/get/FLR"

if not API_KEY:
    raise ValueError("SOLAR_API was not found")