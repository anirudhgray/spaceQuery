from rest_framework import serializers
from .models import Save


class SaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Save
        fields = ('url', 'user', 'title', 'info', 'save_time')
        extra_kwargs = {'user': {'read_only': True}}

    def get_fields(self, *args, **kwargs):
        fields = super(SaveSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) == "POST":
            fields['user'].read_only = False
        return fields
