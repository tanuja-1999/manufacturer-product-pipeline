import pandas as pd


INPUT_FILE = "data/raw_products.csv"
OUTPUT_FILE = "data/clean_products.csv"


RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def clean_products():
    df = pd.read_csv(INPUT_FILE)

    df["price"] = (
    df["price_raw"]
    .str.extract(r"(\d+\.\d+)")[0]
    .astype(float)
)

    df["rating"] = df["rating_raw"].map(RATING_MAP)

    df["availability"] = (
        df["availability_raw"]
        .str.replace("\n", "", regex=False)
        .str.strip()
    )

    df = df[
        [
            "product_name",
            "price",
            "availability",
            "rating",
            "product_url",
            "scraped_at"
        ]
    ]

    df = df.drop_duplicates(subset=["product_name", "product_url"])

    return df


if __name__ == "__main__":
    clean_df = clean_products()
    print(clean_df.head())
    print(f"Total cleaned products: {len(clean_df)}")
    clean_df.to_csv(OUTPUT_FILE, index=False)