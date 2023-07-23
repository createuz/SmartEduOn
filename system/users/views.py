from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.core.mail import send_mail


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    @action(detail=False, methods=['post'])
    def reset_password(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'success': False, 'error': 'User not found'}, status=404)

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        subject = 'Reset Password'
        message = f'''
            User: {user.email}\n
            token: {token}\n
            uid: {uid}
        '''
        send_mail(subject, message, 'no-reply@gmail.com', [user.email])

        return Response({'success': True, 'message': 'Email sent'}, status=200)

    @action(detail=False, methods=['post'])
    def reset_password_confirm(self, request, uid, token):
        try:
            user_id = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=user_id)
        except (User.DoesNotExist, ValueError):
            return Response({'success': False, 'error': '❌ Invalid user or token'}, status=400)

        if not default_token_generator.check_token(user, token):
            return Response({'success': False, 'error': '❌ Invalid token'}, status=400)

        new_password = request.data.get('password')
        user.set_password(new_password)
        user.save()
        return Response({'success': True, 'message': '✅ Password changed'}, status=200)


class LogoutViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({'error': 'Refresh token is required'}, status=400)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response({'error': 'Invalid refresh token'}, status=400)

        return Response({'message': 'Logout successful'}, status=200)
