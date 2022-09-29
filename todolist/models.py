from django.db import models
from django.contrib.auth.models import User

class Item_todolist(models.Model):
    date  = models.TextField()
    title  = models.TextField()
    description  = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
