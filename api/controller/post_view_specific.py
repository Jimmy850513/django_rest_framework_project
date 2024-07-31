from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from ..models.user_models import UserProfile_models
from ..models.post_models import PostModels
from ..models.post_models import PostModels_Comment
from datetime import datetime
from rest_framework import status
from django.forms.models import model_to_dict
from ..utils import get_user_id_and_username
# Create your views here.

class Post_Views_Specific(APIView):
    def get(self,request,*args,**kwargs):
        post_id = self.kwargs.get('id')
        try:
            post = PostModels.objects.get(post_id=post_id)
            post_data = model_to_dict(post)
            post_comment = PostModels_Comment.objects.filter(post_id=post_id).values()
            if post_comment:
                post_data['post_comments'] = [post_comment]
            else:
                post_data['post_comments'] = '目前暫無留言,成為第一個留言的人吧！'
            return Response(post_data)
        except:
            return Response({"msg":"該文章已被刪除了,目前找不到該文章","status":status.HTTP_404_NOT_FOUND})
        
    def post(self,request,*args,**kwargs):
        author_headers = request.headers.get('Authorization',None)
        comment_data = request.data
        post_id = self.kwargs.get('id')
        try:
            post_data = PostModels.objects.get(post_id=post_id)
        except:
            return Response({"msg":"目前找不到該文章,無法進行留言","status":status.HTTP_404_NOT_FOUND})
        if author_headers:
            user_id,user_name = get_user_id_and_username(author_headers)
            if user_id and user_name:
                if comment_data:
                    try:
                        comment = comment_data['post_comment']
                        post_comment_id = PostModels_Comment.objects.create(user_name=user_name,
                                                            comment=comment,
                                                            post_id=post_id,
                                                            user_id=user_id)
                        return Response({"msg":"新增成功","status":status.HTTP_201_CREATED})
                    except Exception as e:
                        return Response({"msg":f"新增留言失敗,失敗原因:{e}","status":status.HTTP_500_INTERNAL_SERVER_ERROR})
                else:
                    return Response({"msg":"要輸入comment進行留言","status":status.HTTP_500_INTERNAL_SERVER_ERROR})
            else:
                return Response({"msg":"權限不足,token認證失敗","status":status.HTTP_403_FORBIDDEN})
        else:
            return Response({"msg":"權限不足,請先登入取得token才可以留言","status":status.HTTP_403_FORBIDDEN})
        
    
    
    
   