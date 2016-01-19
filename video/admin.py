from django.contrib import admin
from . import models


class SnippetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'asset',
        'title',
        'start_time',
        'end_time',
    )

    list_filter = (
        'tags',
    )

    ordering = (
        "-id",
    )


admin.site.register(models.Snippet, SnippetAdmin)
admin.site.register(models.Asset)
admin.site.register(models.Series)
