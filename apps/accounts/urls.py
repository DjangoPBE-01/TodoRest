from django.urls import path

from apps.accounts.views import (
# ExampleView, Example2View
    RegisterUser,
    Login,
    Logout
)


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    
    # path('example/', ExampleView.as_view(), name='example'),
    # path('example2/<int:pk>/', Example2View.as_view(), name='example2'),
]