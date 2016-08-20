from django.contrib import admin

# Register your models here.
from .models import Blog, Author, Entry

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'tagline',
    ]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'email',
    ]

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    pass
