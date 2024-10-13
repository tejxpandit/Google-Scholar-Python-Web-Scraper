# Project   : Google Scholar Web Scraper in Python
# File      : Google Scholar Parser
# Author    : Tej Pandit
# Date      : Sept 2024

from bs4 import BeautifulSoup
import pickle

# Publications Format
pub = {
    'title' : '',
    'author' : '',
    'venue' : '',
    'year' : '',
    'cites' : '0',
    'page_link' : '',
    'paper_link' : '',
    'download_link' : ''
}

class GoogleScholarParser:
    def __init__(self):
        self.auth_htmls = None
        self.pub_data = None
        self.loadfile = ""
        self.savefile = ""
    
    def parseAuthData(self, auth_htmls):
        self.auth_htmls = auth_htmls
        return self.GoogleScholar_AuthorParser()
    
    def parseSavedAuthData(self, loadfile):
        self.loadfile = loadfile
        self.loadAuthFile()
        return self.GoogleScholar_AuthorParser()
    
    def parsePubData(self, pub_data):
        self.pub_data = pub_data
        return self.GoogleScholar_PublicationParser()
    
    def parseSavedPubData(self, loadfile):
        self.loadfile = loadfile
        self.loadPubFile()
        return self.GoogleScholar_PublicationParser()
    
    # Output Data Format
    # pub_data = {
    #     'author name' : [pub1, pub2, pub3.....],
    #     'author name' : [pub1, pub2, pub3.....],
    #     .....
    # }
    def GoogleScholar_AuthorParser(self):
        self.pub_data = {}
        # Extract All Pubs from HTML
        for name, html in self.auth_htmls.items():
            gsc_html = BeautifulSoup(html, 'html.parser')

            # Extract Pub Data
            pubs = []
            pub_section = gsc_html.find(id="gsc_a_b")
            # Iterate all Pub Rows
            for pub_row in pub_section.find_all('tr'):
                # Title
                pub_row_details = pub_row.find('td', {'class' : "gsc_a_t"})
                title = pub_row_details.find('a', {'class' : "gsc_a_at"})
                # Page Link
                page_link = title['href']
                # Author and Venue
                other_elements = pub_row_details.find_all('div', {'class' : "gs_gray"})
                author = other_elements[0]
                venue = other_elements[1]
                # Cites
                pub_row_cites = pub_row.find('td', {'class' : "gsc_a_c"})
                cites = pub_row_cites.find('a')
                # Year
                pub_row_year = pub_row.find('td', {'class' : "gsc_a_y"})
                year = pub_row_year.find('span')

                # Add Data to Pub Format
                p = pub.copy()
                p['title'] = title.get_text()
                p['author'] = author.get_text()
                p['venue'] = venue.get_text()
                p['year'] = year.get_text()
                p['cites'] = cites.get_text()
                p['page_link'] = page_link
                # Add Pub to Pub List
                pubs.append(p)

            # Assign All Pubs to Author Name in Output Data
            self.pub_data[name] = pubs

        return self.pub_data

    def GoogleScholar_PublicationParser(self):
        for auth, pubs in self.pub_data.items():
            for pub in pubs:
                pub_html = BeautifulSoup(pub['pub_html'], 'html.parser')
                # print(pub_html)
                pub_title = pub_html.find(id="gsc_oci_title")
                pub_link = pub_title.find('a', {'class' : "gsc_oci_title_link"})
                pub['paper_link'] = pub_link['href']
                del pub['pub_html']

        return self.pub_data

    # Load HTML from saved file
    def loadAuthFile(self):
        with open(self.loadfile, "rb") as fp:
            self.auth_htmls = pickle.load(fp)
        print('Webpage Data Loaded!\nfile-name : "' + self.loadfile + '"')
