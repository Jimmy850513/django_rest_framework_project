from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from ..models.user_models import UserProfile_models
from ..models.post_models import PostModels
from datetime import datetime
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.forms.models import model_to_dict
# Create your views here.

class Post_Views(APIView):
    def get(self,request,*args,**kwargs):
        all_post = PostModels.objects.all().values()
        if all_post:
            return Response(all_post)
        else:
            return Response({"msg":"目前無文章",'status':status.HTTP_200_OK})
    #新增文章,要確定jwt的token有才可以新增
    def post(self, request, *args, **kwargs):
        author_header = request.headers.get('Authorization',None)
        data = request.data
        if not author_header:
            return Response({'msg': '缺少認證信息'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            token = author_header.split(" ")[1]
            token_payload_dict = JWTAuthentication().get_validated_token(token)
            user_id = token_payload_dict.get('user_profile_id',None)
            user_name = token_payload_dict.get('username',None)
            data_dict = dict(
                user_id=user_id,
                user_name=user_name,
                **data
            )
            if user_id and user_name:
                post = PostModels.objects.create(**data_dict)
                return Response({'msg': '文章創建成功', 'post_id': post.post_id}, 
                                status=status.HTTP_201_CREATED)
            else:
                return Response({'msg': '無效的用戶信息'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'msg': str(e),'status':status.HTTP_500_INTERNAL_SERVER_ERROR})
        
    
    
    
   