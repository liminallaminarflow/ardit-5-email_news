import requests

api_key = "08d5a4dad5c34d6bb0bed70c3610b591"
# url: str = "https://newsapi.org/v2/everything?q=ukraine?country=us&category=business"\
#             "&apiKey=" + api_key

url = "https://newsapi.org/v2/everything?q=ukraine&searchin=title&from&language=en&from=2023-03-15&sortBy=publishedAt&apiKey=08d5a4dad5c34d6bb0bed70c3610b591"




request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["source"]["name"] + ": " + article["title"])
    print(article["publishedAt"])
    print(article["description"])
    print(article["url"])
    print("\n")






