from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
import time
from unittest import skip

import django.contrib.auth

class TestRedirects(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('GUI_Testing/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    # @skip("Don't want")
    def test_home_page_redirects(self):

        home_page = self.live_server_url + reverse('home')

        redirects = {
            'documentation' : 'https://docs.google.com/document/d/1chmmfWFlP5Hf5uhSkZ_u31DODUu3Trtp4VTlmLdkvDQ/edit',
            'help' : 'https://github.com/WebMetadataRetrieval/15-Web_Metadata_Retrieval/discussions',
            'login' : self.live_server_url + reverse('login'),
            'register' : self.live_server_url + reverse('register'),
            'home' : self.live_server_url + reverse('home'),
            'get_key' : self.live_server_url + reverse('register'),
            'github' : 'https://github.com/WebMetadataRetrieval/15-Web_Metadata_Retrieval'
        }

        for key in redirects:

            self.browser.get(home_page)
            time.sleep(1)
            self.browser.find_element_by_class_name(key).click()
            time.sleep(1)
            self.assertEquals(
                self.browser.current_url, 
                redirects[key]
                )

        email = 'some@email.com'
        password = 'somepassword@123'
        User = django.contrib.auth.get_user_model()
        user = User.objects.create_user(email, password=password)
        user.save()

        self.browser.get(redirects['login'])
        time.sleep(1)
        self.browser.find_element_by_id('inputEmail').send_keys(email)
        time.sleep(1)
        self.browser.find_element_by_id('inputPassword').send_keys(password)
        time.sleep(1)
        self.browser.find_element_by_class_name('login_btn').click()
        time.sleep(1)
        self.browser.get(home_page)

        redirects_loggedin = {
            'account': self.live_server_url + reverse('account'),
            'go_doc': 'https://docs.google.com/document/d/1chmmfWFlP5Hf5uhSkZ_u31DODUu3Trtp4VTlmLdkvDQ/edit',
        }

        for key in redirects_loggedin:

            self.browser.get(home_page)
            time.sleep(1)
            self.browser.find_element_by_class_name(key).click()
            time.sleep(1)
            self.assertEquals(
                self.browser.current_url, 
                redirects_loggedin[key]
                )

    # @skip("Checked")
    def test_login_page_redirects(self):

        login_page = self.live_server_url + reverse('login')

        redirects = {
            'documentation' : 'https://docs.google.com/document/d/1chmmfWFlP5Hf5uhSkZ_u31DODUu3Trtp4VTlmLdkvDQ/edit',
            'help' : 'https://github.com/WebMetadataRetrieval/15-Web_Metadata_Retrieval/discussions',
            'register' : self.live_server_url + reverse('register'),
            'home' : self.live_server_url + reverse('home'),
            'h_icon' : self.live_server_url + reverse('home'),
            'github' : 'https://github.com/WebMetadataRetrieval/15-Web_Metadata_Retrieval',
            'dont_reg' : self.live_server_url + reverse('register'),
            'forgot' : self.live_server_url + reverse('password_reset'),
            'go_home' : self.live_server_url + reverse('home')
        }

        for key in redirects:

            self.browser.get(login_page)
            time.sleep(1)
            self.browser.find_element_by_class_name(key).click()
            time.sleep(1)
            self.assertEquals(
                self.browser.current_url, 
                redirects[key]
                )

    # @skip("Checked")
    def test_register_page_redirects(self):

        register_page = self.live_server_url + reverse('register')

        redirects = {
            'documentation' : 'https://docs.google.com/document/d/1chmmfWFlP5Hf5uhSkZ_u31DODUu3Trtp4VTlmLdkvDQ/edit',
            'help' : 'https://github.com/WebMetadataRetrieval/15-Web_Metadata_Retrieval/discussions',
            'login' : self.live_server_url + reverse('login'),
            'home' : self.live_server_url + reverse('home'),
            'h_icon' : self.live_server_url + reverse('home'),
            'github' : 'https://github.com/WebMetadataRetrieval/15-Web_Metadata_Retrieval',
            'already' : self.live_server_url + reverse('login'),
            'go_home' : self.live_server_url + reverse('home')
        }

        for key in redirects:

            self.browser.get(register_page)
            time.sleep(1)
            self.browser.find_element_by_class_name(key).click()
            time.sleep(1)
            self.assertEquals(
                self.browser.current_url, 
                redirects[key]
                )

    # @skip("Checked")
    def test_account_page_redirects(self):

        account_page = self.live_server_url + reverse('account')

        email = 'some@email.com'
        password = 'somepassword@123'
        User = django.contrib.auth.get_user_model()
        user = User.objects.create_user(email, password=password)
        user.save()

        self.browser.get(self.live_server_url + reverse('login'))
        time.sleep(1)
        self.browser.find_element_by_id('inputEmail').send_keys(email)
        self.browser.find_element_by_id('inputPassword').send_keys(password)
        time.sleep(1)
        self.browser.find_element_by_class_name('login_btn').click()
        time.sleep(1)

        redirects = {
            'documentation' : 'https://docs.google.com/document/d/1chmmfWFlP5Hf5uhSkZ_u31DODUu3Trtp4VTlmLdkvDQ/edit',
            'help' : 'https://github.com/WebMetadataRetrieval/15-Web_Metadata_Retrieval/discussions',
            'home' : self.live_server_url + reverse('home'),
            'h_icon' : self.live_server_url + reverse('home'),
            'github' : 'https://github.com/WebMetadataRetrieval/15-Web_Metadata_Retrieval',
            'change_pass' : self.live_server_url + reverse('password_change')
        }

        for key in redirects:

            self.browser.get(account_page)
            time.sleep(1)
            self.browser.find_element_by_class_name(key).click()
            time.sleep(1)
            self.assertEquals(
                self.browser.current_url, 
                redirects[key]
                )

        self.browser.get(account_page)
        time.sleep(1)
        self.browser.find_element_by_class_name('logout').click()
        time.sleep(1)
        self.assertEquals(
            self.browser.current_url, 
            self.live_server_url + reverse('home')
            )

    