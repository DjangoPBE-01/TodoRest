from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .permissions import IsOwnerOrReadOnly

from .models import Article


# Create your views here.


class ArticleListCreateView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = Article
    permission_classes = [AllowAny, IsOwnerOrReadOnly]
    
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE', 'POST']:
            self.permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        return super(ArticleListCreateView, self).get_permissions()
    
    