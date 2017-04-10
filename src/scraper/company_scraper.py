__author__ = 'Cameron'

from bs4 import BeautifulSoup
import bs4

import scraper_utilities as su
from src.scraper.company import Company


"""
We want to collect:
    Founder(s)
    Owner
    Traded as
    Industry
    Revenue
    Operating Income
    Net Income
    Total Assets
    Total equity
    * Determine increase or decrease for above 5
    Employees
    Subsidiaries
    Website
"""

def build_company_data(data, company_name = "", symbol="", link=""):
    soup = BeautifulSoup(data, "html.parser")
    infobox = soup.find("table", { "class" : "infobox"} )
    if not infobox:
        return None
    founder = get_founder(infobox)
    #print(founder)
    owner = get_owner(infobox)
    #print(owner)
    traded_as = get_traded_as(infobox)
    #print(traded_as)
    industry = get_industry(infobox)
    #print(industry)
    revenue = get_revenue(infobox)
    #print(revenue)
    operating_income = get_operating_income(infobox)
    # print(operating_income)
    net_income = get_net_income(infobox)
    #print(net_income)
    total_assets = get_total_assets(infobox)
    #print(total_assets)
    total_equity = get_total_equity(infobox)
    #print(total_equity)
    employees = get_employees(infobox)
    #print(employees)
    subsidiaries = get_subsidiaries(infobox)
    #print(subsidiaries)
    website = get_website(infobox)
    #print(website)
    company = Company(company_name, symbol, link, founder, owner, traded_as, industry, revenue, operating_income,\
                      net_income, total_assets, total_equity, employees, subsidiaries,\
                      website)
    #print(company)
    return company

def get_founder(infobox):
    """
    Gets the founder from the infobox of the company's Wiki page
    :param infobox: The infobox to search through
    :return: None if not found, otherwise the value
    """
    return get_row_from_infobox(infobox, 'founder')

def get_owner(infobox):
    """
    Gets the owner from the infobox of the company's Wiki page
    :param infobox: The infobox to search through
    :return: None if not found, otherwise the value
    """
    return get_row_from_infobox(infobox, 'owner')


def get_traded_as(infobox):
    """
    Gets the traded as value from the infobox of the company's Wiki page
    :param infobox: The infobox to search through
    :return: None if not found, otherwise the value
    """
    return get_row_from_infobox(infobox, 'traded')

def get_industry(infobox):
    """
    Gets the industry from the infobox of the company's Wiki page
    :param infobox: The infobox to search through
    :return: None if not found, otherwise the value
    """
    return get_row_from_infobox(infobox, 'industry')


def get_revenue(infobox):
    """
    Gets the revenue from the infobox of the company's Wiki page
    :param infobox: The infobox to search through
    :return: None if not found, otherwise the value and its direction
    """
    return get_row_from_infobox(infobox, 'revenue')

def get_operating_income(infobox):
    """
    Gets the operating income from the infobox of the company's Wiki page
    :param infobox: The infobox to search through
    :return: None if not found, otherwise the value and its direction
    """
    return get_row_from_infobox(infobox, 'operating')

def get_net_income(infobox):
    """
    Gets the net income from the infobox of the company's Wiki page
    :param infobox: The infobox to search through
    :return: None if not found, otherwise the value and its direction
    """
    return get_row_from_infobox(infobox, 'net income')


def get_total_assets(infobox):
    """
    Gets the founder from the infobox of the company's Wiki page
    :param infobox: The infobox to search through
    :return: None if not found, otherwise the value
    """
    return get_row_from_infobox(infobox, 'total assets')

def get_total_equity(infobox):
    """
    Gets the total_equity from the infobox of the company's Wiki page
    :param infobox: The infobox to search through
    :return: None if not found, otherwise the value and its direction
    """
    return get_row_from_infobox(infobox, 'total equity')

def get_employees(infobox):
    """
    Gets the employees from the infobox of the company's Wiki page
    :param infobox: The infobox to search through
    :return: None if not found, otherwise the value
    """
    return get_row_from_infobox(infobox, 'employees')

def get_subsidiaries(infobox):
    """
    Gets the subsidiary companies from the infobox of the company's Wiki page
    :param infobox: The infobox to search through
    :return: None if not found, otherwise the value
    """
    return get_row_from_infobox(infobox, 'subsidiaries')

def get_website(infobox):
    """
    Gets the website from the infobox of the company's Wiki page
    :param infobox: The infobox to search through
    :return: None if not found, otherwise the value
    """
    return get_row_from_infobox(infobox, 'website')

def get_row_from_infobox(infobox, value):
    """
    Gets the value from the infobox of the company's Wiki page
    :param infobox: The infobox to search through
    :return: None if not found, otherwise the value
    """
    ret = "Not Found"
    for content in infobox.contents:
        if type(content) is bs4.element.Tag:
            name = content.find('th')
            if name is None:
                continue
            else:
                if value in name.text.lower():
                    ret = content.find('td').text
                    ret = su.clean_string(ret)
                    return ret
    return ret


# data = su.get_html_from_url("https://en.wikipedia.org/wiki/Advanced_Micro_Devices")
# build_company_data(data)