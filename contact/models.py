from django.db import models


class ContactDetails(models.Model):
    location = models.CharField(max_length=50, null=True, default= "0.0. 0.0")
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    feed_back = models.TextField()

    def __str__(self):
        return str(self.id)
