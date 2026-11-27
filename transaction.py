from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

@dataclass
class Transaction:
    transaction_id: str
    account_id: str
    amount: Decimal
    timestamp: datetime
    transaction_type: str