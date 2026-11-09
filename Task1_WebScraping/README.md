# Task 1 - Web Scraping

## Project Overview
This project collects book information from the public Books to Scrape website using Python web scraping.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- Pandas

## Data Collected
The scraper collects:
- Book Title
- Price
- Star Rating
- Availability
- Product URL

## Dataset
The scraper visits all 50 catalogue pages and collects 1,000 book records.

Output file: books_dataset.csv

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run the scraper:
   python scraper.py

## Output
The scraped data is saved in books_dataset.csv.
