from django.contrib import admin
from .models import Item, List
from .models import User

# Register your models here.
# Register your models here.

admin.site.register(List)
admin.site.register(Item)
admin.site.register(User)
