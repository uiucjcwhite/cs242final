__author__ = 'Cameron'

import json
class Company:
    def __init__(self, name, symbol, link, founder, owner, traded_as, industry, revenue, operating_income,\
                 net_income, total_assets, total_equity, employees, subsidiaries, website):
        self.name = name
        self.symbol = symbol
        self.link = link
        self.founder = founder
        self.owner = owner
        self.traded_as = traded_as
        self.industry = industry
        self.revenue = revenue
        self.operating_income = operating_income
        self.net_income = net_income
        self.total_assets = total_assets
        self.total_equity = total_equity
        self.employees = employees
        self.subsidiaries = subsidiaries
        self.website = website

    def __str__(self):
        """
        For printing out a company object
        :return:
        """
        return "Name: " + self.name + "\n" +\
              "Abrev: " + self.symbol + '\n' +\
              "Founder: " + self.founder + "\n" +\
              "Owner: " + self.owner + "\n" +\
              "Traded As: " + self.traded_as + "\n" +\
              "Industry: " + self.industry + "\n" +\
              "Revenue: " + self.revenue + "\n" +\
              "Operating Income: " + self.operating_income + "\n" +\
              "Net Income: " + self.net_income + "\n" +\
              "Total Assets: " + self.total_assets + "\n" +\
              "Total Equity: " + self.total_equity + "\n" +\
              "Employees: " + self.employees + "\n" +\
              "Subsidiaries: "+ self.subsidiaries + "\n" +\
              "Website: " + self.website + "\n"

    def company_to_json(self):
        return json.dumps(self.__dict__)