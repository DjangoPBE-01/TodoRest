from django.contrib import admin
from apps.todo.models import Category, Task

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']
    ordering = ['-created_at']
    
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'completed', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    ordering = ['-created_at']