from django.db import models

# Create your models here.

# Image model to display image details


class Images(models.Model):
    image_name = models.CharField(max_length=20)
    image_description = models.CharField(max_length=30)
    # post will contain the image content
    post = models.TextField()
    # one location may describe many images while many images may have one
    # location
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    # __str__ will return string representation of the image model
    # __str__ will enable us view our returned queries

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['name']

# Location model to enable us choose location


class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
