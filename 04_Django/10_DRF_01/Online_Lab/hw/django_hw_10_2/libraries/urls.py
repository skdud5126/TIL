from . import views
from django.urls import path

urlpatterns = [
    path('libraries/', views.book_list),
    path('libraries/<int:book_pk>/', views.book_detail),
]
