from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from unittest import skip
import time

class TestLoginPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='GUI_testing/chromedriver.exe')
        Users = get_user_model()
        user = Users.objects.create_user('paresh@gmail.com', password='1#XxYyZz')
        user.save()

    def tearDown(self):
        self.browser.close()
    
    #@skip("Don't want to test")
    def test_able_to_login_with_valid_email_and_password(self):
        self.browser.get(self.live_server_url + "/login")

        self.browser.find_element_by_id("inputEmail").send_keys("paresh@gmail.com")
        self.browser.find_element_by_id("inputPassword").send_keys("1#XxYyZz")

        self.browser.find_elements_by_id("showPass")[0].click()
        time.sleep(2)
        self.browser.find_elements_by_class_name("btn")[1].click()
        time.sleep(2)

        new_url = self.live_server_url + "/account/"
        self.assertEquals(self.browser.current_url, new_url)


    #@skip("Don't want to test")
    def test_not_able_to_login_with_invalid_email_field(self):
        self.browser.get(self.live_server_url + "/login")
        
        def clear_fields(self):
            input_email = self.browser.find_element_by_id("inputEmail")
            input_email.clear()
            password = self.browser.find_element_by_id("inputPassword")
            password.clear()

        tests = ["", "pares@gmail.com", "paresh@gmai.com"]

        for i in tests:
            clear_fields(self)    
            self.browser.find_element_by_id("inputEmail").send_keys(i)
            self.browser.find_element_by_id("inputPassword").send_keys("1#XxYyZz")
            self.browser.find_elements_by_id("showPass")[0].click()
            time.sleep(2)
            self.browser.find_elements_by_class_name("btn")[1].click()
            time.sleep(2)
            new_url = self.live_server_url + "/login/"
            self.assertEquals(self.browser.current_url, new_url)

    #@skip("Don't want to test")
    def test_not_able_to_login_with_invalid_password_field(self):
        self.browser.get(self.live_server_url + "/login")
        
        def clear_fields(self):
            input_email = self.browser.find_element_by_id("inputEmail")
            input_email.clear()
            password = self.browser.find_element_by_id("inputPassword")
            password.clear()

        tests = ["", "1@XxYyZz", "1#XXYYZZ", "2#XxYyZz"]

        for i in tests:
            clear_fields(self) 
            self.browser.find_element_by_id("inputEmail").send_keys("paresh@gmail.com")
            self.browser.find_element_by_id("inputPassword").send_keys(i)
            self.browser.find_elements_by_id("showPass")[0].click()
            time.sleep(2)
            self.browser.find_elements_by_class_name("btn")[1].click()
            time.sleep(2)
            new_url = self.live_server_url + "/login/"
            self.assertEquals(self.browser.current_url, new_url)