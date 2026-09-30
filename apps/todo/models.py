from django.db import models
from apps.base.models import BaseModel

# Create your models here.


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name='Name')
    
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Task(BaseModel):
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category', related_name='tasks')
    completed = models.BooleanField(default=False, verbose_name='Completed')
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        
    def __str__(self):
        return self.title
