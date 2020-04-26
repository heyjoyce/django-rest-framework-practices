from django.contrib import admin
from . import models


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
      'title',
      'author',
    )
