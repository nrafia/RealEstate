from django.urls import path
from .views import success, contact_us

app_name = 'contact'

urlpatterns = [
    path('', contact_us, name='contact_us'),
    path('success/', success, name='success')
]
