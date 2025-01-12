from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Transaction(BaseModel):
    transaction_id: str
    trans_type: str
    user_id: str
    print_id: Optional[str]
    amount: int
    created_at: datetime
    status: str
    updated_at: datetime

class TransactionRequest(BaseModel):
    trans_type: str
    user_id: str
    print_id: Optional[str]
    amount: int