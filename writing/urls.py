from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='writing'),
    path('<str:post_slug>', views.post, name='writing_post')
    ]