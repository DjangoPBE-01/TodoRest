from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework.permissions import IsAuthenticated


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from apps.todo.serializers import CategoryListSerializer, CategoryCreateSerializer, CategoryUpdateSerializer
from apps.todo.models import Category, Task



# Create your views here.

class CategoryView(views.APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        
        context = {
            'categories': serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CategoryCreateSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryGenericListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CategoryCreateSerializer
        return super().get_serializer_class()
    

class CategoryDetailUpdateView(views.APIView):
    
    def get (self, request, **kwargs):
        print(kwargs)
        id = kwargs.get('pk')
        category = get_object_or_404(Category, id=id)
        serializer = CategoryListSerializer(instance=category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def put(self, request, **kwargs):
        id = kwargs.get('pk')
        instance = Category.objects.get(id=id)
        serializer = CategoryUpdateSerializer(instance, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, **kwargs):
        id = kwargs.get('pk')
        instance = Category.objects.get(id=id)
        serializer = CategoryUpdateSerializer(instance, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, **kwargs):
        id = kwargs.get('pk')
        category = Category.objects.get(id=id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
        
class CategoryGenericRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return CategoryUpdateSerializer
        return super().get_serializer_class()


    
# List, Create   ------------------------>ListCreateAPIView
# pk get, update, delete  --------------->RetrieveUpdateDestroyAPIView baza 1





class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    
class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategoryCreateSerializer
    

class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    
class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
    

class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()


        
        






