from rest_framework import serializers
from Metadata.models import Metadata

class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = ['web_page', 'title', 'description', 'thumbnail',]

