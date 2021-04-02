import requests
import json

# For brief comparison charts

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-spark"

querystring = {"symbols":"AMZN,AAPL,WDC,REYN,AZN,YM=F","interval":"1m","range":"1d"}

headers = {
    'x-rapidapi-key': "dc36f3f082msh314873120b884b8p1604a2jsn16a865b91fe0",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
json_response = json.loads(response.text)
print(json_response)