import requests
from datetime import datetime
from models.print import Print, PrintMetadata
# API 基础URL
BASE_URL = "http://127.0.0.1:8000"

def get_prints_all():
    url = f"{BASE_URL}/print/all"
    response = requests.get(url)
    return response.json()

def get_prints_by_id(user_id, print_id):
    url = f"{BASE_URL}/print/{user_id}"
    data ={
        "user_id": user_id,
        "print_id": print_id
    }
    response = requests.get(url, json=data)
    return response.json()