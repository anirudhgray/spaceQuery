from django.urls import path, include
from rest_framework import routers
from .views import SaveViewSet


router = routers.DefaultRouter()
router.register("", viewset=SaveViewSet)

urlpatterns = [
    path('', include(router.urls))
]
