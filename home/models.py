from django.db import models


class Highlights(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField()
    image = models.ImageField(upload_to='home/', default='home/highlights_default.jpg')

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField()
    image = models.ImageField(upload_to='home/', default='home/services_default.jpg')

    def __str__(self):
        return self.name

