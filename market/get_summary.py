import requests
import json

# Get live summary information of market by region

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-summary"

querystring = {"region": "US"}

headers = {
    'x-rapidapi-key': "dc36f3f082msh314873120b884b8p1604a2jsn16a865b91fe0",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
json_response = json.loads(response.text)
print(json_response['marketSummaryAndSparkResponse']['result'])