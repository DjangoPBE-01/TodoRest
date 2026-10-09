from django.urls import path

from apps.accounts.views import (
# ExampleView, Example2View
    RegisterUser,
#     LoginView,
#     LogoutView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('logout/', Logout.as_view(), name='logout'),
    
    # path('example/', ExampleView.as_view(), name='example'),
    # path('example2/<int:pk>/', Example2View.as_view(), name='example2'),
]