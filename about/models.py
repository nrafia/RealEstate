from django.db import models


class About(models.Model):
    vision = models.TextField()
    mission = models.TextField()
    image = models.ImageField(upload_to='about/', null=True, default='default_about.jpg')

    def __str__(self):
        return self.vision

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"


class History(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='about/', null=True, default='default_history.jpg')

    def __str__(self):
        return self.title
