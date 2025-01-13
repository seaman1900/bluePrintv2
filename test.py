from models.invest import Investment
from datetime import datetime

if __name__ == "__main__":
    # Create an investment object
    investment = Investment(
        invest_id="123",
        user_id="123",
        print_id="123",
        invest_type="Content Promotion",  # "Content Promotion", "Content Maintenance", "Ad Placement", "Angel Investment"
        invest_amount=100.0,
        invest_time= datetime.now(),
        invest_status="Pending",
        last_update_time=datetime.now(),
        profit=10.0
    )
    print(investment.model_dump())