from django.db import models


class Instagram(models.Model):
    access_token = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    user_id = models.IntegerField()
    full_name = models.CharField(max_length=255)
