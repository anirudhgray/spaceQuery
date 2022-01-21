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
from config.settings import EMAIL_HOST_USER
import datetime
import pytz


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def check_reset_token(request):
    """Handle password reset requests initiated via a valid forgot password link."""
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
    """Handle forgot password requests. Generate hashed tokens for the same, and email the user with a reset link."""
    token = get_random_string(length=16)
    token_hash = make_password(token)
    id = get_random_string(length=16)
    pwd_request_obj = ForgotPasswordRequests(id=id, token_hash=token_hash, user=request.data.get("email"))
    pwd_request_obj.save()

    res = sm(
        subject='Your forgot password request.',
        message=f"""
        We received a request to reset the password for your account for this email address. To initiate the password reset process for your account, click: https://spacequery.netlify.app/forgot-reset?ID={id}&token={token}. This link will be active for 10 minutes only.
        """,
        html_message=f"""
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                <title>HTML email template</title>
                <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
            </head>
            <body style="background-color: #ffffff; font-size: 16px;">
                <center>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" style="height:100%; width:600px;">
                        <tr>
                            <td align="center" bgcolor="#ffffff" style="padding:30px">
                            <h2>spaceQuery</h2>
                            <p style="text-align:left">Hello,<br><br> We received a request to reset the password for your account for this email address. To initiate the password reset process for your account, click the link below.
                            </p>
                            <p>
                                <a target="_blank" style="text-decoration:none; background-color: purple; border: purple 1px solid; color: #fff; padding:10px 10px; display:block;" href="https://spacequery.netlify.app/forgot-reset?ID={id}&token={token}">
                                <strong>Reset Password</strong></a>
                            </p>
                            <p style="text-align:left">This link will be active for 10 minutes only. If you need to reset your password again, please visit https://spacequery.netlify.app/ and request another reset.<br><br>If you did not make this request, you can simply ignore this email.</p>
                            <p style="text-align:left">
                            Sincerely,<br>spaceQuery Admin.
                            </p>
                            </td>
                        </tr>
                    </table>
                </center>
            </body>
        </html>
        """,
        from_email='mail@gmail.com',
        recipient_list=[request.data.get("email")],
        fail_silently=False,
    )
    return Response(f"Sent {res}")


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def feedback(request):
    """Send an email with the feedback content as submitted by the user."""
    res = sm(
        subject=request.data.get("email"),
        message=f'''Rating: {request.data.get("rate")},
        Category: {request.data.get("category")},
        Description: {request.data.get("desc")}''',
        from_email='mail@gmail.com',
        recipient_list=[EMAIL_HOST_USER],
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
    """Handle password reset requests initiated by a logged in user."""
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
    """Return profile information about the current logged in user."""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return get_user_model().objects.filter(id=self.request.user.id)
