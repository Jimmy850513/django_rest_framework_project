from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from ..models.user_models import UserProfile_models
from ..models.post_models import PostModels
from ..models.post_models import PostModels_Comment
from ..models.user_models import User_Follower
from datetime import datetime
from rest_framework import status
from django.forms.models import model_to_dict
from ..utils import get_user_id_and_username

class User_Follow_All(APIView):
    def get(self,request,*args,**kwargs):
        author_head = request.headers.get("Authorization",None)
        user_id,user_name = get_user_id_and_username(author_head)
        if user_id and user_name:
            user_follower = User_Follower.objects.filter(user_follow_id=user_id,cancel_follow=False).values('user_id','user_name')
            if user_follower:
                return Response({"msg":"你的追隨的名單已找到","status":status.HTTP_200_OK,
                                 "追隨的名單":user_follower})
            else:
                return Response({"msg":"目前你暫無專隨的使用者","status":status.HTTP_200_OK})
        else:
            return Response({"msg":"權限不足請先登入","status":status.HTTP_403_FORBIDDEN})
   
        