from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, UserProfileViewSet, User_logout


router = routers.DefaultRouter()
router.register("profiles", viewset=UserProfileViewSet)
router.register("auths", viewset=UserViewSet)

urlpatterns = [
    path('logout/', User_logout.as_view(), name='logout'),
    path('', include(router.urls))
]
