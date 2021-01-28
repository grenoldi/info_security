from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content

soup = BeautifulSoup(site, 'html.parser')

#print(soup.prettify())

html_content = soup.find("h4", class_="-gray-dark-2 -font-base -bold")

print(html_content.string)
print(soup.title.string)
print(soup.a)