# Project   : Google Scholar Web Scraper in Python
# File      : Google Scholar Scraper
# Author    : Tej Pandit
# Date      : Sept 2024

import pickle
from util.WebpageScraper import WebpageScraper
from GoogleScholarParser import GoogleScholarParser

# Import Data 
from GoogleScholar_URLs import URLs

class GoogleScholarScraper:
    def __init__(self):
        self.scraper = None
        self.parser = None
        self.auth_urls = URLs
        self.auth_htmls = None
        self.pub_data = None
        self.googlescholar_baseURL = "https://scholar.google.com/"