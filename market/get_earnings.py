import requests
import json

# Get recent earnings in the market

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-earnings"

querystring = {"region":"US","startDate":"1585155600000","endDate":"1589475600000","size":"10"}

headers = {
    'x-rapidapi-key': "dc36f3f082msh314873120b884b8p1604a2jsn16a865b91fe0",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
json_response = json.loads(response.text)
print(json_response['finance']['result'])