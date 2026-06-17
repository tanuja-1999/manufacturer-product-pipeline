import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import pandas as pd


BASE_URL = "https://books.toscrape.com/"
OUTPUT_FILE = "data/raw_products.csv"


def scrape_products():
    response = requests.get(BASE_URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("article", class_="product_pod")

    rows = []

    for product in products:
        title = product.find("h3").find("a")["title"]
        price = product.find("p", class_="price_color").text
        availability = product.find("p", class_="instock availability").text.strip()
        rating = product.find("p", class_="star-rating")["class"][1]
        relative_url = product.find("h3").find("a")["href"]

        rows.append({
            "product_name": title,
            "price_raw": price,
            "availability_raw": availability,
            "rating_raw": rating,
            "product_url": BASE_URL + relative_url,
            "scraped_at": datetime.now(timezone.utc)
        })

    return pd.DataFrame(rows)


if __name__ == "__main__":
    df = scrape_products()
    print(df.head())
    print(f"Total products scraped: {len(df)}")
    df.to_csv(OUTPUT_FILE, index=False)