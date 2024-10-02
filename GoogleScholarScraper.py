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
    
    # Google Scholar Scrape Authors
    def GoogleScholar_ScrapeAuthors(self):
        self.scraper.setSaveFilename("data\gsc_auth_html")
        try:
            self.auth_htmls = self.scraper.getHTMLDict(self.auth_urls)
        except:
            self.auth_htmls = [""]
        # getHTMLDict --> {"auth name 1" : str(html), "auth name 2" : str(html),....}
        # print(self.auth_htmls)

    # Google Scholar Parse Author Publications
    def GoogleScholar_ParseAuthorPubs(self):
        # self.parser.parseAuthData(self.auth_htmls)
        self.pub_data = self.parser.parseSavedAuthData("data\gsc_auth_html")
        # parsePubData --> {"auth name 1" : [pub1, pub2, pub3.....], "auth name 2" : [pub1, pub2, pub3.....],....}
        # pub_format = {
        #     'title' : '',
        #     'author' : '',
        #     'venue' : '',
        #     'year' : '',
        #     'cites' : '',
        #     'page_link' : '',
        #     'paper_link' : '',
        #     'download_link' : ''
        # }
        # Example : print(self.pub_data['Tej Pandit'][5]['title'])
        # print(self.pub_data)

    # Google Scholar Scrape Publication Page
    def GoogleScholar_ScrapePubPage(self):
        self.scraper.disableSave()
        for auth, pubs in self.pub_data.items():
            for pub in pubs:
                try:
                    pub_html = self.scraper.getHTML(self.googlescholar_baseURL + pub['page_link'])
                except:
                    pub_html = ""
                # getHTML --> str(html)
                pub['pub_html'] = pub_html
        # Save the Data File with Pub HTMLs
        # print(self.pub_data)
        self.savePubDataFile("data\gsc_pub_html")

    # Google Scholar Parse Publication Page
    def GoogleScholar_ParsePubPage(self):
        self.parser.pub_data = self.pub_data
        # self.parser.parsePubData(self.auth_htmls)
        self.pub_data = self.parser.parseSavedPubData("data\gsc_pub_html")
        # parsePubData --> {"auth name 1" : [pub1, pub2, pub3.....], "auth name 2" : [pub1, pub2, pub3.....],....}
        # pub_format = {
        #     'title' : '',
        #     'author' : '',
        #     'venue' : '',
        #     'year' : '',
        #     'cites' : '',
        #     'page_link' : '',
        #     'paper_link' : '',
        #     'download_link' : '',
        #     'pub_html' : ''
        # }
        # Example : print(self.pub_data['Tej Pandit'][5]['pub_html'])
        # print(self.pub_data)