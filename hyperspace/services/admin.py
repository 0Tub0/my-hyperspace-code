from django.contrib import admin
from .models import Service  # Import the Service model from models.py

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'slug')
    search_fields = ('title', 'description')  # Enable search functionality in the admin interface
    list_filter = ('is_featured',)