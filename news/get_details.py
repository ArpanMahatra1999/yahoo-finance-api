import requests
import json

# Read the specific news in details

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/get-details"

querystring = {"uuid": "9803606d-a324-3864-83a8-2bd621e6ccbd"}

headers = {
    'x-rapidapi-key': "dc36f3f082msh314873120b884b8p1604a2jsn16a865b91fe0",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
json_response = json.loads(response.text)
print(json_response['data']['contents'][0]['content'])
