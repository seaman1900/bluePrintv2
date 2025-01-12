# 用户余额单独管理
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class Balance(BaseModel):
    user_id: str
    balance: float
    frozen_amount: float
    last_update_time: Optional[datetime]