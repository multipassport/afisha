from django.http import HttpResponse
from django.template import loader

from places.models import Place


def get_geo_json():
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
                "detailsUrl": "static/places/moscow_legends.json"
            }
        } for place in Place.objects.all()
    ]
    geo_json = {
        "type": "FeatureCollection",
        "features": features
    }
    return geo_json


def show_index_page(request):
    template = loader.get_template('index.html')
    context = {'geo_json': get_geo_json()}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
