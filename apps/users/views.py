from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserProfileSerializer
from .models import UserProfile
from .permissions import IsUserAccess, IsProfileAccess, CanPost


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [(IsUserAccess & IsAuthenticated) | (CanPost & ~ IsAuthenticated)]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsProfileAccess, IsAuthenticated)
