from django.urls import path, include

from . import views as art_views

from general_models import views as general_models_views


urlpatterns = [
    path('', art_views.art_home, name='art_home'),
    path('/<str:post_slug>', general_models_views.general_detail, name='detail')
]