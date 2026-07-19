import requests
import pandas as pd
import json
import re
import time

from bs4 import BeautifulSoup

headers = {
    "User-Agent": "EducationalScraper/1.0"
}

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

data = []

for page in range(1, 51):

    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = (
            f"https://books.toscrape.com/"
            f"catalogue/page-{page}.html"
        )

    print(f"Scraping Page {page}: {url}")

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code != 200:
        print(f"Failed Page {page}")
        continue

    soup = BeautifulSoup(
        response.text,
        "lxml"
    )

    books = soup.find_all(
        "article",
        class_="product_pod"
    )

    for book in books:

        title = book.h3.a["title"]

        price = book.find(
            "p",
            class_="price_color"
        ).text

        price = float(
            re.sub(r"[^\d.]", "", price)
        )

        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        rating = book.find(
            "p",
            class_="star-rating"
        )["class"][1]

        rating = rating_map[rating]

        data.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating
        })

    time.sleep(1)

print(f"\nTotal Books Scraped: {len(data)}")

# Save JSON
with open(
    "books.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        data,
        f,
        indent=4,
        ensure_ascii=False
    )

# Save CSV
df = pd.DataFrame(data)

df.to_csv(
    "books.csv",
    index=False,
    encoding="utf-8"
)

print("books.json saved")
print("books.csv saved")
