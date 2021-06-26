from core.requester import get_my_ip
import os


def create_payment(request):
    my_ip = get_my_ip()

    return {**my_ip, "my_token": os.getenv("PAGAR_ME_TOKEN")}
