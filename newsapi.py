
import requests
import secrets

base_url = 'https://newsapi.org/v2/top-headlines'
params = {
    "q": "new hampshire",
    "apiKey": secrets.NEWSAPI_KEY
}

response = requests.get(base_url, params)
result = response.json()
x = result

new_hampshire = []

for i in x["articles"]:
    print(i["title"], "-", i["source"]["name"])

# new_hampshire.append(i)





