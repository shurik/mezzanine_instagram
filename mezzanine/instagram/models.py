from django.db import models


class Instagram(models.Model):
    access_token = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    user_id = models.IntegerField()
    full_name = models.CharField(max_length=255)


class Tag(models.Model):
    tag = models.CharField(max_length=255)

    def __unicode__(self):
        return self.tag


class Media(models.Model):
    media_id = models.CharField(max_length=255)
    allowed = models.BooleanField()

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media'
