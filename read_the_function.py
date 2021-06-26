import json
import os
import sys

import google.auth.transport.requests
import requests
from google.oauth2.service_account import IDTokenCredentials

endpoint = "https://us-east1-tomalok-dev.cloudfunctions.net/payment-dev-create_payment"
aud = "https://us-east1-tomalok-dev.cloudfunctions.net/payment-dev-create_payment"


def invoke_endpoint(url, id_token):
    headers = {"Authorization": "Bearer " + id_token}

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print("Calling endpoint failed")
        print("HTTP Status Code:", r.status_code)
        print(r.content)
        return None

    return r.content.decode("utf-8")


if __name__ == "__main__":
    GCP_TOKEN = os.getenv("GCP_TOKEN")

    if not GCP_TOKEN:
        print("GRP_TOKEN environment variable doesn't exist.")
        sys.exit(1)

    credentials = IDTokenCredentials.from_service_account_info(
        json.loads(GCP_TOKEN),
        target_audience=aud,
    )
    request = google.auth.transport.requests.Request()

    credentials.refresh(request)

    response = invoke_endpoint(endpoint, credentials.token)

    if response is not None:
        print(response)
