from django.contrib import admin
from .models import Item, List

# Register your models here.

admin.site.register(List)
admin.site.register(Item)