from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout 

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterUserSerializer

# Create your views here.



class RegisterUser(CreateAPIView):
    serializer_class = RegisterUserSerializer
    

class Login(APIView):
    
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        



from django.conf import settings
class Logout(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
       
        user = request.user
        
    
        if request.session:
            request.session.flush()  # Foydalanuvchiga tegishli barcha sessiya ma'lumotlarini o'chirish
            
        logout(request)
        
        # 2. Brauzer kukilarini tozalash uchun javob tayyorlaymiz
        response = Response(
            {'message': f'User {user.username} logged out successfully'}, 
            status=status.HTTP_200_OK
        )
        
        # Kuki nomlarini sozlamalardan olib o'chiramiz
        response.delete_cookie(settings.SESSION_COOKIE_NAME)
        response.delete_cookie('csrftoken')
        
        return response
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# class ExampleView(APIView):
#     def get(self, request, *args, **kwargs):
        
#         print(request)
#         query_params = request.query_params
        
#         print(query_params)
        
#         name = query_params.get('name')
#         fullname = query_params.get('fullname')
        
        
#         print(name, fullname, "##################################")
        
#         return Response({'message': query_params}, status=status.HTTP_200_OK)
    
    
# class Example2View(APIView):
#     def get(self, request, *args, **kwargs):
        
        
#         path_args = kwargs.get('pk')
#         print(path_args, "##################################")
        
#         header = request.headers
#         print(header, "##################################")
        
#         body = request.data
#         print(body, "##################################")
        
#         return Response({'message': path_args, 'headers': header, 'body': body}, status=status.HTTP_200_OK)

