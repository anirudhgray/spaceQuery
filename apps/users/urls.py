from django.urls import path
from rest_framework import routers
from .views import UserViewSet, UserProfileViewSet, User_logout, MeViewSet, Reset_password


router = routers.SimpleRouter()
router.register("users/profiles", viewset=UserProfileViewSet)
router.register("users/auths", viewset=UserViewSet)
router.register("users/me", viewset=MeViewSet)

urlpatterns = [
    path('logout/', User_logout.as_view(), name='logout'),
    path('reset/', Reset_password.as_view(), name='reset')
]
