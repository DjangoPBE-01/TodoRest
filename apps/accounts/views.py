from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout 
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# from rest_framework.authtoken.models import Token

from .serializers import RegisterUserSerializer

# Create your views here.

User = get_user_model()

class RegisterUser(CreateAPIView):
    serializer_class = RegisterUserSerializer
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.pop('confirm_password', None)  # Remove confirm_password from the response data
        # Endi perform_create userni qaytaradi
        user = serializer.save(is_active=False)  # Set the user as inactive until email verification
        
        # Send verification email
        self.send_verification_email(user)
        
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def perform_create(self, serializer):        
        serializer.save(is_active=False) # Set the user as inactive until email verification
       
    
    
    
    def send_verification_email(self, user):
        
        activation_link = f"{settings.FRONTEND_URL}verify-email/{user.id}/"
        
        subject = 'Welcome to Our Platform'
        message = f'Hi {user.username},\n\nThank you for registering at our platform! Please click the link below to verify your email address:\n\n{activation_link}\n\nIf you did not register, please ignore this email.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]
        
        send_mail(subject, message, from_email, recipient_list)

class ConfirmEmailView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            if user.is_active:
                return Response({'message': 'Email already verified.'}, status=status.HTTP_400_BAD_REQUEST)
            user.is_active = True
            user.save()
            return Response({'message': 'Email verified successfully!'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Invalid verification link.'}, status=status.HTTP_400_BAD_REQUEST)
    
    





# token auth
# class LoginView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         user = authenticate(username=email, password=password)

#         if user:
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key})
#         return Response({"error": "Invalid credentials"}, status=400)


# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         user = request.user
#         user.auth_token.delete()
#         return Response({"message": "Logged out successfully"})



# session auth    

# class Login(APIView):
    
#     def post(self, request, *args, **kwargs):
#         email = request.data.get('email')
#         password = request.data.get('password')
        
#         user = authenticate(request, email=email, password=password)
        
#         if user is not None:
#             login(request, user)
#             return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        



# from django.conf import settings
# class Logout(APIView):
#     permission_classes = [IsAuthenticated]
    
#     def post(self, request, *args, **kwargs):
       
#         user = request.user
        
    
#         if request.session:
#             request.session.flush()  # Foydalanuvchiga tegishli barcha sessiya ma'lumotlarini o'chirish
            
#         logout(request)
        
#         # 2. Brauzer kukilarini tozalash uchun javob tayyorlaymiz
#         response = Response(
#             {'message': f'User {user.username} logged out successfully'}, 
#             status=status.HTTP_200_OK
#         )
        
#         # Kuki nomlarini sozlamalardan olib o'chiramiz
#         response.delete_cookie(settings.SESSION_COOKIE_NAME)
#         response.delete_cookie('csrftoken')
        
#         return response
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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

