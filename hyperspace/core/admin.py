
from django.contrib import admin
from blog.models import Blog  


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author')
    search_fields = ('title', 'description', 'author')  # Enable search functionality in the admin interface
    list_filter = ['author']
    raw_id_fields = ['author']  # Enable filtering by author in the admin interface


