import unittest
from datetime import datetime
from decimal import Decimal

from transaction import Transaction
from transactionGenerator import TransactionGenerator

class TestTransactionGenerator(unittest.TestCase):
    def test_creates_correct_number_and_types_of_transactions(self):
        expected_count = 10
        generator = TransactionGenerator(expected_count)

        transactions = generator.generate_transactions()

        self.assertEqual(len(transactions), expected_count)

        for transaction in transactions:
            self.assertIsInstance(transaction, Transaction)
            self.assertIsInstance(transaction.transaction_id, str)
            self.assertIsInstance(transaction.account_id, str)
            self.assertIsInstance(transaction.amount, Decimal)
            self.assertIsInstance(transaction.timestamp, datetime)
            self.assertIsInstance(transaction.transaction_type, str)
            self.assertIn(transaction.transaction_type, {"BUY", "SELL"})


if __name__ == "__main__":
    unittest.main()
