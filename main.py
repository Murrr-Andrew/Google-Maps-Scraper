from scrapers.website_scraper import WebsiteScraper

def main():
    base_url = ''
    proxy = ''
    
    scraper = WebsiteScraper(base_url, proxy)
    
    links = scraper.scrape_all_links()
    scraper.save_links_to_csv(links, "data/scraped_links.csv")
    
    scraper.close()

if __name__ == '__main__':
    main()
