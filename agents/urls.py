from django.urls import path
from .views import agents

app_name = 'agents'

urlpatterns = [
    path('', agents, name='agents'),
]
