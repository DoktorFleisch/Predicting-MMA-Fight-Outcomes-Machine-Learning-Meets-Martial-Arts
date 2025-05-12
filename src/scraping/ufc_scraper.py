import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "http://ufcstats.com/statistics/events/completed/?page={}" #use .format to get the page

def get_event_links(pages=2, delay=1):
    all_event_links = []

    for page in range(pages):
        URL = BASE_URL.format(page)
        request = requests.get(URL)
        soup = BeautifulSoup(request.content, 'html.parser')

        links = soup.select('a.b-link')

        event_links = [link['href'] for link in links if 'href' in link.attrs]
        all_event_links.extend(event_links)

        time.sleep(delay)

    return all_event_links
