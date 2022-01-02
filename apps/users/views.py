from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserProfileSerializer
from .models import UserProfile
from .permissions import IsUserAccess, IsProfileAccess, CanPost
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import TokenAuthentication
from django.http import HttpResponseBadRequest
from django.core.mail import send_mail as sm
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


@csrf_exempt
@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def forgot_pwd(request):
    res = sm(
        subject='Subject here',
        message='Here is the message.',
        from_email='mail@gmail.com',
        recipient_list=[request.data.get("email")],
        fail_silently=False,
    )

    return Response(f"Sent {res}")


@csrf_exempt
@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def feedback(request):
    res = sm(
        subject=request.data.get("email"),
        message=f'''Rating: {request.data.get("rate")},
        Category: {request.data.get("category")},
        Description: {request.data.get("desc")}''',
        from_email='mail@gmail.com',
        recipient_list=['spacequerywebapp@gmail.com'],
        fail_silently=False,
    )

    return Response(f"Sent {res}")


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [(IsUserAccess & IsAuthenticated) | (CanPost & ~ IsAuthenticated)]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsProfileAccess, IsAuthenticated)

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        search = self.request.query_params.get('search')
        if search is not None:
            queryset = queryset.filter(user__email__contains=search)
        return queryset


class User_logout(GenericAPIView):
    permission_classes = [(IsAuthenticated)]
    authentication_classes = [(TokenAuthentication)]

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response("Logged out.")


class Reset_password(GenericAPIView):
    permission_classes = [(IsAuthenticated)]

    def post(self, request, format=None):
        user = get_user_model().objects.filter(id=request.user.id).first()
        old_password = request.data.get("oldPass")
        new_password = request.data.get("newPass")
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response("Password reset successfully.")
        return HttpResponseBadRequest("Old password incorrect.")


class MeViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return get_user_model().objects.filter(id=self.request.user.id)
