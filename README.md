# TOP-100-Anime-Title-Scraping
DAY - 45/100 - Project - python X TOP 100 Anime Title Scraping

# 🍥 Top 100 Anime Titles Scraper

A simple Python script that scrapes the **Top 100 anime titles and ratings** from MyAnimeList and saves them into a text file.

---

## 🎥 Demo

[https://github.com/guptaji0358/TOP-100-Anime-Title-Scraping/blob/main/Demo.mp4]

> ▶️ Watch the demo to see how the script runs and generates the output file.

---

## 🚀 Features

* 📡 Scrapes Top 100 anime from MyAnimeList
* 🔢 Handles pagination automatically (2 pages)
* ⭐ Extracts anime titles and ratings
* 💾 Saves results into a `.txt` file
* 🖥️ Prints formatted output in terminal
* ⚡ Lightweight and beginner-friendly

---

## 🧰 Tech Stack

* **Python** 🐍
* **Requests** – HTTP requests
* **BeautifulSoup (bs4)** – HTML parsing

---

## 📂 Project Structure

```bash
TOP-100-Anime-Title-Scraping/
│── 45_TOP_100_ANIME_SCRAPPING.py   # Main script
│── TOP_100_ANIME_TITLES.txt        # Output file (generated)
│── demo.mp4                        # Demo video
│── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/guptaji0358/TOP-100-Anime-Title-Scraping.git
cd TOP-100-Anime-Title-Scraping
pip install requests beautifulsoup4
```

---

## ▶️ Usage

```bash
python 45_TOP_100_ANIME_SCRAPPING.py
```

---

## 🧪 How It Works

1. Sends HTTP requests to:

   * https://myanimelist.net/topanime.php
   * https://myanimelist.net/topanime.php?limit=50

2. Parses HTML using BeautifulSoup

3. Extracts:

   * Anime titles
   * Ratings (scores)

4. Stores data in a list

5. Outputs formatted results like:

```
1. Fullmetal Alchemist: Brotherhood        ⭐ 9.10
2. Attack on Titan Final Season            ⭐ 9.00
```

---

## 📁 Output

* File: `TOP_100_ANIME_TITLES.txt`

Format:

```
Rank. Title                                   ⭐ Score
```

---

## ⚠️ Important Notes

* Uses a **User-Agent header** to reduce blocking
* Website structure may change and break the scraper
* Respect MyAnimeList terms of service
* Avoid excessive requests

---

## 🌍 Open Source Contribution

This project is **open source**, and anyone can improve it.

* 🍴 Fork the repository
* ✏️ Make changes
* 🔁 Submit a Pull Request

---

## 💡 Upgrade & Improvements

This project is open for everyone to **fully upgrade, improve, and extend**.
Feel free to enhance features, optimize performance, or add new functionalities 🚀

---

## 👨‍💻 Author

**Robin Gupta**

---

## 📜 License

MIT License

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

