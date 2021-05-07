from django.urls import reverse, resolve
from django.test import SimpleTestCase
from Account.views import login_view, register_view, account_view, logout_view


class TestUrls(SimpleTestCase):
    def test_login_url(self):
        url = reverse('login')
        self.url = url
        self.assertEqual(resolve(self.url).func, login_view)

    def test_register_url(self):
        url = reverse('register')
        self.url = url
        self.assertEqual(resolve(self.url).func, register_view)

    def test_account_url(self):
        url = reverse('account')
        self.url = url
        self.assertEqual(resolve(self.url).func, account_view)

    def test_logout_url(self):
        url = reverse('logout')
        self.url = url
        self.assertEqual(resolve(self.url).func, logout_view)
