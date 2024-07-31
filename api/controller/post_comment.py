from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from ..models.user_models import UserProfile_models
from ..models.post_models import PostModels
from ..models.post_models import PostModels_Comment
from datetime import datetime
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.forms.models import model_to_dict
from ..utils import get_user_id_and_username
# Create your views here.

class Post_Views_Comment(APIView):
    def put(self,request,*args,**kwargs):
        comment_id = self.kwargs.get("comment_id")
        try:
            comment_data = PostModels_Comment.objects.get(comment_id = comment_id)
            comment_data_dict = model_to_dict(comment_data)
            print(comment_data_dict)
            if comment_data_dict:
                comment_user_id = comment_data_dict['user']
            else:
                comment_user_id = 0
        except Exception as e:
            print(e)
            return Response({"msg":"找不到該則留言","status":status.HTTP_404_NOT_FOUND})
                   
        data_form = request.data
        comment_update_data = data_form.get("post_comment")
        author_headers = request.headers.get('Authorization',None)
        user_id,user_name = get_user_id_and_username(author_headers)
        if comment_user_id:
            if user_id != comment_user_id:
                return Response({"msg":"請選擇你自己的留言進行更新,無權限更新他人的留言",
                                 "status":status.HTTP_403_FORBIDDEN})
            if user_id and user_name:
                if comment_update_data:
                    try:
                        post_update = PostModels_Comment.objects.filter(
                            comment_id=comment_id,user_id=user_id,user_name=user_name
                            ).update(comment=comment_update_data)
                        return Response({"msg":f"更新成功","status":status.HTTP_200_OK})
                    except Exception as e:
                        return Response({"msg":f"{e}","status":status.HTTP_500_INTERNAL_SERVER_ERROR})
                else:
                    return Response({"msg":"更新失敗,要輸入要更新的內容！","status":status.HTTP_500_INTERNAL_SERVER_ERROR})
        else:
            return Response({"msg":"請點選留言進行更新！未點選無法更新","status":status.HTTP_404_NOT_FOUND})    
               

    
    def delete(self,request,*args,**kwargs):
        comment_id = self.kwargs.get("comment_id")
        author_headers = request.headers.get('Authorization',None)
        user_id,user_name = get_user_id_and_username(author_headers)
        if user_id and user_name:
            try:
                PostModels_Comment.objects.get(comment_id = comment_id).delete()
                return Response({"msg":"刪除成功","status":status.HTTP_200_OK})
            except:
                return Response({"msg":"找不到該留言刪除！","status":status.HTTP_404_NOT_FOUND})
        else:
            return Response({"msg":"權限不足請先登入！","status":status.HTTP_403_FORBIDDEN})
    
   