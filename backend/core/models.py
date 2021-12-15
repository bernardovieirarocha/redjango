from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class List(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Item(models.Model):
    list = models.ForeignKey(List, on_delete=CASCADE)
    name = models.CharField(max_length=50)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
