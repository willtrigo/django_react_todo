"""Admin settings."""
from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    """Create display with 'title', 'description' and 'completed'."""
    list_display = ('title', 'description', 'completed')


admin.site.register(Todo, TodoAdmin)
