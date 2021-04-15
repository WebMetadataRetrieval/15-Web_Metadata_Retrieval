from django.db import models

# Create your models here.

class Metadata(models.Model):
    web_page = models.TextField(primary_key=True, unique=True)
    title = models.TextField()
    description = models.TextField()
    thumbnail = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
