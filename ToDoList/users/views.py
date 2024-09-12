from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class login(APIView):
    permission_class = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user =  authenticate(username=email, password=password) 
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
class register(APIView):
    pass