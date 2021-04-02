import requests
import json

# This could used for search engine optimization

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

querystring = {"q": "NYSE"}

headers = {
    'x-rapidapi-key': "dc36f3f082msh314873120b884b8p1604a2jsn16a865b91fe0",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
json_response = json.loads(response.text)
print(json_response['quotes'])
print(json_response['news'])
