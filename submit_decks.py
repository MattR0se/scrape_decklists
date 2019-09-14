# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:28:39 2019

@author: Christian
"""

from selenium import webdriver
from time import sleep

import json


driver = webdriver.Firefox(executable_path=r'webdriver/geckodriver.exe')

url = 'https://www.mtgtop8.com/submit_event'
driver.get(url)


# load decklists
# TODO: remove after testing (access decklists as an argument for main())
with open('decklists_modern.json', 'r') as f:
    decklists = json.load(f)


event_form_data = {
        'event_title': 'Traderliga',
        'event_place': 'Dülmen',
        'event_link': 'https://www.trader-online.de',
        'event_email': 'chr.post@gmx.net'
        }



for key, value in event_form_data.items():
    form = driver.find_element_by_name(key)
    form.send_keys(value)
    sleep(1)


for i, decklist in enumerate(decklists):
    player_form_data = {
            f'titre[{i+1}]': decklist['Title'],
            f'player[{i+1}]': decklist['Player'],
            f'deck_cards[{i+1}]': decklist['Cards']
            }
    
    # fill deck forms
    for key, value in player_form_data.items():
        sleep(1)
        textarea = driver.find_element_by_name(key)
        textarea.send_keys(value)