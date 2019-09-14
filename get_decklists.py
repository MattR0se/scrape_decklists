# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:12:37 2019

@author: Christian
"""

from webscrape import simple_get
from bs4 import BeautifulSoup
import numpy as np
from time import sleep
from os import path, mkdir


def get_html(url):
    # requests url and returns a bs4 html object
    raw_html = simple_get(url)
    if raw_html:
        return BeautifulSoup(raw_html, 'html.parser')
    else:
        print(f'Parsing {url} failed')
        return None


def extract_decks(format_, urls, deck_dict):
    deck_dict[format_] = []
    deck_urls = []

    for url in urls:
        decklist_page1 = get_html(url)
        deck_urls += [u['src'] for u in decklist_page1.select('frame')]
    
    
    for url in deck_urls:
        print(f'reading {url}...')
        sleep(1)
        deck = get_html(f'https://www.trader-online.de/turniere/Decks/{url}')
        
        dname = deck.select('head')[0]['data-deckname']
        dfirstname = deck.select('head')[0]['data-firstname']
        dlastname = deck.select('head')[0]['data-lastname']
        drank = int(deck.select('head')[0]['data-rank'])
        date = deck.select('head')[0]['data-date']
        
        dlist = deck.select('td')[5]
        card_names = []
        card_quantities = []
        for i, tag in enumerate(dlist.select('td')):
            if i <= 1:
                # skip title
                continue
            if i % 2 == 0:
                try:
                    card_quantities.append(tag.text[0])
                except ValueError:
                    card_quantities.append(np.nan)
            else:
                card_names.append(tag.text.replace('\n', ''))
        
        # format deck string for mtgtop8 form
        decklist_t = tuple(zip(card_quantities, card_names))
        decklist_s = ''
        for pair in decklist_t:
            if pair[1] == 'Sideboard':
                decklist_s += 'Sideboard\n'
            else:
                decklist_s += (' ').join(pair)
                decklist_s += '\n'
        
        deck_dict[format_].append({
                'Title': dname, 
                'Player': f'{dfirstname} {dlastname}', 
                'Rank': drank,
                'Cards': decklist_s})

        # export to txt files
        # create folder if it not exists
        folder = path.join('exported_lists', f'{date}')
        if not path.exists(folder):
            mkdir(folder)
        filename = f'{drank}_{dfirstname}_{dlastname}.txt'
        with open(path.join(folder, filename), 'w') as f:
            f.write(decklist_s)
        

def main(date):
    '''
    Args:
        date: string - format: YYYY-MM
    '''
    decklists = {}
    
    url_lib  = {
            'Modern': [
                    f'https://www.trader-online.de/turniere/Decks/{date}-T5.html',
                    f'https://www.trader-online.de/turniere/Decks/{date}-X5.html'
                    ],
            'Standard': [
                    f'https://www.trader-online.de/turniere/Decks/{date}-T2.html',
                    f'https://www.trader-online.de/turniere/Decks/{date}-X2.html'
                    ],
            'Legacy': [
                    f'https://www.trader-online.de/turniere/Decks/{date}-T15.html',
                    f'https://www.trader-online.de/turniere/Decks/{date}-X15.html'
                    ]
            }
    
    for f in ['Modern', 'Standard', 'Legacy']:
        extract_decks(f, url_lib[f], decklists)
    
    return decklists



if __name__ == '__main__':
    lists = main('2019-08')

