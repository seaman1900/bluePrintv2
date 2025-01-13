from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Investment(BaseModel):
    invest_id: Optional[str]
    user_id: str
    print_id: str
    invest_type: str  # "Content Promotion", "Content Maintenance", "Ad Placement", "Angel Investment"
    invest_amount: float
    invest_time: Optional[str]
    invest_status: Optional[str]  # "Pending", "Approved", "Rejected", "Completed"
    last_update_time: Optional[str]
    profit: Optional[float]  # 预期或实际收益