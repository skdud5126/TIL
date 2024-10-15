from . import views
from django.urls import path

urlpatterns = [
    
    path('accounts/login/', views.login, name = 'login'), 


 ]
