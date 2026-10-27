from rest_framework import serializers
from apps.todo.models import Category, Task


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', 'updated_at')
        
class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
        
class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)



class TaskListSerializer(serializers.ModelSerializer):

    category = CategoryListSerializer(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
