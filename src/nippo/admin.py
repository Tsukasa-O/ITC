from django.contrib import admin

# Register your models here.
from .models import NippoModel #追記

admin.site.register(NippoModel) #追記