from django.db import models

class Item_MyWatchList(models.Model):
    watched = models.CharField(max_length=255)
    title = models.TextField(default="")
    rating = models.IntegerField(default=0)
    release_date = models.TextField(default="")
    review = models.TextField(default="")
