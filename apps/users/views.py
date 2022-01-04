from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserProfileSerializer
from .models import UserProfile, ForgotPasswordRequests
from .permissions import IsUserAccess, IsProfileAccess, CanPost
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import TokenAuthentication
from django.http import HttpResponseBadRequest
from django.core.mail import send_mail as sm
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password, check_password
import datetime
import pytz


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def check_reset_token(request):
    curr_time = datetime.datetime.now().replace(tzinfo=pytz.UTC)
    id = request.data.get('id')
    token = request.data.get('token')
    record = ForgotPasswordRequests.objects.filter(id=id)
    if record:
        record = record[0]
        if check_password(token, record.token_hash):
            if curr_time - record.time < datetime.timedelta(minutes=10):
                email = record.user
                new_password = request.data.get('newPass')
                user = get_user_model().objects.filter(email=email).first()
                user.set_password(new_password)
                user.save()
                return Response("Valid token, password reset.")
    return HttpResponseBadRequest("Invalid/expired token.")


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def forgot_pwd(request):
    token = get_random_string(length=16)
    token_hash = make_password(token)
    id = get_random_string(length=16)
    pwd_request_obj = ForgotPasswordRequests(id=id, token_hash=token_hash, user=request.data.get("email"))
    pwd_request_obj.save()

    res = sm(
        subject='Your forgot password request.',
        message=f"""Ignore this mail if you did not request this/do not use this app.
        Head over to http://192.168.1.33:8080/forgot-reset?ID={id}&token={token} to reset your password.
        This link will be active for 10 minutes only.""",
        from_email='mail@gmail.com',
        recipient_list=[request.data.get("email")],
        fail_silently=False,
    )
    return Response(f"Sent {res}")


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
