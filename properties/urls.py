from django.urls import path
from .views import property_list, property_detail, property_neighbors

app_name = 'properties'

urlpatterns = [
    path('', property_list, name='property_list'),
    path('<int:id>', property_detail, name='property_detail'),
    path('neighbors/', property_neighbors, name='property_neighbors'),
    path('neighbors/<int:id>', property_neighbors, name='property_neighbors'),
]
