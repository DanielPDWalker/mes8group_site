from django.db import models
from datetime import datetime


class FeatureSlotModel(models.Model):
    slot_number = models.IntegerField()


class WritingModel (models.Model):
    title = models.CharField(max_length=150)
    short_title = models.CharField(max_length=100)

    category = models.CharField(max_length=100, default="writing")
    genre = models.CharField(max_length=100)
    subgenre = models.CharField(max_length=100)

    slug = models.SlugField(max_length=100)
    publish_date = models.DateTimeField(default=datetime.now, blank=True)
    owner = models.CharField(max_length=50)

    snippet = models.TextField(blank=False)
    content= models.TextField(blank=False)

    thumbnail = models.ImageField()

    tags = models.CharField(max_length=200)
    feature_slot = models.OneToOneField(FeatureSlotModel, on_delete= models.DO_NOTHING, default=None)

    def __str__(self):
        return self.title

