from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
import time

import django.contrib.auth


class TestAPIEndPoint(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('GUI_Testing/chromedriver.exe')
        
    def tearDown(self):
        self.browser.close()

    # Request API End Point without any params
    def test_api_with_zero_arguments(self):

        url = self.live_server_url + '/api'

        self.browser.get(url)
        time.sleep(1)
        self.assertEquals(
            self.browser.find_element_by_class_name('meta').find_element_by_tag_name('b').text,
            "HTTP 400 Bad Request"
            )
        

    # Request API End Point without API_KEY param
    def test_api_without_api_key(self):

        web_page = "web_page=" + "https://youtu.be/28zdhLPZ1Zk"
        cached = "cached=" + "true"
        url = self.live_server_url + '/api' + '/?' + web_page + '&' + cached

        self.browser.get(url)
        time.sleep(1)
        self.assertEquals(
            self.browser.find_element_by_class_name('meta').find_element_by_tag_name('b').text,
            "HTTP 400 Bad Request"
            )
        

    # Request API End Point without Web_Page param
    def test_api_without_web_page(self):

        User = django.contrib.auth.get_user_model()
        user = User.objects.create_user('some@email.com', password='somepassword@123')
        user.save()

        api_key = "api_key=" + str(user.api_key)
        url = self.live_server_url + '/api' + '/?' + api_key

        self.browser.get(url)
        time.sleep(1)
        self.assertEquals(
            self.browser.find_element_by_class_name('meta').find_element_by_tag_name('b').text,
            "HTTP 400 Bad Request"
            )

    # Request API End Point with invalid API key
    def test_api_with_wrong_api_key(self):

        User = django.contrib.auth.get_user_model()
        user = User.objects.create_user('some@email.com', password='somepassword@123')
        user.save()

        api_key = "api_key=" + str(user.api_key) + '12'
        web_page = "web_page=" + "https://youtu.be/28zdhLPZ1Zk"
        url = self.live_server_url + '/api' + '/?' + api_key + '&' + web_page

        self.browser.get(url)
        time.sleep(1)
        self.assertEquals(
            self.browser.find_element_by_class_name('meta').find_element_by_tag_name('b').text,
            "HTTP 401 Unauthorized"
            )

    # Request API End Point with proper perams
    def test_api_with_proper_perams(self):
        
        User = django.contrib.auth.get_user_model()
        user = User.objects.create_user('some@email.com', password='somepassword@123')
        user.save()

        api_key = "api_key=" + str(user.api_key)
        web_page = "web_page=" + "https://youtu.be/28zdhLPZ1Zk"
        url = self.live_server_url + '/api' + '/?' + api_key + '&' + web_page

        self.browser.get(url)
        time.sleep(1)
        self.assertEquals(
            self.browser.find_element_by_class_name('meta').find_element_by_tag_name('b').text,
            "HTTP 200 OK"
            )

    # Requesting API End point with cached = true
    def test_api_with_proper_perams_plus_cached(self):
        
        User = django.contrib.auth.get_user_model()
        user = User.objects.create_user('some@email.com', password='somepassword@123')
        user.save()

        api_key = "api_key=" + str(user.api_key)
        web_page = "web_page=" + "https://youtu.be/28zdhLPZ1Zk"
        cached = "cached=" + "true"
        url = self.live_server_url + '/api' + '/?' + api_key + '&' + web_page + '&' + cached

        self.browser.get(url)
        time.sleep(1)
        self.assertEquals(
            self.browser.find_element_by_class_name('meta').find_element_by_tag_name('b').text,
            "HTTP 200 OK"
            )

    # Request API End Point with Daily limit exceeded account
    def test_api_with_user_with_zero_daily_limit(self):

        User = django.contrib.auth.get_user_model()
        user = User.objects.create_user('some@email.com', password='somepassword@123')
        user.daily_limit = 0
        user.save()

        api_key = "api_key=" + str(user.api_key)
        web_page = "web_page=" + "https://youtu.be/28zdhLPZ1Zk"
        url = self.live_server_url + '/api' + '/?' + api_key + '&' + web_page

        self.browser.get(url)
        time.sleep(1)
        self.assertEquals(
            self.browser.find_element_by_class_name('meta').find_element_by_tag_name('b').text,
            "HTTP 403 Forbidden"
            )