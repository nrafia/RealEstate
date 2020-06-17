from django.db import models

class Agents(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='agents/', default='agents/default_agent.jpg')

    def __str__(self):
        return self.name
