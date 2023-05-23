# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 20:12:42 2022

@author: cococ
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

our_url = 'https://careers.google.com/jobs/results/#modal_open'
career_page = requests.get(our_url)

google_careers = BeautifulSoup(career_page.content, 'html.parser')

careers = google_careers.find_all('a', class_ = "gc-card")

career_info = []

for career in careers:
    try:
        career_name = career.find('h2', class_= "gc-card__title gc-heading gc-heading--beta").text
        career_description = career.find('meta', itemprop= "description").text
        career_info.append({"Job Title": career_name, "Description" : career_description})
    except:
        continue

career_data = pd.DataFrame(career_info)
career_data.to_csv('C:/Users/cococ/OneDrive/Documents/career_data.csv')
                            