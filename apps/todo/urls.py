from rest_framework import urls

from apps.todo.views import (
    CategoryView, 
    CategoryDetailUpdateView,
     
    CategoryGenericListCreateView, 
    CategoryGenericRetrieveUpdateDestroyView,
    
    CategoryListAPIView,
    CategoryCreateAPIView,
    CategoryRetrieveAPIView,
    CategoryUpdateAPIView,
    CategoryDestroyAPIView
    )

urlpatterns = [
    urls.path('category/', CategoryView.as_view(), name='category'),
    urls.path('category/<int:pk>/', CategoryDetailUpdateView.as_view(), name='category-detail'),
    
    
    urls.path('category-generic/', CategoryGenericListCreateView.as_view(), name='category-generic-list-create'),
    urls.path('category-generic/<int:pk>/', CategoryGenericRetrieveUpdateDestroyView.as_view(), name='category-generic-retrieve-update-destroy'),
    
    
    urls.path('category-list/', CategoryListAPIView.as_view(), name='category-list'),
    urls.path('category-create/', CategoryCreateAPIView.as_view(), name='category-create'),
    urls.path('category-retrieve/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category-retrieve'),
    urls.path('category-update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category-update'),    
    urls.path('category-destroy/<int:pk>/', CategoryDestroyAPIView.as_view(), name='category-destroy'),
]

