from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('url', 'id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = UserProfile
        fields = ('url', 'user', 'email', 'first_name', 'last_name',
                  'github_username', 'image', 'saved_results', 'queries_made')
        extra_kwargs = {'user': {'read_only': True}, 'saved_results': {
            'read_only': True}, 'queries_made': {'read_only': True}}

    def get_fields(self, *args, **kwargs):
        fields = super(UserProfileSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) == "POST":
            fields['user'].read_only = False
        return fields
