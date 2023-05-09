import requests
from requests.auth import HTTPBasicAuth
import json

apiUrl = "https://api.sec-api.io?token=fc6b6f50708c6badf613a33abefc6ea3efdbc00bdb6f9e9dc1bf80cb20f4e26f"

qString = "8-K"

query = {
    "query": {
        "query_string": {
            "query": f"formType:\"{qString}\""
        }
    },
    "from": "0",
    "size": "20",
    "sort": [{"filedAt": {"order": "desc"}}]
}

response = requests.post(apiUrl, json=query)
response = response.json()

filings = response["filings"]

for o in filings:
   print(o["companyName"])