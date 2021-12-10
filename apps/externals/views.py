from rest_framework import viewsets
from .models import External
from .serializers import ExternalSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUserOrReadOnly


class ExternalViewSet(viewsets.ModelViewSet):
    queryset = External.objects.all()
    serializer_class = ExternalSerializer
    permission_classes = (IsAuthenticated, IsAdminUserOrReadOnly)
