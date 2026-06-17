# manufacturer-product-pipeline
# Manufacturer Product Update Pipeline

## Project Overview

This project is an end-to-end data engineering pipeline that extracts product information from a manufacturer-style website, cleans and standardizes the data, loads it into Snowflake, and detects product updates using snapshot-based change detection.

The goal is to simulate a real-world product monitoring system where companies need to track latest product updates, price changes, availability changes, and source-level metadata from external websites.

## Tech Stack

* Python
* Requests
* BeautifulSoup
* Pandas
* Snowflake
* SQL
* Git & GitHub
* VS Code

## Architecture

Website
→ Python Web Scraper
→ Raw CSV
→ Data Cleaning & Standardization
→ Snowflake Product Snapshot Table
→ SQL-Based Change Detection

## Features

* Extracts product data from website HTML
* Parses product name, price, availability, rating, URL, and scrape timestamp
* Handles data cleaning and type conversion
* Resolves currency formatting and encoding issues
* Loads cleaned records into Snowflake
* Maintains product snapshot history
* Detects product-level changes using SQL
* Uses Git feature-branch workflow

## Data Fields

| Column       | Description                     |
| ------------ | ------------------------------- |
| product_name | Product/book title              |
| price        | Cleaned numeric price           |
| availability | Product availability status     |
| rating       | Numeric rating                  |
| product_url  | Source product URL              |
| scraped_at   | Timestamp when data was scraped |

## Change Detection Logic

The pipeline compares the current product snapshot with historical snapshot data using `product_url` as the business key.

It identifies changes such as:

* Price updates
* Availability changes
* New or modified product records

## Key Learnings

* Web scraping using Requests and BeautifulSoup
* HTML parsing and selector identification
* Data cleaning using Pandas
* Handling encoding issues in scraped data
* Loading data into Snowflake
* Designing snapshot-based change detection
* Applying Git/GitHub workflow for project development

## Resume Summary

Built a Python-based web scraping pipeline to extract product information from external websites, clean and standardize raw scraped data, load structured records into Snowflake, and detect product updates using SQL-based snapshot comparison.
