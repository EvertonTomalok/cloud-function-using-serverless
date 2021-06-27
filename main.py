from src.domain.requester import get_my_ip
import os

from src.repositories.transactions import Transactions


def create_payment(request):
    my_ip = get_my_ip()

    return {**my_ip, "my_token": os.getenv("PAGAR_ME_TOKEN")}


def get_transactions_not_confirmed(request):
    return {
        "status": "ok",
        "data": Transactions.get_transactions_to_validate()
    }
