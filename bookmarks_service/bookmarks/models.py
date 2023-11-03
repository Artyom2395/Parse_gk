from django.db import models

from django.contrib.auth.models import User

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    favicon = models.ImageField(upload_to='favicons/', blank=True)

