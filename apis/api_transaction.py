import requests
from models.transaction import TransactionRequest
# API 基础URL
BASE_URL = "http://127.0.0.1:8000"

# 充值积分
def recharge(user_id, amount):
    url = f"{BASE_URL}/transaction/create"
    trans_request = TransactionRequest(
        user_id=user_id, amount=amount, trans_type="recharge")
    response = requests.post(url, json=trans_request.dict())
    return response.json()
# 购买print
def buy_print(user_id, print_id, amount):
    url = f"{BASE_URL}/transaction/create"
    trans_request = TransactionRequest(
        user_id=user_id, print_id=print_id, amount=amount, trans_type="purchase")
    response = requests.post(url, json=trans_request.dict())
    return response.json()

# 检查是否已经购买
def check_purchase(user_id, print_id):
    url = f"{BASE_URL}/transaction/check/{user_id}/{print_id}"
    response = requests.get(url)
    return response.json().get("message")