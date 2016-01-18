from django.contrib import admin
from . import models

admin.site.register(models.Snippet)
admin.site.register(models.Asset)
admin.site.register(models.Series)