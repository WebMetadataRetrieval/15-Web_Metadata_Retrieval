from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()


class RegistrationTestCase(TestCase):

    # Setup for our Tests
    def setUp(self):
        user_a = User(email='abcd@invalid.com')
        user_a_pw = 'some_strong_123_pass'
        self.user_a_pw = user_a_pw
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a

    # Test for user's existence

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)     # ==
        self.assertNotEqual(user_count, 0)  # !=

    # Test for Signup and redirecting routes

    def test_signup_url(self):
        register_url = settings.REGISTER_URL
        data = {"email": "abcd@invalid.com",
                "password": "some_strong_123_pass"}
        response = self.client.post(register_url, data, follow=True)
        status_code = response.status_code
        redirect_path = response.request.get("PATH_INFO")
        # checks redirected route
        #self.assertEqual(redirect_path, settings.REGISTER_REDIRECT_URL)
        self.assertEqual(status_code, 200)
