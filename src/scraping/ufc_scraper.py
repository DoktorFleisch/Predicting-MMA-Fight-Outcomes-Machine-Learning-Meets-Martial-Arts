import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "http://ufcstats.com/statistics/events/completed?page={}" #use .format to get the page

def get_event_links(pages=2, delay=1):
    all_event_links = []

    for page in range(1, pages+1):
        URL = BASE_URL.format(page)
        request = requests.get(URL)
        soup = BeautifulSoup(request.content, 'html.parser')

        links = soup.select('a.b-link')

        event_links = [link['href'] for link in links if 'href' in link.attrs]
        all_event_links.extend(event_links)

        time.sleep(delay)

    return all_event_links

def get_fighting_links(event_link, delay=1):
    fighting_links = []

    request = requests.get(event_link)
    soup = BeautifulSoup(request.content, 'html.parser')

    links = soup.select('a.blink')

    fighting_links = [link['href'] for link in links if 'href' in link.attrs]

    return fighting_links

def get_fighting_data(fight_link):
    request = requests.get(fight_link)
    soup = BeautifulSoup(request.content, 'html.parser')

    rows = soup.select('tr.b-fight-details__table-row tr')

    return rows

if __name__ == '__main__':
    event_links = get_event_links()

    first_event_link = event_links[1]
    first_event_fights = get_fighting_links(first_event_link)
    first_fight = first_event_fights[0]

    rows = get_fighting_data(first_fight)

    print(rows)

