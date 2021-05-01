from django.contrib import admin
from django.urls import path

from Metadata.api.views import (
    metadata_api,
)

app_name = 'Metadata'

urlpatterns = [
    path('', metadata_api, name="api"),
]
