import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_links(base_url, container_selector, tag_name, max_pages):
    all_links = set()
    
    for page_number in range(1, max_pages + 1):
        url = base_url.format(page_number=page_number)
        print(f"Scraping page {page_number}: {url}")
        
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            print(f"Failed to retrieve page {page_number}, status code: {response.status_code}")
            continue
        
        soup = BeautifulSoup(response.text, "html.parser")
        containers = soup.select(container_selector)
        
        for container in containers:
            links = container.find_all(tag_name, href=True)
            for link in links:
                all_links.add(link["href"])
        
        print(f"Scraped {len(links)} links from page {page_number}. Total: {len(all_links)}")

    return all_links

def save_links(links, folder, subfolder, filename):
    save_path = os.path.join(os.getcwd(), f"output/{folder}", subfolder)
    os.makedirs(save_path, exist_ok=True)
    csv_file_path = os.path.join(save_path, filename)
    
    df = pd.DataFrame(links, columns=["link"])
    df.to_csv(csv_file_path, index=False)
    print(f"Data saved to {csv_file_path}")

if __name__ == "__main__":
    base_url = "https://www.kompas.com/tag/ipb?page={page_number}"
    container_selector = "body > div.wrap > div.container.clearfix > div> div.col-bs10-7 > div.latest.ga--latest.mt2.clearfix.-newlayout > div > div.article__list__title > h3"  # Adjust as needed
    tag_name = "a"
    max_pages = 1

    all_links = scrape_links(base_url, container_selector, tag_name, max_pages)

    df = pd.DataFrame(all_links, columns=["link"])
    df.to_csv("links.csv", index=False)
    print("Scraping complete.")
