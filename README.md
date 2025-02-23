# Sentiment Analysis of IPB-Related News on Kompas

This project focuses on web scraping and sentiment analysis of news articles related to IPB (Institut Pertanian Bogor) from Kompas. The scraped articles are then analyzed using a Hugging Face model for sentiment classification.

## Project Structure

```
📂 sentiment_analysis_newsipb_kompas
│── scrapping.py          # Scrapes news article links from Kompas
│── extract.py            # Extracts content from the collected news links
│── sentiment_analysis_newsipb_kompas.ipynb  # Performs sentiment analysis
│── output/               # Directory to store scraped data and results
│   ├── links.csv
│   ├── scraped_articles.csv # Extracted article contents
```

## Installation

Ensure you have Python 3.7+ installed. Install the required dependencies using:

```bash
pip install -r requirements.txt
```

(*Create a `requirements.txt` file if necessary*)

## Usage

1. **Scrape Links**  
   Run `scrapping.py` to collect article URLs related to IPB from Kompas:

   ```bash
   python scrapping.py
   ```

   This will save the links in `output/IPB/kompas/links/links.csv`.

2. **Extract Article Content**  
   Run `extract.py` to scrape article titles and content:

   ```bash
   python extract.py
   ```

   This will save the extracted data in `scraped_articles.csv`.

3. **Perform Sentiment Analysis**  
   Open `sentiment_analysis_newsipb_kompas.ipynb` and execute the notebook to analyze the sentiment of the collected articles.

## Features

- **Automated Web Scraping**: Collects news articles dynamically.
- **Content Extraction**: Extracts titles, content, and publication dates.
- **Sentiment Analysis**: Uses a Hugging Face model to classify article sentiment.

## Notes

- Modify `scrapping.py` to change the source website or scraping depth.
- Update `extract.py` if the website structure changes.
- Ensure compliance with Kompas' terms of service before scraping.

## License

This project is for educational purposes. Follow ethical scraping practices.

---
Developed by Hasrul Malik Putra Mashun

