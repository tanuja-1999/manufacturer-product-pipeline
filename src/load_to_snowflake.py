import os
import pandas as pd
import snowflake.connector 
from dotenv import load_dotenv

load_dotenv()
 
INPUT_FILE = "data/clean_products.csv"


def get_snowflake_connection():
    return snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
        role=os.getenv("SNOWFLAKE_ROLE"),
    )


def load_products_to_snowflake():
    df = pd.read_csv(INPUT_FILE)

    conn = get_snowflake_connection()
    cursor = conn.cursor()

    insert_sql = """
        INSERT INTO PRODUCT_SNAPSHOTS
        (
            PRODUCT_NAME,
            PRICE,
            AVAILABILITY,
            RATING,
            PRODUCT_URL,
            SCRAPED_AT
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    rows = [
        (
            row["product_name"],
            row["price"],
            row["availability"],
            int(row["rating"]),
            row["product_url"],
            row["scraped_at"],
        )
        for _, row in df.iterrows()
    ]

    cursor.executemany(insert_sql, rows)

    conn.commit()
    cursor.close()
    conn.close()

    print(f"Loaded {len(rows)} records into Snowflake.")


if __name__ == "__main__":
    load_products_to_snowflake()