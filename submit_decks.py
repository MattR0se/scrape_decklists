# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:28:39 2019

@author: Christian
"""

from selenium import webdriver
from selenium.common.exceptions import (ElementNotInteractableException,
                                        InvalidElementStateException)
from time import sleep


def main(event_form_data, decklists):
    driver = webdriver.Firefox(executable_path=r'webdriver/geckodriver.exe')
    
    url = 'https://www.mtgtop8.com/submit_event'
    driver.get(url)
    
    for key, value in event_form_data.items():
        form = driver.find_element_by_name(key)
        try:
            form.clear()
        except InvalidElementStateException:
            pass
        form.send_keys(value)
        sleep(1)
    
    for i, decklist in enumerate(decklists):
        player_form_data = {
                f'titre[{i+1}]': decklist['Title'],
                f'player[{i+1}]': decklist['Player'],
                f'rank[{i+1}]': decklist['Rank'],
                f'deck_cards[{i+1}]': decklist['Cards']
                }
        
        # fill deck forms
        for key, value in player_form_data.items():
            sleep(1)
            try:
                textarea = driver.find_element_by_name(key)
                textarea.send_keys(value)
            except ElementNotInteractableException:
                div = driver.find_element_by_id(f'decklist_edit_{i+1}')
                div.click()
                div.send_keys(value)
