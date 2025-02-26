from difflib import get_close_matches
import json

import requests
from bs4 import BeautifulSoup

with open('utils/city_links.json') as json_file:
    data = json.load(json_file)
city_list = list(data.keys())

# check if city there in citylinks
def is_station(city):
    return(city in city_list)

# get closest match
def closest_station(city):
    return(get_close_matches(city, city_list, n=10))

# get data into tables
def load_table(city):
    url = data[city]
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table_cells = soup.find_all('td')
    return(table_cells)


# get daily-data one func to:
# based on true false thingies
def get_daily(city, detailed=False):
    table_cells = load_table(city)
    daily_list = {}
    if(detailed==True):

        daily_list['max_temp'] = table_cells[4].font.text.strip()
        daily_list['max_temp_departure_from_normal'] = table_cells[6].font.text.strip()
        daily_list['min_temp'] = table_cells[8].font.text.strip()
        daily_list['min_temp_departure_from_normal'] = table_cells[10].font.text.strip()
        daily_list['24hr_rainfall'] = table_cells[12].font.text.strip()
        daily_list['total_rainfall'] = table_cells[14].font.text.strip()
        daily_list['humidity_0830'] = table_cells[16].font.text.strip()
        daily_list['humidity_1730'] = table_cells[18].font.text.strip()
        daily_list['sunset'] = table_cells[20].font.text.strip()
        daily_list['sunrise'] = table_cells[22].font.text.strip()
        daily_list['moonset'] = table_cells[24].font.text.strip()
        daily_list['moonrise'] = table_cells[26].font.text.strip()

    else:
        daily_list['max_temp'] = table_cells[4].font.text.strip()
        daily_list['min_temp'] = table_cells[8].font.text.strip()
        daily_list['total_rainfall'] = table_cells[14].font.text.strip()
        daily_list['humidity_0830'] = table_cells[16].font.text.strip()

    return(daily_list)
    

# get forecast
def get_forecast(city):
    table_cells = load_table(city)

    forecast_list = []

    for x in range(33,68,5):
        #these numbers are very prone to change 
        #imd is kind of unreliable with this 
        forec_dict = {}
        # it recursively appends into lists, change to recursively adds dicts to main list
        forec_dict['date'] = table_cells[x].font.text.strip()
        forec_dict['min_temp'] = table_cells[x+1].font.text.strip()
        forec_dict['max_temp'] = table_cells[x+2].font.text.strip()
        forec_dict['weather'] = table_cells[x+4].font.text.strip()
        forecast_list.append(forec_dict)
    return(forecast_list)