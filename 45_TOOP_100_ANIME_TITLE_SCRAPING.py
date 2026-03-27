import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

FilePPath = "TOP_100_ANIME_TITLES.txt"
urls = [
    "https://myanimelist.net/topanime.php",
    "https://myanimelist.net/topanime.php?limit=50"
]

anime_data = []

for URL in urls:
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.select("h3.anime_ranking_h3 a")
    scores = soup.select("div.js-top-ranking-score-col span")

    for t, s in zip(titles, scores):
        title = t.text.strip()
        score = s.text.strip()
        anime_data.append((title, score))

with open(FilePPath, "w", encoding="utf-8") as file:
    for i, (title, score) in enumerate(anime_data, start=1):
        
        line = f"{i}. {title:<45} ⭐ {score}"
        
        print(line)
        file.write(line + "\n")
