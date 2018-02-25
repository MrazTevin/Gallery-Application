from django.db import models

# Create your models here.

# Image model to display image details


class Images(models.Model):
    image_name = models.CharField(max_length=20)
    image_description = models.CharField(max_length=30)

    # __str__ will return string representation of the image model
    # __str__ will enable us view our returned queries
    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['name']
