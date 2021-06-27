from datetime import datetime

from src.domain.enums.transactions import TransactionStatus


class Transactions:
    @staticmethod
    def get_transactions_to_validate():
        now = datetime.now()

        return [
            {
                "_id": "123456",
                "amount": 15000,
                "status": TransactionStatus.WAITING_CONFIRMATION.value,
                "created_at": now,
                "updated_at": now,
            }
        ]
