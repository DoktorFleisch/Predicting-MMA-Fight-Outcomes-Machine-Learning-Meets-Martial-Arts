import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "http://ufcstats.com/statistics/events/completed/?page={}" #use .format to get the page

website = requests.get(BASE_URL)

def get_event_links(pages=2):
    event_links = []

    for page in range(pages):
        URL = BASE_URL.format(page)
        request = requests.get(URL)
        soup = BeautifulSoup(request.content, 'html.parser')

        links = soup.select('a.b-link')

        event_links = [link['href'] for link in links if 'href' in link.attrs]

        time.sleep(1)

    return event_links
