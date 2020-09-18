from django.urls import path, include

from . import views as writing_views

from general_models import views as general_models_views


urlpatterns = [
    path('/', writing_views.writing_home, name='writing_home'),
    path('<str:post_slug>', general_models_views.general_detail, name='detail')
]