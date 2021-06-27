from enum import Enum


class TransactionStatus(Enum):
    PAID = "PAID"
    WAITING_CONFIRMATION = "WAITING_CONFIRMATION"
    CANCELED = "CANCELED"
