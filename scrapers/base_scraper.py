import csv
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from typing import List, Dict
import requests


class BaseScraper:
    def __init__(self, base_url: str, proxy: str = None) -> None:
        """
        Initialize the base scraper.
        
        :param base_url: The base URL of the website to scrape.
        :param proxy: Optional proxy address to use for requests.
        """
        self.base_url = base_url
        
        if proxy:
            self.driver = self._init_driver_with_proxy(proxy)
        else:
            self.driver = webdriver.Chrome()
    
    
    def _init_driver_with_proxy(self, proxy: str) -> webdriver.Chrome:
        """
        Initialize the Selenium WebDriver with a proxy.
        
        :param proxy: The proxy address to use.
        :return: Initialized WebDriver instance.
        """
        proxy_settings = Proxy()
        proxy_settings.proxy_type = ProxyType.MANUAL
        proxy_settings.http_proxy = proxy
        proxy_settings.ssl_proxy = proxy
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % proxy)
        
        return webdriver.Chrome(chrome_options=chrome_options)


    def fetch_page(self, url: str) -> str:
        """
        Fetch the HTML content of a webpage.
        
        :param url: The URL of the webpage to fetch.
        :return: HTML content of the webpage.
        """
        response = requests.get(url)
        response.raise_for_status()
        return response.text


    def build_url(self, endpoint: str) -> str:
        """
        Construct the full URL by combining the base URL and endpoint.
        
        :param endpoint: The endpoint to append to the base URL.
        :return: The complete URL.
        """
        return f'{self.base_url}/{endpoint}'
    
    
    def save_to_csv(self, data: List[Dict[str, str]], filename: str) -> None:
        with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data[0].keys())
            for item in data:
                csv_writer.writerow(item.values())

    
    def close(self) -> None:
        """
        Close the WebDriver instance.
        """
        self.driver.quit()
