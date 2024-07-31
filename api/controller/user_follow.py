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

class User_Follow(APIView):
    def get(self,request,*args,**kwargs):
        user_id_been_follow = self.kwargs.get('user_id')
        author_heads = request.headers.get('Authorization',None)
        user_id,user_name = get_user_id_and_username(author_heads)
        if user_id_been_follow == user_id:
            return Response({"msg":"查看你個人的訊息可以到自己的主頁查看喔！！"})
        if user_id and user_name:
            try:
                user_follow_data = User_Follower.objects.get(user_id = user_id_been_follow,
                                                             user_follow_id=user_id,
                                                             cancel_follow=False)
            except:
                return Response({"msg":"使用者尚未追隨,請先追隨,在查看他的貼文跟資料","status":status.HTTP_403_FORBIDDEN})
            
            try:
                user_profile = UserProfile_models.objects.get(user_id=user_id_been_follow)
                user_profile_dict = model_to_dict(user_profile)
                user_profile_data = {
                    'user_id':user_profile_dict['user_id'],
                    'user_name':user_profile_dict['user_name'],
                    'user_email':user_profile_dict['user_email']
                }
            except Exception as e:
                print(e)
                return Response({"msg":"找不到該位使用者的資料",'status':status.HTTP_404_NOT_FOUND})
            try:
                user_post = PostModels.objects.filter(user=user_id_been_follow).values()
            except:
                user_post = []
            return Response({"msg":"查看該使用者的資料成功",
                             'user_profile':user_profile_data,
                             'user_post':user_post})
        else:
            return Response({"msg":"權限不足請先登入","status":status.HTTP_403_FORBIDDEN})
    def post(self,request,*args,**kwargs):
        user_followed_id = self.kwargs.get('user_id')
        author_heads = request.headers.get('Authorization',None)
        user_id,user_name = get_user_id_and_username(author_heads)
        if user_followed_id == user_id:
            return Response({"msg":"你不能追隨你自己"})
        try:
            User_Follower.objects.get(user_id=user_followed_id,user_follow_id=user_id,cancel_follow=False)
            return Response({"msg":"該位使用者已經被你追隨了,如不追隨可以取消追隨"})
        except:   
            if user_id and user_name:
                try:
                    user_followed_profile = UserProfile_models.objects.get(user_id = user_followed_id)
                    user_followed_profile_dict = model_to_dict(user_followed_profile)
                    user_followed_name = user_followed_profile_dict['user_name']
                    User_Follower.objects.create(user_id=user_followed_id,
                                                user_name=user_followed_name,
                                                user_follow_id=user_id,
                                                user_follow_name=user_name)
                    user_need_delete = User_Follower.objects.filter(user_id=user_followed_id,
                                                 user_follow_id=user_id,
                                                 cancel_follow=True)
                    if user_need_delete:
                        user_need_delete.delete()
                    return Response({"msg":"追隨成功","status":status.HTTP_201_CREATED})
                except Exception as e:
                    return Response({"msg":f"追蹤的使用者不存在","status":status.HTTP_404_NOT_FOUND})
            else:
                return Response({"msg":"權限不足請先登入","status":status.HTTP_403_FORBIDDEN})
        
    def patch(self,request,*args,**kwargs):
        user_followed_id = self.kwargs.get('user_id')
        author_heads = request.headers.get('Authorization',None)
        user_id,user_name = get_user_id_and_username(author_heads)
      
        if not User_Follower.objects.filter(user_id=user_followed_id,user_follow_id=user_id,cancel_follow=False).exists():
            return Response({"msg":"尚未追蹤該位使用者","status":status.HTTP_404_NOT_FOUND})
        
        if user_id and user_name:
            try:
                user_follow_data = User_Follower.objects.filter(user_id=user_followed_id,user_follow_id=user_id,cancel_follow=False)
                user_follow_data.update(cancel_follow = True)
                return Response({"msg":"取消追蹤成功","status":status.HTTP_202_ACCEPTED})
            except Exception as e:
                print(e)
                return Response({"msg":"取消追蹤操作失敗","status":status.HTTP_500_INTERNAL_SERVER_ERROR})
        else:
           return Response({"msg":"權限不足請先登入","status":status.HTTP_403_FORBIDDEN})
        