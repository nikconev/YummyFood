from django.contrib import admin

# Register your models here.
from mysite.food.models import Item

admin.site.register(Item)
