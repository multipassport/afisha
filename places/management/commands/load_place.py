import os
import requests

from requests.exceptions import HTTPError
from urllib.parse import urlsplit
from django.core.files.base import ContentFile
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
from places.models import Image, Place


def download_image(url, place_id):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_content = ContentFile(response.content)
        image_name = os.path.split(urlsplit(url).path)[-1]
        Path(os.path.join(settings.BASE_DIR, 'media')).mkdir(exist_ok=True)
        if image_name not in os.listdir(settings.MEDIA_ROOT):
            image, _ = Image.objects.get_or_create(
                image=image_name, place_id=place_id)
            image.image.save(image_name, image_content, save=True)
    except ConnectionError:
        raise CommandError('ConnectionError. Try again later')
    except HTTPError:
        raise CommandError(f'Photo from {url} is not found')


def get_place(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except ConnectionError:
        raise CommandError('ConnectionError. Try again later')
    except HTTPError:
        raise CommandError(f'JSON file from {url} is not found')
    return response.json()


def create_place(place_content):
    place, _ = Place.objects.get_or_create(
        title=place_content['title'],
        longitude=place_content['coordinates']['lng'],
        latitude=place_content['coordinates']['lat'],
        description_long=place_content['description_long'],
        description_short=place_content['description_short'],
    )
    place_id = place.id
    for photo_url in place_content['imgs']:
        download_image(photo_url, place_id)


class Command(BaseCommand):
    help = 'Upload images from .json file'

    def add_arguments(self, parser):
        parser.add_argument(
            'place_url', type=str,
            help='Input url of json file containing Place model data'
        )

    def handle(self, *args, **options):
        place_content = get_place(options['place_url'])
        create_place(place_content)
