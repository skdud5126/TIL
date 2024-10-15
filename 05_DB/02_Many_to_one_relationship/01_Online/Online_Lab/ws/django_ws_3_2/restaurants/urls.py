from . import  views
from django.urls import path

app_name = 'restaurants'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_restaurant, name = 'create_restaurant'),
    path('<int:pk>/', views.detail, name='detail'),
]
