import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes_data = []

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
for q, a in zip(quotes, authors):
    quotes_data.append({"quote": q.text, "author": a.text})

print("Citations recuperees :",len(quotes_data))