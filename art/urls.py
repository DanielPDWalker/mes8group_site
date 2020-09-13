from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.art_home, name='art_home'),
    path('<str:post_slug>', views.art_post, name='art_post')
]