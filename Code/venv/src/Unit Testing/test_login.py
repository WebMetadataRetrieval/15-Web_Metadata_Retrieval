from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()


class UserTestCase(TestCase):

    # Setup for our Tests
    def setUp(self):
        user_a = User(email='abcd@invalid.com')
        user_a_pw = 'some_strong_123_pass'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a
        user_b = User.objects.create_user(
            'efgh@invalid.com', 'some_strong_123_pass')
        self.user_b = user_b

    # Test for User Exists

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)     # ==
        self.assertNotEqual(user_count, 0)  # !=

    # Test for Validating User's Email

    def test_user_email(self):
        user_qs = User.objects.filter(email__iexact="abcd@invalid.com")
        user_exists = user_qs.exists() and user_qs.count() == 1
        self.assertTrue(user_exists)         # True/False

    # Test for Validating User's Password
    # Poorly writen Test

    # def test_user_password(self):
    #     self.assertTrue(self.user_a.check_password(self.user_a_pw))

    # Well written Test

    def test_user_password(self):
        user_a = User.objects.get(email="abcd@invalid.com")
        self.assertTrue(user_a.check_password(self.user_a_pw))

    # Testing for Login and its redirecting routes

    def test_login_url(self):
        login_url = settings.LOGIN_URL
        data = {"email": "abcd@invalid.com",
                "password": "some_strong_123_pass"}
        response = self.client.post(login_url, data, follow=True)
        status_code = response.status_code
        redirect_path = response.request.get("PATH_INFO")
        # checks redirected route
        self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)
        self.assertEqual(status_code, 200)

    # Test for Invalid Request from User

    def test_invalid_request(self):
        self.client.login(email=self.user_b.email, password='some_strong_123_pass')
        response = self.client.post("/admin/")
        self.assertNotEqual(response.status_code, 200)  # 302

    # Test for Valid Request from User

    def test_valid_request(self):
        self.client.login(email=self.user_a.email, password='some_strong_123_pass')
        response = self.client.post("/admin/")
        self.assertEqual(response.status_code, 200)  # 200
