import requests

url = "https://api.apilayer.com/short_url/hash"

payload = "https://google.com".encode("utf-8")
headers = {"apikey": "zkI8JiZxynxpQ6aV2ItB87s0skNEeDb1"}

print(payload)
response = requests.request("POST", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text

print(result)
