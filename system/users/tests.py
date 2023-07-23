from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('user-register')
        self.login_url = reverse('token_obtain_pair')
        self.reset_password_url = reverse('user-reset-password')
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password': 'testpassword',
            'password2': 'testpassword',
        }

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_reset_password(self):
        # Register a user
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Reset password
        reset_data = {'email': self.user_data['email']}
        response = self.client.post(self.reset_password_url, reset_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'success': True, 'message': 'Email sent'})

    def test_reset_password_confirm(self):
        # Register a user
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(email=self.user_data['email'])
        refresh = RefreshToken.for_user(user)
        reset_confirm_url = reverse('user-reset-password-confirm', kwargs={
            'uid': refresh['user_id'],
            'token': refresh.access_token
        })

        # Reset password confirm
        new_password_data = {'password': 'newpassword'}
        response = self.client.post(reset_confirm_url, new_password_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'success': True, 'message': '✅ Password changed'})

    def test_invalid_reset_password_confirm(self):
        # Try to reset password with invalid token and uid
        reset_confirm_url = reverse('user-reset-password-confirm', kwargs={
            'uid': 'invalid_uid',
            'token': 'invalid_token'
        })
        new_password_data = {'password': 'newpassword'}
        response = self.client.post(reset_confirm_url, new_password_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'success': False, 'error': '❌ Invalid user or token'})
