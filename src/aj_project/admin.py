from django.contrib import admin
from .models import Article, Comment

# Register your models here.
@admin.register(Article, Comment)
class aj_projectAdmin(admin.ModelAdmin):
    pass
