from django.contrib import admin
from django.urls import path
from .controller.user_profile import UserProfile
from .controller.user_register import User_Register
from .controller.user_login import User_Login
from .controller.post import Post_Views
from .controller.post_personal import Post_Views_Personal,Post_Views_Personal_update
from .controller.post_view_specific import Post_Views_Specific
from .controller.post_comment import Post_Views_Comment
from .controller.user_follow import User_Follow
from .controller.user_all_follow import User_Follow_All
from .controller.user_liked_post import User_Liked_Post
from .controller.user_liked_post_specifice import User_Liked_Post_Spec
urlpatterns = [
  path('api/user_profile/',UserProfile.as_view(),name='user_profile'),
  path('api/user_register/',User_Register.as_view(),name='user_register'),
  path('api/user_login/',User_Login.as_view(),name='user_login'),
  path('api/post_views/',Post_Views.as_view(),name='post_views'),
  path('api/post_views_personal/',Post_Views_Personal.as_view(),name='post_views_personal'),
  #使用者的自己的貼文
  path('api/post_views_by_id/<int:id>/',Post_Views_Personal_update.as_view(),name='post_view_by_id'),
  #瀏覽特定文章,不需要jwt token就可以看
  path('api/post_views_specific/<int:id>/',Post_Views_Specific.as_view(),name='post_views_specific'),
  #對指定貼文進行留言的話,需要jwt token才可以留言,對留言可以進行刪改查的動作
  path('api/post_views_comment/<int:comment_id>/',Post_Views_Comment.as_view(),name='post_views_comment'),
  #追隨指定的使用者#查看追隨使用者的貼文,可以取消追隨#查看該使用者的個人資料
  path("api/user_follow/<int:user_id>",User_Follow.as_view(),name='user_follow'),
  #查看當前使用者的所有追蹤文章清單
  path("api/user_liked_post/",User_Liked_Post.as_view(),name='user_liked_post'),
  #取消追蹤當前使用者的特定喜歡的文章追隨,新增當前使用者的特定喜歡的文章清單
  path("api/user_liked_post_spec/",User_Liked_Post_Spec.as_view(),name='user_liked_post_spec'),
  #查看當前使用者的追隨者清單
  path("api/user_follow_all/",User_Follow_All.as_view(),name='user_follow_all')
]
