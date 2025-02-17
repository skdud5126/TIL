from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('<int:user_pk>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup')
]
