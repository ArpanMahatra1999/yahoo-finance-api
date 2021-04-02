import requests
import json

# Get data to draw chart for a specific symbol and its comparisons

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-charts"

querystring = {"symbol": "HYDR.ME", "interval": "5m", "range": "1d", "region": "US", "comparisons": "^GDAXI,^FCHI"}

headers = {
    'x-rapidapi-key': "dc36f3f082msh314873120b884b8p1604a2jsn16a865b91fe0",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
json_response = json.loads(response.text)
print(json_response['chart']['result'])
