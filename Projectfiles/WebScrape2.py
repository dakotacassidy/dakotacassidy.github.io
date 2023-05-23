# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 20:40:23 2022

@author: cococ
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

our_url = 'https://www.nordstrom.com/browse/kids/baby-gear/strollers?breadcrumb=Home%2FKids%2FBaby%20Gear%20%26%20Essentials%2FStrollers&origin=topnav'

url_start = 'https://www.nordstrom.com/browse/kids/baby-gear/strollers?breadcrumb=Home%2FKids%2FBaby%20Gear%20%26%20Essentials%2FStrollers&origin=topnav&page='
url_end = '&sort=Boosted'
stroller_page = requests.get(our_url)

stroller_info = []

for page_number in range(1,7):
    url = url_start + str(page_number) + url_end
    stroller_page = requests.get(url)
    nordstrom_strollers = BeautifulSoup(stroller_page.content, 'html.parser')
    strollers = nordstrom_strollers.find_all('div', class_ = "gFaKF _3jNIn _36liS _1GUt4")

    for stroller in strollers:
        stroller_name = stroller.find('h3', class_= "_1B5Va _2Gi1Y").text
        stroller_price = stroller.find('div', class_= "_3bxjM _2cxHg _2_z5L").text
        stroller_info.append({"Name": stroller_name, "Price" : stroller_price})
       

stroller_data = pd.DataFrame(stroller_info)
stroller_data.to_csv('C:/Users/cococ/OneDrive/Documents/stroller_data.csv')