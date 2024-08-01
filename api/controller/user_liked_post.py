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

class User_Liked_Post(APIView):
    #選出該使用者喜歡的全部文章
    def get(self,request,*args,**kwargs):
        author_headers = request.headers.get('Authorization',None)
        user_id,user_name = get_user_id_and_username(author_headers)
        if user_id and user_name:
            try:
                like_post = User_Follow_Post.objects.filter(user_id=user_id,user_name=user_name,like_post=True).values()
                for data in like_post:
                    post_id = data['post_id']
                    if PostModels.objects.filter(post_id=post_id).exists():
                        like_post = [{**data}]
                    else:
                        pass
                if like_post:
                    return Response({"msg":f"{user_name}所喜歡的文章","data":like_post,"status":status.HTTP_200_OK})
                else:
                    return Response({"msg":"目前無喜歡的文章","status":status.HTTP_200_OK})
            except Exception as e:
                return Response({"msg":f"發生錯誤:{e}","status":status.HTTP_500_INTERNAL_SERVER_ERRORT})
        else:
            return Response({"msg":"權限不足請先登入","status":status.HTTP_403_FORBIDDEN})
    def post(self,request,*args,**kwargs):
        author_headers = request.headers.get('Authorization',None)
        user_id,user_name = get_user_id_and_username(author_headers)
        data_form = request.data
        if user_id and user_name:
            post_id = data_form.get("post_id")
            if post_id:
                try:
                    post_id_data = PostModels.objects.get(post_id=post_id)
                    post_id_dict = model_to_dict(post_id_data)
                    if post_id_dict['user'] == user_id:
                        return Response({"msg":"該文章是你自己的喔,相信你會喜歡你自己","status":status.HTTP_400_BAD_REQUEST})
                except Exception as e:
                    print(e)
                    return Response({"msg":"找不到該篇文章,文章主人可能已經刪除了","status":status.HTTP_404_NOT_FOUND})
                if post_id_dict:
                    try:
                        User_Follow_Post.objects.create(post_id=post_id_dict['post_id'],
                                                        user_id=user_id,
                                                        user_name=user_name,
                                                        like_post=True
                                                        )
                        return Response({"msg":f"{user_name}喜歡文章{post_id}成功","status":status.HTTP_200_OK})
                    except Exception as e:
                        return Response({"msg":f"發生錯誤：{e}","status":status.HTTP_500_INTERNAL_SERVER_ERROR})                
            else:
                return Response({"msg":"請輸入你要追蹤的文章編號！","status":status.HTTP_400_BAD_REQUEST})
        else:
            return Response({"msg":"權限不足請先登入","status":status.HTTP_403_FORBIDDEN})