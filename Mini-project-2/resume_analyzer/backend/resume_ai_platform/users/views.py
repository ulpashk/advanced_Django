from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserAccount
from .serializers import UserRegisterSerializer, UserLoginSerializer


from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator

from django.shortcuts import get_object_or_404

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            user.save()

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            current_site = get_current_site(request).domain
            activation_link = f"http://{current_site}/api/users/activate/{uid}/{token}/"

            message = f"Hi {user.name}, click the link to activate your account:\n{activation_link}"
            send_mail('Activate your account', message, None, [user.email])

            return Response({'message': 'User registered. Please check your email to activate your account.'}, status=201)
        return Response(serializer.errors, status=400)


# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserRegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             tokens = get_tokens_for_user(user)
#             return Response({'user': serializer.data, 'tokens': tokens}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            tokens = get_tokens_for_user(user)
            return Response({'tokens': tokens})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ActivateAccountView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_object_or_404(UserAccount, pk=uid)
        except Exception:
            return Response({'error': 'Invalid activation link'}, status=400)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'message': 'Account activated successfully'}, status=200)
        return Response({'error': 'Invalid or expired token'}, status=400)


class PasswordResetRequestView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user = UserAccount.objects.filter(email=email).first()
        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            current_site = get_current_site(request).domain
            reset_link = f"http://{current_site}/reset-password/{uid}/{token}/"  # Frontend will use this

            send_mail('Password Reset', f"Click to reset your password:\n{reset_link}", None, [email])
        return Response({'message': 'If your email exists, a reset link has been sent.'})


class PasswordResetConfirmView(APIView):
    def post(self, request, uidb64, token):
        password = request.data.get('password')
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = UserAccount.objects.get(pk=uid)
        except (UserAccount.DoesNotExist, ValueError, TypeError):
            return Response({'error': 'Invalid reset link'}, status=400)

        if default_token_generator.check_token(user, token):
            user.set_password(password)
            user.save()
            return Response({'message': 'Password has been reset successfully'})
        return Response({'error': 'Invalid or expired token'}, status=400)