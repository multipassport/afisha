import logging
import os
import requests

from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from urllib.parse import quote


def get_places_urls(initial_url, changed_url):
    try:
        response = requests.get(initial_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        box_class = 'js-navigation-open Link--primary'
        # print(len(soup.find_all(class_=box_class)))
        for string in soup.find_all(class_=box_class):
            yield os.path.join(changed_url, quote(string['title']))
    except(HTTPError, ConnectionError) as error:
        logging.info(error)


if __name__ == '__main__':
    logging.basicConfig(filename="places.log", level=logging.INFO)
    logging.info('Program started')
    places_url = 'https://github.com/devmanorg/where-to-go-places/tree/master/places'
    raw_places_url = 'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/'

    for url in get_places_urls(places_url, raw_places_url):
        os.system(f'python manage.py load_place {url}')
