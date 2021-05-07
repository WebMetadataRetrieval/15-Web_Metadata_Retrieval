from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from Metadata.models import Metadata
import json

User = get_user_model()


class TestViews(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.account_url = reverse('account')
        user_a = User.objects.create_user('efgh@invalid.com', 'some_strong_123_pass')
        user_a.save()
        self.user_a = user_a


    def test_register_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register.html')


    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')


    def test_account_view(self):
        data = {"email": "abcd@invalid.com", "password": "some_strong_123_pass"}
        response = self.client.post(self.account_url, data, follow=True)
        redirect_path = response.request.get("PATH_INFO")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(redirect_path, '/login/')
