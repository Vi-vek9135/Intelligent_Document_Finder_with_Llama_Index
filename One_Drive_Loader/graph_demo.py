import json

import requests
from msal import ConfidentialClientApplication

client_id = "3a6f7573-fb1f-4856-84ed-cd30273b4a6f"
client_secret = "A_C8Q~ssjXEfak2gj-VzaSgsyIshs_T4xWngecM~"
tenant_id = "6f0e257a-ff8e-428f-9b09-54c1c3a7950c"

msal_authority = f"https://login.microsoftonline.com/6f0e257a-ff8e-428f-9b09-54c1c3a7950c"

msal_scope = ["https://graph.microsoft.com/.default"]

msal_app = ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=msal_authority,
)

result = msal_app.acquire_token_silent(
    scopes=msal_scope,
    account=None,
)

if not result:
    result = msal_app.acquire_token_for_client(scopes=msal_scope)

if "access_token" in result:
    access_token = result["access_token"]
else:
    raise Exception("No Access Token found")

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

response = requests.get(
    url="https://graph.microsoft.com/v1.0/users",
    headers=headers,
)

print(json.dumps(response.json(), indent=4))
