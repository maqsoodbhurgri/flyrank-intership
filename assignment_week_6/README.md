# Week 6 Assignment - Ethical Web Scraper

## Project Overview

This project demonstrates the complete web scraping pipeline:

**Fetch → Parse → Extract → Clean → Structure → Store**

The scraper collects book information from the practice website:

https://books.toscrape.com

The extracted data is cleaned and stored in structured formats (JSON and CSV) for future use in Retrieval-Augmented Generation (RAG) applications.

---

## Objective

* Learn professional web scraping practices.
* Understand HTML parsing and data extraction.
* Build structured datasets from web pages.
* Prepare a corpus that can later be used for AI and RAG systems.

---

## Target Website

Website:

https://books.toscrape.com

This website is intentionally created for scraping practice and contains approximately **1000 books across 50 pages**.

---

## Ethical Considerations

Before scraping, the website's robots file was checked:

```text
https://books.toscrape.com/robots.txt
```

Result:

```text
404 Not Found
```

No explicit crawling restrictions were provided.

Professional scraping practices followed:

* Custom User-Agent header
* Low request rate (1 request per second)
* Educational purpose only
* No excessive requests or aggressive crawling

---

## Technologies Used

* Python 3
* Requests
* BeautifulSoup4
* Pandas
* JSON
* Regular Expressions (re)

---

## Installation

Clone repository:

```bash
git clone https://github.com/maqsoodbhurgri/flyrank-intership.git
cd flyrank-intership/assignment_week_6
```

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
python scraper.py
```

---

## Extracted Fields

Each record contains:

| Field        | Description                       |
| ------------ | --------------------------------- |
| title        | Book title                        |
| price        | Book price                        |
| availability | Stock availability                |
| rating       | Rating converted to numeric value |

Example:

```json
{
    "title": "A Light in the Attic",
    "price": 51.77,
    "availability": "In stock",
    "rating": 3
}
```

---

## Project Structure

```text
assignment_week_6/
│
├── scraper.py
├── books.json
├── books.csv
├── requirements.txt
├── README.md
└── venv/
```

---

## Output Files

### books.json

Structured JSON dataset.

### books.csv

Tabular dataset suitable for analysis and machine learning workflows.

---

## Future Scope

This dataset can be used as a knowledge corpus for:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embedding Pipelines
* AI Chatbots
* Data Analysis Projects

---
