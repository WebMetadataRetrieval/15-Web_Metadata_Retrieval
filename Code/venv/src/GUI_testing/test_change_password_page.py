from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from unittest import skip
import time

class TestChangePasswordPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='GUI_testing/chromedriver.exe')
        Users = get_user_model()
        user = Users.objects.create_user('paresh@gmail.com', password='1#XxYyZz')
        user.save()
        self.browser.get(self.live_server_url + "/login")

        self.browser.find_element_by_id("inputEmail").send_keys("paresh@gmail.com")
        self.browser.find_element_by_id("inputPassword").send_keys("1#XxYyZz")

        self.browser.find_elements_by_id("showPass")[0].click()
        time.sleep(2)
        self.browser.find_elements_by_class_name("btn")[1].click()
        time.sleep(2)

        new_url = self.live_server_url + "/account/"
        self.assertEquals(self.browser.current_url, new_url)


    def tearDown(self):
        self.browser.close()
    
    #@skip("Don't want to test")
    def test_able_to_change_password_with_valid_old_and_new_passwords(self):
        self.browser.get(self.live_server_url + "/password_change")

        self.browser.find_element_by_id("id_old_password").send_keys("1#XxYyZz")
        self.browser.find_element_by_id("id_new_password1").send_keys("1#AaBbCc")
        self.browser.find_element_by_id("id_new_password2").send_keys("1#AaBbCc")
        time.sleep(2)

        self.browser.find_elements_by_class_name("btn")[1].click()
        time.sleep(2)

        new_url = self.live_server_url + "/password_change/done/"
        self.assertEquals(self.browser.current_url, new_url)


    #@skip("Don't want to test")
    def test_not_able_to_change_password_with_invalid_old_password(self):
        self.browser.get(self.live_server_url + "/password_change")

        def clear_fields(self):
            old_password = self.browser.find_element_by_id("id_old_password")
            old_password.clear()
            new_password = self.browser.find_element_by_id("id_new_password1")
            new_password.clear()
            new_password = self.browser.find_element_by_id("id_new_password2")
            new_password.clear()
        
        tests = ["", "1@XxYyZz", "1#XXYYZZ", "2#XxYyZz"]

        for i in tests:
            clear_fields(self)    
            self.browser.find_element_by_id("id_old_password").send_keys(i)
            self.browser.find_element_by_id("id_new_password1").send_keys("1#AaBbCc")
            self.browser.find_element_by_id("id_new_password2").send_keys("1#AaBbCc")
            time.sleep(2)

            self.browser.find_elements_by_class_name("btn")[1].click()
            time.sleep(2)

            new_url = self.live_server_url + "/password_change/"
            self.assertEquals(self.browser.current_url, new_url)


    #@skip("Don't want to test")
    def test_not_able_to_change_password_with_invalid_new_passwords(self):
        self.browser.get(self.live_server_url + "/password_change")

        def clear_fields(self):
            old_password = self.browser.find_element_by_id("id_old_password")
            old_password.clear()
            new_password = self.browser.find_element_by_id("id_new_password1")
            new_password.clear()
            new_password = self.browser.find_element_by_id("id_new_password2")
            new_password.clear()
        
        tests = ["", "paresh", "1#Paresh", "1#XxYy", "password", "123456789", "1#AaBbCc"]

        for i in tests:
            clear_fields(self)    
            self.browser.find_element_by_id("id_old_password").send_keys("1#XxYyZz")
            self.browser.find_element_by_id("id_new_password1").send_keys(i)
            if (i=="1#AaBbCc"):
                i = i + "a"
            self.browser.find_element_by_id("id_new_password2").send_keys(i)
            time.sleep(2)

            self.browser.find_elements_by_class_name("btn")[1].click()
            time.sleep(2)

            new_url = self.live_server_url + "/password_change/"
            self.assertEquals(self.browser.current_url, new_url)