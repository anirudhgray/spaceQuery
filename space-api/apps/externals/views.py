from rest_framework import viewsets
from .models import External
from .serializers import ExternalSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUserOrReadOnly
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import JsonResponse
import requests
from decouple import config
MAP_KEY = config('MAP_KEY')


class ExternalViewSet(viewsets.ModelViewSet):
    queryset = External.objects.all()
    serializer_class = ExternalSerializer
    permission_classes = (IsAuthenticated, IsAdminUserOrReadOnly)


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def ISSData(request):
    """Return the current position (lat, long, and other data) of the ISS as JSON."""

    URL = 'https://api.wheretheiss.at/v1/satellites/25544'
    r = requests.get(url=URL)
    data = r.json()
    print(data)
    return JsonResponse(data)


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def ISSLoc(request):
    """Return the country code (if applicable), timezone and map url of specified coordinates as JSON."""

    URL = 'https://api.wheretheiss.at/v1/coordinates/'
    lat = request.data.get('lat')
    long = request.data.get('long')
    URL += str(lat) + ',' + str(long)
    r = requests.get(url=URL)
    data = r.json()
    data['map_url'] = f"https://www.google.com/maps/embed/v1/search?q={lat},{long}&zoom=5&maptype=satellite&key={MAP_KEY}"
    return JsonResponse(data)
