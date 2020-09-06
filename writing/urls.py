from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.writing_home, name='writing_home'),
    path('<str:post_slug>', views.writing_post, name='writing_post')
    ]