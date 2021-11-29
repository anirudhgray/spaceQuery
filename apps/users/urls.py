from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet


router = routers.DefaultRouter()
router.register("", viewset=UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
