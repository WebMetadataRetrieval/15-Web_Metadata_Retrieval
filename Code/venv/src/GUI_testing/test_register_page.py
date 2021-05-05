from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from unittest import skip
import time

class TestRegisterPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('GUI_testing/chromedriver.exe')

    def tearDown(self):
        self.browser.close()
    
    #@skip("Don't want to test")
    def test_able_to_register_with_valid_email_and_password(self):
        self.browser.get(self.live_server_url + "/register")

        self.browser.find_element_by_id("inputEmail").send_keys("paresh@gmail.com")
        self.browser.find_element_by_id("inputPassword1").send_keys("1#XxYyZz")
        self.browser.find_element_by_id("inputPassword2").send_keys("1#XxYyZz")

        self.browser.find_elements_by_id("showPass")[0].click()
        time.sleep(3)
        self.browser.find_elements_by_class_name("btn")[1].click()
        time.sleep(3)

        new_url = self.live_server_url + "/account/"
        self.assertEquals(self.browser.current_url, new_url)
        

    #@skip("Don't want to test")
    def test_not_able_to_register_with_invalid_email_field(self):
        self.browser.get(self.live_server_url + "/register")

        def clear_fields(self):
            input_email = self.browser.find_element_by_id("inputEmail")
            input_email.clear()
            password1 = self.browser.find_element_by_id("inputPassword1")
            password1.clear()
            password2 = self.browser.find_element_by_id("inputPassword2")
            password2.clear()
        
        tests = ["", "paresh", "paresh.com", "paresh@", "paresh@.com", "@.com"]
        self.browser.find_elements_by_id("showPass")[0].click()

        for i in tests:
            clear_fields(self)    
            self.browser.find_element_by_id("inputEmail").send_keys(i)
            self.browser.find_element_by_id("inputPassword1").send_keys("1#XxYyZzx")
            self.browser.find_element_by_id("inputPassword2").send_keys("1#XxYyZzx")
            time.sleep(2)
            self.browser.find_elements_by_class_name("btn")[1].click()
            time.sleep(2)
            new_url = self.live_server_url + "/register/"
            self.assertEquals(self.browser.current_url, new_url)


    #@skip("Don't want to test")
    def test_not_able_to_register_with_invalid_password_field(self):
        self.browser.get(self.live_server_url + "/register")

        def clear_fields(self):
            input_email = self.browser.find_element_by_id("inputEmail")
            input_email.clear()
            password1 = self.browser.find_element_by_id("inputPassword1")
            password1.clear()
            password2 = self.browser.find_element_by_id("inputPassword2")
            password2.clear()

        tests = ["", "paresh", "1#Paresh", "1#XxYy", "password", "123456789", "1#XxYyZz"]

        for i in tests:
            clear_fields(self)    
            self.browser.find_element_by_id("inputEmail").send_keys("paresh@gmail.com")
            self.browser.find_element_by_id("inputPassword1").send_keys(i)
            if (i=="1#XxYyZz"):
                i = i + "a"
            self.browser.find_element_by_id("inputPassword2").send_keys(i)
            self.browser.find_elements_by_id("showPass")[0].click()
            time.sleep(2)
            self.browser.find_elements_by_class_name("btn")[1].click()
            time.sleep(2)
            new_url = self.live_server_url + "/register/"
            self.assertEquals(self.browser.current_url, new_url)
