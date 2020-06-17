from django.db import models
import secrets


def ads_keys():
    ads_key = secrets.token_hex()
    ads_key = str.upper(ads_key)
    ads_key = ads_key[0:8]
    print(ads_key)
    return ads_key


pr_type = (
    ('Sale', "Sale"),
    ('Rent', "Rent"),
)

pr_featured = (
    ('Yes', "Yes"),
    ('No', "No"),
)

class Property(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=50, null=True, default="null")
    state = models.ForeignKey('States', null=True, on_delete=models.SET_NULL)
    type = models.CharField(choices=pr_type, max_length=50)
    price = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    beds = models.PositiveIntegerField()
    baths = models.PositiveIntegerField()
    garages = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property_images/', default='property_images/default.png')
    ads_id = models.CharField(max_length=8, default=ads_keys, editable=True)
    featured = models.CharField(choices=pr_featured, max_length=50, default="No")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"


class States(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='state_images/', default='state_images/default.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"


class Reserve(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    notes = models.TextField()
    ads_id = models.CharField(max_length=8)

    def __str__(self):
        return self.first_name