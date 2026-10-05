from django.db import models
from django.contrib.auth import get_user_model


from apps.base.models import BaseModel

# Create your models here.

User = get_user_model()

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
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Assigned To', related_name='tasks')

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        
    def __str__(self):
        return self.title
