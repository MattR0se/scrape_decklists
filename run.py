# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:11:01 2019

@author: Christian
"""

import get_decklists, submit_decks
from calendar import month_name


# get lists from trader website
decklists = get_decklists.main('2019-09')

# get date from decklist
date_string = decklists['Modern'][0]['Date']
year, month, day = date_string.split('-')
month = month_name[int(month)]

# fill mtgtop8 forms
# TODO: read this also from website?
event_form_data = {
        'Modern': {
                'event_title': 'Traderliga',
                'event_place': 'Dülmen',
                'event_format': 'Modern',
                'event_day': day,
                'event_month': month,
                'event_year': year,
                'event_players': '60',
                'event_link': 'https://www.trader-online.de',
                'event_email': ''
                },
         'Legacy': {
                'event_title': 'Traderliga',
                'event_place': 'Dülmen',
                'event_format': 'Legacy',
                'event_day': day,
                'event_month': month,
                'event_year': year,
                'event_players': '25',
                'event_link': 'https://www.trader-online.de',
                'event_email': ''
                },
         'Standard': {
                'event_title': 'Traderliga',
                'event_place': 'Dülmen',
                'event_format': 'Standard',
                'event_day': day,
                'event_month': month,
                'event_year': year,
                'event_players': '16',
                'event_link': 'https://www.trader-online.de',
                'event_email': ''
                }
        }


for format_, data in event_form_data.items():
    submit_decks.main(data, decklists[format_])