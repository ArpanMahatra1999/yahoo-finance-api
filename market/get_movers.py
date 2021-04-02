import requests
import json

# Get the gainers, losers and most actives in a particular region

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-movers"

querystring = {"region": "US", "lang": "en-US", "start": "0", "count": "6"}

headers = {
    'x-rapidapi-key': "dc36f3f082msh314873120b884b8p1604a2jsn16a865b91fe0",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
json_response = json.loads(response.text)
print(json_response['finance']['result'][0])
print(json_response['finance']['result'][1])
print(json_response['finance']['result'][2])

