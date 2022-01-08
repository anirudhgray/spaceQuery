from rest_framework import routers
from django.urls import path
from .views import ExternalViewSet, ISSData, ISSLoc


router = routers.SimpleRouter()
router.register("externals", viewset=ExternalViewSet)

urlpatterns = [
    path('iss/data', ISSData, name='issdata'),
    path('iss/loc', ISSLoc, name='issloc')
]
