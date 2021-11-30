from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, UserProfileViewSet


router = routers.DefaultRouter()
router.register("profiles", viewset=UserProfileViewSet)
router.register("auths", viewset=UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
