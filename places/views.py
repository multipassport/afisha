from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def create_geo_json(places):
    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('places', args=[place.id])
            }
        } for place in places
    ]
    geo_json = {
        "type": "FeatureCollection",
        "features": features
    }
    return geo_json


def show_index_page(request):
    places = Place.objects.all()
    places_context = {'geo_json': create_geo_json(places)}
    return render(request, 'index.html', context=places_context)


def show_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    details = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }
    return JsonResponse(
        details,
        json_dumps_params={'ensure_ascii': False, 'indent': 2})
