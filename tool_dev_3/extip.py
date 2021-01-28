import re
import json
from urllib.request import urlopen


url = 'https://ipinfo.io/json'

response = urlopen(url)

data = json.load(response)

ip = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

print('IP details :\nIP: {4}\nRegion: {1}\nCountry: {2}\nCity: {3}\nOrganization: {0}'.format(org, region, country, city, ip))
