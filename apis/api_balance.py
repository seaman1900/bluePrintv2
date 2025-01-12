# 余额相关操作
import requests

from models.balance import Balance
BASE_URL = "http://127.0.0.1:8000"

# 查询
def get_balance(user_id: str):

    url = BASE_URL + "/balance/" + user_id
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
# 更新
def update_balance(user_id: str, new_balance: Balance):
    url = BASE_URL + "/balance/" + user_id
    response = requests.put(url, json=new_balance.dict())
    if response.status_code == 200:
        return response.json()
    else:
        return None
