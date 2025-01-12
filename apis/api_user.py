import requests
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000"

def get_user(user_id):
    response = requests.get(f"{BASE_URL}/user/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return None