from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from ..models.user_models import UserProfile_models
from datetime import datetime
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,get_user_model
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
# Create your views here.

class User_Login(APIView):
    def post(self, request, *args, **kwargs):
        data_from = request.data
        username = data_from.get('username')
        user_password = data_from.get('user_password')
        user = authenticate(username=username,password=user_password)
        user_profile = UserProfile_models.objects.filter(user_name=username).exists()
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            refresh['username'] = username
            refresh['user_id'] = user.id
            if user_profile:
                user_profile_id = UserProfile_models.objects.get(user_name=username)
                refresh['user_profile_id'] = user_profile_id.user_id
            else:
                refresh['user_profile_id'] = None
            return Response({
                'user_id':refresh['user_profile_id'],
                'username':username,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'msg': '帳號密碼錯誤或是要先去註冊！'}, status=status.HTTP_401_UNAUTHORIZED)
    
    
   