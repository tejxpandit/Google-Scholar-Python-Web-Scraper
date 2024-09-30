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

    # Initialize Custom Web Scraper Class
    def initializeWebScraper(self):
        webScraper = WebpageScraper()
        webScraper.enableSave()
        webScraper.enableWait()
        webScraper.setWaitTime(1)
        webScraper.disableLog()
        self.scraper = webScraper

    # Initialize Custom Web Parser Class
    def initializeWebParser(self):
        webParser = GoogleScholarParser()
        self.parser = webParser
    