import requests
import json

# Get detail information of specific watchlist

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-watchlist-detail"

querystring = {"userId": "X3NJ2A7VDSABUI4URBWME2PZNM", "pfId": "the_berkshire_hathaway_portfolio"}

headers = {
    'x-rapidapi-key': "dc36f3f082msh314873120b884b8p1604a2jsn16a865b91fe0",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
json_response = json.loads(response.text)
print(json_response['finance']['result'])
