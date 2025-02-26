import json
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup

main_url = 'https://city.imd.gov.in/citywx/menu_test.php##'
response = requests.get(main_url)
soup = BeautifulSoup(response.text, 'html.parser')

all_states = soup.find_all('a', attrs={'target':'mainframe'})

city_link_dict = {}
for i in all_states:
    #https://city.imd.gov.in/citywx/
    if(i['href']!=None and i.text!=''):
        city_link_dict[i.text.lower().rstrip(" ")] = "https://city.imd.gov.in/citywx/"+i['href']
#print(city_link_dict)
with open("/city_links.json", "w") as outfile:
    json.dump(city_link_dict, outfile, indent=4)