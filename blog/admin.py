from django.contrib import admin

# Register your models here.
from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

admin.site.register(Blog, BlogAdmin)