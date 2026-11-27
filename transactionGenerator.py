import random
from datetime import datetime
from transaction import Transaction
from decimal import Decimal

# We use decimals due to needing precise figures.
# Slower but more accurate than floats, which can have rounding errors.

# Generates random transactions being offered from vendors
# These vendors are offering to buy or to sell items, 
# and the transactions are generated in real-time to simulate a live environment.

class TransactionGenerator:
    def __init__(self, num_transactions):
        self.num_transactions = num_transactions

    def generate_transaction(self) -> Transaction:
        transaction_id = str(random.randint(100000, 999999))
        account_id = str(random.randint(1000, 9999))

        # Transactions come in multiples of 5000 between 1000 and 1,000,000
        amount = round(random.uniform(1e3, 1e6), 2 )
        rounded_amount = (amount // 5000 ) * 5000

        # Can add currency conversion later
        # currency = random.choice(['USD', 'EUR', 'GBP', 'JPY'])
        timestamp = datetime.now()

        transaction_type = random.choice(['BUY', 'SELL'])

        return Transaction(
            transaction_id,
            account_id,
            Decimal(str(rounded_amount)),
            timestamp,
            transaction_type
        )

    def generate_transactions(self):
        transactions = []
        for _ in range(self.num_transactions):
            transactions.append(self.generate_transaction())
        return transactions