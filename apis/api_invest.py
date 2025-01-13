# 投资相关API
import requests
from datetime import datetime
from models.invest import Investment

BASE_URL = "http://127.0.0.1:8000"

def create_invest(user_id, print_id, amount, investment_type):
    # 创建投资
    url = f"{BASE_URL}/invest/create"
    invest = Investment(
        invest_id=None,
        user_id=user_id,
        print_id=print_id,
        invest_amount=amount,
        invest_type=investment_type,
        invest_time=datetime.now().isoformat(),
        invest_status="created",
        last_update_time=datetime.now().isoformat(),
        profit=0.0
    )
    response = requests.post(url, json=invest.model_dump())
    return response.json()