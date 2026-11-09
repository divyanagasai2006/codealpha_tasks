import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://books.toscrape.com/"
next_url = urljoin(base_url, "catalogue/page-1.html")

books = []

while next_url:
    print("Scraping:", next_url)

    response = requests.get(next_url, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").get_text(strip=True).replace("Â£", "£")
        availability = book.select_one(".availability").get_text(strip=True)
        rating = book.select_one(".star-rating")["class"][1]
        link = urljoin(next_url, book.h3.a["href"])

        books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product_Link": link
        })

    next_button = soup.select_one("li.next a")

    if next_button:
        next_url = urljoin(next_url, next_button["href"])
    else:
        next_url = None

    time.sleep(0.3)

df = pd.DataFrame(books)
df.to_csv("books_dataset.csv", index=False, encoding="utf-8-sig")

print("\nWEB SCRAPING COMPLETED!")
print("Total books collected:", len(df))
print(df.head())
print("\nDataset saved as books_dataset.csv")


