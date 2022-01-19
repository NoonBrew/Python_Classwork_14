import openpyxl
import docx
import requests
import pprint
import Workbook

country_workbook = Workbook()
country_worksheet = country_workbook.active

countries_response = requests.get('https://country-list-1150.herokuapp.com/api/country').json()

pprint.pprint(countries_response)
print(len(countries_response))

for country in countries_response:
    name = country['name']
    capital = country['capitalCity']
    print(name)
    print(capital)