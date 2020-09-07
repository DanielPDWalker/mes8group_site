from django.urls import path, include
from django.conf.urls.static import static

from . import views
from mes8group import settings


urlpatterns = [
    path('', views.writing_home, name='writing_home'),
    path('<str:post_slug>', views.writing_post, name='writing_post')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)