from django.contrib import admin
from .models import Item, List
from .models import CustomUser

# Register your models here.
# Register your models here.

admin.site.register(List)
admin.site.register(Item)
admin.site.register(CustomUser)
