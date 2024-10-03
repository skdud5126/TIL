from . import views
from django.urls import path

urlpatterns = [
    path('recommend/', views.recommend, name = 'recommend'),
    path('bestseller/', views.bestseller, name = 'bestseller'),
]

