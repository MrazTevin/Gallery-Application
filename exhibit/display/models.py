from django.db import models

# Create your models here.

# Image model to display image details


class Images(models.Model):
    image_name = models.CharField(max_length=20)
    image_description = models.CharField(max_length=30)
