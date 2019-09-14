# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:11:01 2019

@author: Christian
"""

import get_decklists, submit_decks


# get lists from trader website
decklists = get_decklists.main('2019-08')


# fill mtgtop8 forms
# TODO: read this also from website
event_form_data = {
        'Modern': {
                'event_title': 'Traderliga',
                'event_place': 'Dülmen',
                'event_format': 'Modern',
                'event_day': '25',
                'event_month': 'August',
                'event_year': '2019',
                'event_players': '68',
                'event_link': 'https://www.trader-online.de',
                'event_email': ''
                },
         'Legacy': {
                'event_title': 'Traderliga',
                'event_place': 'Dülmen',
                'event_format': 'Legacy',
                'event_day': '25',
                'event_month': 'August',
                'event_year': '2019',
                'event_players': '44',
                'event_link': 'https://www.trader-online.de',
                'event_email': ''
                },
         'Standard': {
                'event_title': 'Traderliga',
                'event_place': 'Dülmen',
                'event_format': 'Standard',
                'event_day': '25',
                'event_month': 'August',
                'event_year': '2019',
                'event_players': '20',
                'event_link': 'https://www.trader-online.de',
                'event_email': ''
                }
        }
         
FORMAT = 'Standard'
submit_decks.main(event_form_data[FORMAT], decklists[FORMAT])