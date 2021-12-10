from rest_framework import serializers
from .models import External


class ExternalSerializer(serializers.ModelSerializer):

    class Meta:
        model = External
        fields = ('id', 'image', 'name', 'url_name', 'description', 'credit', 'link')
