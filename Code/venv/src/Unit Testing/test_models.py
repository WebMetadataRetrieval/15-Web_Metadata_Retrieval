from django.test import TestCase
from Metadata.models import Metadata


class ModelTestCase(TestCase):

    # Setup for our Tests
    def setUp(self):
        meta_data = Metadata.objects.create(
            web_page = 'https://www.abcdinvalid.com',
            title = 'some_title',
            description = 'Some long long description',
            thumbnail = 'https://invalidthumbnail.png')

    def test_metadata_model(self):
        meta = Metadata()
        self.assertEqual(str(meta), meta.web_page)