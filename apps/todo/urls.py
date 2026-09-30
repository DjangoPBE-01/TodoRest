from rest_framework import urls

from apps.todo.views import CategoryView, CategoryDetailUpdateView

urlpatterns = [
    urls.path('category/', CategoryView.as_view(), name='category'),
    urls.path('category/<int:pk>/', CategoryDetailUpdateView.as_view(), name='category-detail'),
]

