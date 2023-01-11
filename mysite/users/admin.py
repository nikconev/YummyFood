from django.contrib import admin

# Register your models here.
from mysite.users.models import Profile

admin.site.register(Profile)