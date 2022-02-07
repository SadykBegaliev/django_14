from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.posts_all, name='post_list'),
    path('hello/', views.hello_world, name='hello_world'),
]
