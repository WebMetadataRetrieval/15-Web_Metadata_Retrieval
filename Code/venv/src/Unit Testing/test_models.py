from django.test import TestCase
# from django.contrib.auth import get_user_model
from Metadata.models import Metadata

#User = get_user_model()


class ModelTestCase(TestCase):

    # Setup for our Tests
    def setUp(self):
        web_page = 'https://www.abcdinvalid.com'
        title = 'some_title'
        description = 'Some long long description'
        thumbnail = 'https://invalidthumbnail.png'

    def test_str(self):
        company = Metadata()
        #self.assertEqual(str(company), company.name)
