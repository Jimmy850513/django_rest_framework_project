from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from ..models.user_models import UserProfile_models
from ..models.post_models import PostModels
from ..models.post_models import PostModels_Comment
from ..models.user_models import User_Follower
from ..models.user_models import User_Follow_Post
from datetime import datetime
from rest_framework import status
from django.forms.models import model_to_dict
from ..utils import get_user_id_and_username

class User_Liked_Post_Spec(APIView):
    #顯示單篇喜歡的文章
    def get(self,request,*args,**kwargs):
        post_id = self.kwargs.get("post_id",None)
        author_headers = request.headers.get("Authorization",None)
        user_id,user_name = get_user_id_and_username(author_headers)
        if user_id and user_name:
            try:
                post = PostModels.objects.get(post_id=post_id)
                post_dict = model_to_dict(post)
                post_liked_spec = User_Follow_Post.objects.filter(post_id=post_id,user_id=user_id,like_post=True).values()
                post_yourself = PostModels.objects.filter(user_id=user_id,post_id=post_id).values()
                if post_yourself:
                    return Response({"msg":"該文章文自己的文章","status":status.HTTP_400_BAD_REQUEST})
                else:
                    if post_liked_spec:
                        return Response({"msg":"找到該文章成功","data":post_dict,"status":status.HTTP_200_OK})
                    else:
                        return Response({"msg":"尚未喜歡該文章,要先去喜歡才可以查看","status":status.HTTP_400_BAD_REQUEST})
            except Exception as e:
                print(e)
                return Response({"msg":"找不到該文章,可能已經被刪除了","status":status.HTTP_404_NOT_FOUND})  
        else:
            return Response({"msg":"權限不足請先登入","status":status.HTTP_403_FORBIDDEN})
    #取消追蹤喜歡的文章
    def patch(self,request,*args,**kwargs):
        post_id = self.kwargs.get('post_id',None)
        author_headers = request.headers.get("Authorization",None)
        user_id,user_name = get_user_id_and_username(author_headers)
        if user_id and user_name:
            try:
                post = PostModels.objects.get(post_id=post_id)
                post_dict = model_to_dict(post)
                post_yourself = PostModels.objects.filter(user_id=user_id,post_id=post_id).values()
                if post_yourself:
                    return Response({"msg":"該文章文自己的文章,不可以取消追蹤","status":status.HTTP_400_BAD_REQUEST})
                
                post_liked_spec = User_Follow_Post.objects.filter(post_id=post_id,user_id=user_id).exists()
                if post_liked_spec:
                    User_Follow_Post.objects.filter(post_id=post_id,user_id=user_id).update(like_post=False)
                    return Response({"msg":"取消追蹤成功","status":status.HTTP_200_OK})
                else:
                    return Response({"msg":"尚未喜歡該文章,無法執行取消追蹤","status":status.HTTP_400_BAD_REQUEST})
            except Exception as e:
                print(e)
                return Response({"msg":"找不到該文章,可能已經被刪除了","status":status.HTTP_404_NOT_FOUND})  
        else:
            return Response({"msg":"權限不足請先登入","status":status.HTTP_403_FORBIDDEN}) 