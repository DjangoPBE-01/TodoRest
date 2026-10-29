from rest_framework import serializers
from .models import Article


class ArticleListCreateSerializer(serializers.ModelField):
    owner_name = serializers.CharField(source="owner.username", read_only=True)
    
    class Meta:
        model = Article
        fields = ("id", "name", "owner", "owner_name", "description")
        
        
        
        
        

        