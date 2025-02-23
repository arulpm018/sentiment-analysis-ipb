import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# Load CSV containing links
input_csv = "output/IPB/kompas/links/links.csv"  # Update with your actual file path
output_csv = "scraped_articles.csv"

df = pd.read_csv(input_csv)

# Function to extract date from URL (YYYY/MM/DD format)
def extract_date_from_url(url):
    match = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', url)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    return "No Date"

# Function to scrape title and main content from a specific div/article
def scrape_article(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise error for HTTP errors
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract title
        title = soup.find("h1", class_='read__title').text.strip() if soup.find("title") else "No Title"

        # Extract main content from specific div
        content_div = soup.find("div", class_="read__content")  # Change this for other sites
        if content_div:
            paragraphs = content_div.find_all("p")
            content = " ".join(p.text.strip() for p in paragraphs)
        else:
            content = "No content found"

        # Extract date from URL
        date = extract_date_from_url(url)

        return {"Title": title, "Content": content, "Date": date}

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return {"Title": "Error", "Content": "Error", "Date": extract_date_from_url(url)}

# Scrape all articles
articles = []
for link in tqdm(df["link"], desc="Scraping articles"):
    article_data = scrape_article(link)
    article_data["URL"] = link  # Add URL for reference
    articles.append(article_data)

# Save results to CSV
output_df = pd.DataFrame(articles)
output_df.to_csv(output_csv, index=False)

print(f"Done! Scraped data saved to {output_csv}")
