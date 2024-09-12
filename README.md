/*
# Web Scraper for Saansha Artworks on Amazon

## Project Overview

This web scraper was somthing i built in college second year  to track the price and sales data for Saansha Artworks products on Amazon. By scraping product listings, it retrieves customer reviews and ranks the product in its respective category. This helps monitor the product's performance over time.

## Features

- Scrapes Amazon product details such as ratings and sales rank.
- Logs the scraped data (ratings, rank, and timestamp) into a CSV file.
- Data can be used to analyze trends over time for better business decision-making.

## Tech Stack

- **Python**: Core language used for building the scraper.
- **BeautifulSoup**: For parsing the HTML structure of the Amazon product page.
- **CSV**: For storing the scraped data in a structured format.

## Code Overview

### Main Code Snippet

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
from csv import writer
import re
import time
from datetime import datetime
import pytz

IST = pytz.timezone('Asia/Kolkata')
i = 0
i = i + 1

# URL of the product page to scrape
u = "https://www.amazon.in/Planner-Organiser-Illustrated-Planning-Calendar/dp/B08NZGGKTF/ref=sr_1_3?keywords=the+super+ultra+mega+planner+2022&qid=1640110651&sprefix=super+ultra+mega%2Caps%2C227&sr=8-3"

# Opening the URL
page = urlopen(u)
soup = BeautifulSoup(page, "html.parser")

# Extracting ratings and rank
title = soup.select('#acrCustomerReviewText , #productDetails_detailBullets_sections1 span span:nth-child(3)')
x = [span.text for span in title]
ratings = int(x[0][:3])
rank = int(re.findall('[0-9]+', x[2])[0])

# Creating a list to store scraped data
List = [i, datetime.now(IST), ratings, rank]

# Appending data to CSV
with open('Data.csv', 'a', newline='') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(List)
    f_object.close()
