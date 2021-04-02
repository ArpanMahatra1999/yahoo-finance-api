import requests
import json

# List conversations relating to a symbol

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/conversations/list"

querystring = {"symbol": "AAPL", "messageBoardId": "finmb_24937", "region": "US", "userActivity": "true", "sortBy": "createdAt", "off": "0"}

headers = {
    'x-rapidapi-key': "dc36f3f082msh314873120b884b8p1604a2jsn16a865b91fe0",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
json_response = json.loads(response.text)
print(json_response['canvassMessages'])
