from rest_framework import serializers
from .models import Save, History


class SaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Save
        fields = ('url', 'id', 'user', 'title', 'info', 'save_time')
        extra_kwargs = {'user': {'read_only': True}}

    def get_fields(self, *args, **kwargs):
        fields = super(SaveSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) == "POST":
            fields['user'].read_only = False
        return fields


class HistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = ('url', 'id', 'user', 'title', 'info', 'search_time')
        extra_kwargs = {'user': {'read_only': True}}

    def get_fields(self, *args, **kwargs):
        fields = super(HistorySerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) == "POST":
            fields['user'].read_only = False
        return fields
