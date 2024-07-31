from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from ..models.user_models import UserProfile_models
from datetime import datetime
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth.hashers import make_password
# Create your views here.

class User_Register(APIView):
    def post(self,request,*args,**kwargs):
        data_from = request.data
        username = data_from.get('username')
        user_password = data_from.get('user_password')
        user_check_password = data_from.get('user_check_password')
        user_email = data_from.get('user_email')
        msg_return = dict(msg='帳號註冊成功',status_code=status.HTTP_200_OK)
        user = User.objects.filter(username=username).exists()
        user_profile = UserProfile_models.objects.filter(user_name=username).exists()
     
        if user or user_profile:
            msg_return['msg'] = '該帳號已存在'
            msg_return['status_code'] = status.HTTP_500_INTERNAL_SERVER_ERROR
            return Response(msg_return)
        else:
            if not username:
                msg_return['msg'] = '使用者帳號不得為空！'
                msg_return['status_code'] = status.HTTP_500_INTERNAL_SERVER_ERROR
                return Response(msg_return)
            elif user_password != user_check_password:
                msg_return['msg'] = '密碼跟確認密碼不符合！'
                msg_return['status_code'] = status.HTTP_500_INTERNAL_SERVER_ERROR
                return Response(msg_return)
            elif not user_email:
                msg_return['msg'] = 'email不得為空！'
                msg_return['status_code'] = status.HTTP_500_INTERNAL_SERVER_ERROR
                return Response(msg_return)

            user = User.objects.create(username=username,
                                       email=user_email,
                                       password=make_password(user_password)
                                       )
            user.save()

            user_profile = UserProfile_models.objects.create(
                user_name=username,
                user_password=make_password(user_password),
                user_email=user_email
            )
            user_profile.save()
            return Response(msg_return)
    
   