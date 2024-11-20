from django.urls import path
from . import views

urlpatterns = [
    path('convert_csv_to_dataframe/', views.convert_csv_to_dataframe),
    path('get_data_nan/', views.get_data_nan),
    path('get_data_avg/', views.get_data_avg),
]

