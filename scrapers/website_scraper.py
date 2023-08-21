from .base_scraper import BaseScraper
from bs4 import BeautifulSoup
from typing import List, Dict

class WebsiteScraper(BaseScraper):
    def __init__(self, base_url: str, proxy: str = None):
        """
        Initialize the website scraper.
        
        :param base_url: The base URL of the website to scrape.
        :param proxy: Optional proxy address to use for requests.
        """
        super().__init__(base_url, proxy)
    
    
    def scrape_all_links(self) -> List[str]:
        """
        Scrape all links from the website.
        
        :return: List of all links found on the website.
        """
        endpoint = ""
        
        full_url = self.build_url(endpoint)
        
        page_content = self.fetch_page(full_url)
        
        soup = BeautifulSoup(page_content, 'html.parser')
        
        links = [link['href'] for link in soup.find_all('a', href=True)]
        
        return links


    def save_links_to_csv(self, links: List[str], filename: str) -> None:
        """
        Save list of links to a CSV file.
        
        :param links: List of links to save.
        :param filename: Name of the CSV file.
        """
        data = [{'link': link} for link in links]
        self.save_to_csv(data, filename)
