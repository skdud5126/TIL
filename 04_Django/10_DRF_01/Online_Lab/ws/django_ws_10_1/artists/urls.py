from . import views
from django.urls import path

urlpatterns = [
    path('artists/', views.artist_list),
]
