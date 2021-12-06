from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserProfileSerializer
from .models import UserProfile
from .permissions import IsUserAccess, IsProfileAccess, CanPost
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [(IsUserAccess & IsAuthenticated) | (CanPost & ~ IsAuthenticated)]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsProfileAccess, IsAuthenticated)


class User_logout(GenericAPIView):
    permission_classes = [(IsAuthenticated)]
    authentication_classes = [(TokenAuthentication)]

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response("Logged out.")
