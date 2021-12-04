from rest_framework import viewsets
from .models import Save
from .serializers import SaveSerializer
from .permissions import IsSaveAccess
from rest_framework.permissions import IsAuthenticated


class SaveViewSet(viewsets.ModelViewSet):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer
    permission_classes = (IsAuthenticated, IsSaveAccess)
