from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, Article, Comment

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comment)