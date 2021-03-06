import requests
import lxml
from bs4 import BeautifulSoup as bsp

web_page_html = requests.get('https://www.worldstandards.eu/other/tlds/').text
web_page = bsp(web_page_html,'html.parser')


# print(web_page.find_all(class_ = 'table table-striped'))
table = web_page.find_all(class_ = 'table table-striped')[0]
print(type(table))
print(len(web_page.find_all(class_ = 'table table-striped')))
list_data = table.findAll('td')
with open('./data/country_domain.csv',mode='w+') as file:
    for index, item in enumerate(list_data):
        if index % 2 == 0:
            file.write(item.text + ', ')
        else:
            file.write(item.text + '\n')


# for table in web_page.find_all(class_ = 'table table-striped'):
#     table.tbody.