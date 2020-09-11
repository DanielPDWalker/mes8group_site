from django.db import models
from datetime import datetime


class GeneralModel (models.Model):
    title = models.CharField(max_length=150)
    short_title = models.CharField(max_length=50)

    category = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    subgenre = models.CharField(max_length=100)

    slug = models.SlugField(max_length=100, unique=True)
    publish_date = models.DateTimeField(default=datetime.now, blank=True)
    owner = models.CharField(max_length=50)

    snippet = models.TextField(blank=False, max_length=300)
    content = models.TextField(blank=False)

    thumbnail = models.ImageField(upload_to='thumbnails/', default='default_thumbnail.jpg')

    tags = models.CharField(max_length=200)
    frontpage_feature_slot = models.IntegerField(blank=True, unique=True, null=True)
    category_feature_slot = models.BooleanField(default=False)

    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title