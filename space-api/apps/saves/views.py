from rest_framework import viewsets
from .models import Save, History
from .serializers import SaveSerializer, HistorySerializer
from .permissions import IsSaveAccess
from rest_framework.permissions import IsAuthenticated
from apps.users.models import UserProfile


class SaveViewSet(viewsets.ModelViewSet):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer
    permission_classes = (IsAuthenticated, IsSaveAccess)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        profile = UserProfile.objects.get(user=self.request.user)
        profile.saved_results = len(Save.objects.filter(user=self.request.user))
        profile.save()

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        profile = UserProfile.objects.get(user=self.request.user)
        profile.saved_results = len(Save.objects.filter(user=self.request.user))
        profile.save()

    def get_queryset(self):
        queryset = Save.objects.all()
        search = self.request.query_params.get('search')
        if search is not None:
            queryset = queryset.filter(user__id=search)
        return queryset


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = (IsAuthenticated, IsSaveAccess)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        profile = UserProfile.objects.get(user=self.request.user)
        profile.queries_made = len(History.objects.filter(user=self.request.user))
        profile.save()

    def get_queryset(self):
        queryset = History.objects.all()
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
        return queryset
