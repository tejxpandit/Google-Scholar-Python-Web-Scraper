# Project   : Google Scholar Web Scraper in Python
# File      : Google Scholar Parser
# Author    : Tej Pandit
# Date      : Sept 2024

from bs4 import BeautifulSoup
import pickle

class GoogleScholarParser:
    def __init__(self):
        self.auth_htmls = None
        self.pub_data = None
        self.loadfile = ""
        self.savefile = ""
    