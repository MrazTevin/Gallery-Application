from django.db import models

# Create your models here.


class Images(models.Model):
    image_name = models.CharField(max_length=20)
    image_description = models.CharField(max_length=30)
