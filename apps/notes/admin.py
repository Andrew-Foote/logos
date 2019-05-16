from django.contrib import admin
from apps.notes import models

# Register your models here.

admin.site.register(models.ContentFormat)
admin.site.register(models.Note)
