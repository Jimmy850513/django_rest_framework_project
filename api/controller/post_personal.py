from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from ..models.user_models import UserProfile_models
from ..models.post_models import PostModels
from datetime import datetime
from rest_framework import status
from django.forms.models import model_to_dict
from ..utils import get_user_id_and_username
# Create your views here.

#獲取使用者所有的文章
class Post_Views_Personal(APIView):
    def get(self,request,*args,**kwargs):
        author_headers = request.headers.get('Authorization',None)
        if author_headers:
            user_id,user_name = get_user_id_and_username(author_headers)
            try:
                post = PostModels.objects.filter(user_id=user_id)
                posts_data = [model_to_dict(post) for post in post]
                print(posts_data)
                return Response({"msg":"個人文章找到了",'post':posts_data,'status':status.HTTP_200_OK})
            except:
                return Response({"msg":"目前還未張貼個人文章","status":status.HTTP_200_OK})
        else:
            return Response({"msg":"無效用戶,請先登入","status":status.HTTP_403_FORBIDDEN})

    
#獲取使用者單一的貼文    
class Post_Views_Personal_update(APIView):
    def get(self,request,*args,**kwargs):
        post_id = self.kwargs.get('id')
        author_headers = request.headers.get('Authorization',None)
        if author_headers:
            user_id,user_name = get_user_id_and_username(author_headers)
            try:
                post = PostModels.objects.get(post_id=post_id,user_id=user_id)
                post_data = model_to_dict(post)
                print(post_data)
                return Response({"msg":f"{post_data.get('post_title')}的文章找到了","post_detail":{
                    "post_title":post_data.get('post_title'),
                    "post_content":post_data.get('post_content')
                },'status':status.HTTP_200_OK})
            except:
                return Response({"msg":"找不到該文章",'status':status.HTTP_404_NOT_FOUND})
        else:
            return Response({"msg":"要先進行登入,才可查看個人文章",'status':status.HTTP_403_FORBIDDEN})
     
    
    def put(self, request, *args, **kwargs):
        post_id = self.kwargs.get('id')
        author_headers = request.headers.get('Authorization',None)
        data = request.data
        if not data.get('post_title'):
            return Response({"msg":"更新需要文章的title,不得為空",'status':status.HTTP_500_INTERNAL_SERVER_ERROR})
        if not data.get('post_content'):
            return Response({"msg":"更新需要文章的content,不得為空",'status':status.HTTP_500_INTERNAL_SERVER_ERROR})
        if author_headers:
            user_id,user_name = get_user_id_and_username(author_headers)
            try:
                PostModels.objects.filter(post_id=post_id,user_id=user_id).update(
                    post_title=data.get('post_title'),post_content=data.get('post_content')
                )
                post = PostModels.objects.get(user_id=user_id,post_id=post_id)
                return Response({"msg":"更新成功","post_detail":{
                    "post_title":post.post_title,
                    "post_content":post.post_content
                },'status':status.HTTP_202_ACCEPTED})
            except Exception as e:
                print(e)
                return Response({"msg":"找不到該文章,無法更新該文章",'status':status.HTTP_404_NOT_FOUND})
        else:
           return Response({"msg":"要先進行登入,才可更新個人文章",'status':status.HTTP_403_FORBIDDEN})
    
    def delete(self,request,*args,**kwargs):
        post_id = self.kwargs.get('id')
        author_headers = request.headers.get('Authorization',None)
        data = request.data
        if not data.get("is_check_delete"):
            return Response({"msg":"請確認是否刪除該文章確認不得為空,確認請輸入Y",'status':status.HTTP_500_INTERNAL_SERVER_ERROR})
        if author_headers:
            user_id,user_name = get_user_id_and_username(author_headers)
            if data.get("is_check_delete") == 'Y':
                try:
                    PostModels.objects.filter(user_id=user_id,post_id=post_id).delete()
                    post = PostModels.objects.filter(user_id=user_id,post_id=post_id).exists()
                    if post:
                        return Response({"msg":"刪除成功！",'status':status.HTTP_202_ACCEPTED})
                    else:
                        return Response({"msg":"找不到該文章無法刪除",'status':status.HTTP_404_NOT_FOUND})
                except Exception as e:
                    print(e)
                    return Response({"msg":"找不到該文章無法刪除",'status':status.HTTP_404_NOT_FOUND})
            else:
                return Response({"msg":"如要刪除記得輸入Y"})
        else:        
            return Response({"msg":"要先進行登入,才可刪除個人文章",'status':status.HTTP_403_FORBIDDEN})