from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/likes/', views.likes, name='likes'),
    path('<int:pk>/comment/', views.comments_create, name='comments_create'),
    path(
        '<int:movie_pk>/comment/<int:comment_pk>/delete/',
        views.comment_delete,
        name='comment_delete',
    ),
    path(
        '<int:movie_pk>/sub_comment/<int:comment_pk>/create/',
        views.create_sub_comment,
        name='create_sub_comment',
    ),
    path(
        '<int:movie_pk>/sub_comment/<int:comment_pk>/delete/',
        views.delete_sub_comment,
        name='delete_sub_comment',
    ),
]
