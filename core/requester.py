import requests


def get_my_ip():
    return requests.get("https://api.ipify.org?format=json").json()
