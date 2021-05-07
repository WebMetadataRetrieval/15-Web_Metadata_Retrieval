from django.test import TestCase
from Metadata.api.serializers import MetadataSerializer
from Metadata.models import Metadata


# class Test_API_Serializer(TestCase):
#     def setUp(self):
#         fields = ['web_page', 'title', 'description', 'thumbnail', ]
#         self.fields = fields

#     def test_model_fields(self):
#         for field_name in [
#             'id', 'name', 'description', 'website', 'street_line_1', 'street_line_2',
#             'city', 'state', 'zipcode'
#         ]
#         self.assertEqual(MetadataSerializer.data[field_name], getattr(Metadata, field_name))
