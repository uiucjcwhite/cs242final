__author__ = 'Cameron'

import time

from bs4 import BeautifulSoup
import bs4
from pymongo import MongoClient
import scraper_utilities
import company_scraper


SP_LINK = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
BASE_LINK = "https://en.wikipedia.org"
COMPANY_DB_URL = "mongodb://username:password@ds157380.mlab.com:57380/cs242final"
CLIENT = MongoClient(COMPANY_DB_URL)
COMPANY_DB = CLIENT.cs242final.companies

def scrape_sp_list(html):
    """
    Scrapes 500 companies from the S&P 500 list. Needs more error checking
    Determines if companies need to be scraped or not
    :param html: html of the wiki page
    :return: Nothing
    """
    html = scraper_utilities.get_html_from_url(html)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", { "class" : "wikitable sortable"})
    rows = table.find_all("tr")
    rows = rows[1:]
    for row in rows:
        symbol = ""
        link = ""
        company_name = ""
        for i in range(len(row.contents)):
            if type(row.contents[i]) is bs4.element.Tag:
                if i == 1:
                    symbol = row.contents[i].text
                elif i == 3:
                    company_name = row.contents[i].text
                    link = BASE_LINK + row.contents[i].find('a', href=True)["href"]
        if link:
            data = scraper_utilities.get_html_from_url(link)
            if data:
                company = company_scraper.build_company_data(data, company_name, symbol, link)
                if company:
                    company_json = company.company_to_json()
                    print(company_json)
                    if "." in company_name:
                        company_name = company_name.replace(".", "#")
                    lookup = COMPANY_DB.find({company_name : {'$exists' : True}})
                    if lookup.count == 0:
                        COMPANY_DB.insert_one({company_name : company_json})
                    else:
                        COMPANY_DB.update({company_name : {'$exists' : True}}, {company_name : company_json})
        time.sleep(.75)


scrape_sp_list(SP_LINK)