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

class User_Liked_Post_Spec(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"權限不足請先登入","status":status.HTTP_403_FORBIDDEN})
   
        