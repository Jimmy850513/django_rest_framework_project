from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from ..models.user_models import UserProfile_models
from datetime import datetime
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.forms.models import model_to_dict
from rest_framework_simplejwt.exceptions import InvalidToken
# Create your views here.

class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self,request,*args,**kwargs):
        username = request.data.get('username',None)
        try:
            user_profile = UserProfile_models.objects.get(user_name=username)
            user_profile_data = model_to_dict(user_profile)
            return Response({
                'user_id': user_profile_data['user_id'], 
                'user_name': user_profile_data['user_name'], 
                'user_email': user_profile_data['user_email'], 
                'user_birthday': user_profile_data.get('user_birthday',''), 
                'tel': user_profile_data.get('tel',''), 
                'mobile': user_profile_data.get('mobile',''), 
                'city': user_profile_data.get('city',''), 
                'district': user_profile_data.get('district',''), 
                'zip': user_profile_data.get('zip',''), 
                'addr': user_profile_data.get('addr','')}
                , status=status.HTTP_200_OK)
        except UserProfile_models.DoesNotExist:
            return Response({'msg': '使用者的資料找不到'}, status=status.HTTP_404_NOT_FOUND)
                
    def put(self,request,*args,**kwargs):
        auth_header = request.headers.get('Authorization',None)
        data_form = request.data
        if auth_header:
            try:
                token = auth_header.split(' ')[1]
                token_payload_dict = JWTAuthentication().get_validated_token(token)
                user_id = token_payload_dict.get('user_profile_id',None)
                if user_id:
                    UserProfile_models.objects.filter(user_id=user_id).update(**data_form)
                    user_profile = UserProfile_models.objects.get(user_id=user_id)
                    user_profile_data = model_to_dict(user_profile)
                    return Response( {'user_id': user_profile_data['user_id'], 
                    'user_name': user_profile_data['user_name'], 
                    'user_email': user_profile_data['user_email'], 
                    'user_birthday': user_profile_data.get('user_birthday',''), 
                    'tel': user_profile_data.get('tel',''), 
                    'mobile': user_profile_data.get('mobile',''), 
                    'city': user_profile_data.get('city',''), 
                    'district': user_profile_data.get('district',''), 
                    'zip': user_profile_data.get('zip',''), 
                    'addr': user_profile_data.get('addr',''),'msg':"更新成功"}
                    , status=status.HTTP_200_OK)
            except:
                return Response({"msg":"找不到使用者！",'status':status.HTTP_404_NOT_FOUND})
        else:
            return Response({"msg":"token 不正確請檢查token",'status':status.HTTP_401_UNAUTHORIZED})
    
   