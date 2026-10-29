from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status


from .permissions import IsOwnerorReadOnly

from .models import Article
from .serializers import ArticleListCreateSerializer


# Create your views here.


class ArticleListCreateView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListCreateSerializer
    permission_classes = [AllowAny, IsOwnerorReadOnly]
    
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE', 'POST']:
            self.permission_classes = [IsAuthenticated, IsOwnerorReadOnly]
        return super(ArticleListCreateView, self).get_permissions()
    
    
    
class ArticleRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListCreateSerializer
    permission_classes = [AllowAny, IsOwnerorReadOnly]
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated, IsOwnerorReadOnly]
        return super(ArticleRetrieveUpdateDestroyView, self).get_permissions()
    
    
    def get_object(self):
        obj = get_object_or_404(Article.objects.filter(is_active=True), pk=self.kwargs['pk'])
        
        self.check_object_permissions(self.request, obj)
        return obj
    
    
    def get(self, request, *args, **kwargs):
        article = self.get_object()
        serializer = self.get_serializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        article = self.get_object()
        serializer = self.get_serializer(article, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def delete(self, request, *args, **kwargs):
        article = self.get_object()
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)