import requests
import json

# Get the most popular portfolios

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-popular-watchlists"

headers = {
    'x-rapidapi-key': "dc36f3f082msh314873120b884b8p1604a2jsn16a865b91fe0",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
json_response = json.loads(response.text)
print(json_response['finance']['result'][0]['portfolios'])